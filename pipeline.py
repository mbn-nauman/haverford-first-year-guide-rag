import os
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

DOCUMENTS_DIR = "documents"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "haverford_guide"

_model = None
_collection = None


def get_model():
    global _model
    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        _collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection

# Maps filename → (title, url)
DOCUMENT_METADATA = {
    "Information about all the residential housing on-campus.txt": (
        "A Guide to Residential Life at Haverford",
        "https://www.reddit.com/r/Haverford/comments/1tj0y90/a_guide_to_residential_life_at_haverford/",
    ),
    "Social Scene at Haverford.txt": (
        "Social Scene at Haverford",
        "https://www.reddit.com/r/Haverford/comments/ti98st/social_scene_at_haverford/",
    ),
    "Reddit thread for QnA about Haverford.txt": (
        "Reddit QnA about Haverford",
        "https://www.reddit.com/r/Haverford/comments/7ngl51/anyone_who_is_applying_have_questions_about/",
    ),
    "Another advice QnA thread.txt": (
        "Another Advice/QnA Thread",
        "https://www.reddit.com/r/Haverford/comments/1bfvbeg/class_of_27_28/",
    ),
    "A freshman guide to Haverford College.txt": (
        "A Freshman Guide to Haverford College",
        "https://generalintelligences.wordpress.com/2020/05/16/a-freshman-guide-to-haverford-college/",
    ),
    "Freshman reflection on first month of Haverford College.txt": (
        "Freshmen Reflect on the First Month of College",
        "https://haverfordclerk.com/freshmen-reflect-on-the-first-month-of-college/",
    ),
    "A first-year's experience about Customs (Orientation).txt": (
        "Customs Gave Me a Community: A First-Year Perspective",
        "https://haverfordclerk.com/customs-gave-me-a-community-a-first-year-perspective/",
    ),
    "Dining Culture at Haverford according to a Transfer Student.txt": (
        "Handle With Care: Is Our Dining Center Culture Healthy?",
        "https://haverfordclerk.com/handle-with-care-is-our-dining-center-culture-healthy/",
    ),
    "Haverford vs Bryn Mawr Dining Halls.txt": (
        "Haverford vs Bryn Mawr Dining Halls",
        "https://bicollegenews.com/2019/10/05/opinion-haverford-vs-bryn-mawrs-dining-halls/",
    ),
    "Campus Life Review of Haverford.txt": (
        "Campus Life Review of Haverford",
        "https://www.niche.com/colleges/haverford-college/campus-life/",
    ),
}


def load_documents():
    documents = []
    for filename, (title, url) in DOCUMENT_METADATA.items():
        filepath = os.path.join(DOCUMENTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read().strip()
        documents.append({"title": title, "url": url, "text": text})
    return documents


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        line_number = text[:start].count("\n") + 1
        chunks.append({"text": text[start:end], "line_number": line_number})
        start += chunk_size - overlap
    return chunks


def build_chunks(documents):
    all_chunks = []
    for doc in documents:
        for chunk in chunk_text(doc["text"]):
            all_chunks.append({
                "title": doc["title"],
                "url": doc["url"],
                "text": chunk["text"],
                "line_number": chunk["line_number"],
            })
    return all_chunks


def embed_and_store(chunks):
    model = get_model()
    collection = get_collection()

    # Skip if already populated
    if collection.count() > 0:
        print(f"Collection already has {collection.count()} chunks — skipping embedding.")
        return

    texts = [c["text"] for c in chunks]
    print(f"Embedding {len(texts)} chunks...")
    embeddings = model.encode(texts, show_progress_bar=True).tolist()

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        embeddings=embeddings,
        documents=texts,
        metadatas=[{"title": c["title"], "url": c["url"], "line_number": c["line_number"]} for c in chunks],
    )
    print(f"Stored {len(chunks)} chunks in ChromaDB.\n")


def retrieve(query, top_k=4):
    model = get_model()
    collection = get_collection()

    query_embedding = model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)

    chunks = []
    for i in range(len(results["documents"][0])):
        chunks.append({
            "distance": results["distances"][0][i],
            "text": results["documents"][0][i],
            "title": results["metadatas"][0][i]["title"],
            "url": results["metadatas"][0][i]["url"],
            "line_number": results["metadatas"][0][i]["line_number"],
        })
    chunks.sort(key=lambda c: c["distance"])
    return chunks


NO_ANSWER = "The answer to your question is not in our database."
DISTANCE_THRESHOLD = 0.7

def generate(query, top_k=4):
    chunks = retrieve(query, top_k=top_k)

    if not chunks or chunks[0]["distance"] > DISTANCE_THRESHOLD:
        return {"answer": NO_ANSWER, "sources": []}

    context_blocks = []
    for chunk in chunks:
        context_blocks.append(chunk['text'])
    context = "\n\n---\n\n".join(context_blocks)

    system_prompt = (
        "You are a senior at Haverford College answering questions from an incoming first-year. "
        "You have read some notes below. Use only what is in those notes to answer. "
        "Speak naturally and directly — like you are texting a friend. "
        "Give a clear answer in 2-4 sentences. "
        "BAD example (never do this): 'According to Source 1, classes are hard. Source 2 implies...' "
        "GOOD example (always do this): 'Classes are genuinely tough — most students find the workload heavy, "
        "especially early on. The small class sizes help though, usually 5-20 people, so professors actually know you.' "
        "Never mention sources, documents, or notes in your answer. Never use 'according to', 'it implies', "
        "'it appears', 'Source 1', or any similar phrase. "
        "If the notes don't contain enough to answer, reply with exactly: "
        '"The answer to your question is not in our database."'
    )

    user_prompt = f"Use the following information to answer the question:\n\n{context}\n\nQuestion: {query}"

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    answer = response.choices[0].message.content

    seen = set()
    sources = []
    for chunk in chunks:
        key = chunk["url"]
        if key not in seen:
            seen.add(key)
            sources.append(f"{chunk['title']} — {chunk['url']}")

    return {"answer": answer, "sources": sources}


if __name__ == "__main__":
    documents = load_documents()
    print(f"Loaded {len(documents)} documents\n")

    all_chunks = build_chunks(documents)
    print(f"Total chunks: {len(all_chunks)}\n")

    embed_and_store(all_chunks)

    # Test retrieval
    test_query = "What are the freshman dorms like?"
    print(f"Test query: '{test_query}'\n")
    results = retrieve(test_query)
    for i, r in enumerate(results):
        print(f"[Result {i+1}] {r['title']}")
        print(f"URL: {r['url']}")
        print(f"Text: {r['text'][:300]}...")
        print()
