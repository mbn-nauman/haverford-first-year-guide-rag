# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

Haverford College incoming first-year survival guide. This information is generally hard to find because it is throught the student's perspectives so it is not on official college website, but instead it is scattered on places like reddit threads, student news paper articles and review sites.
---

## Documents

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Reddit | Information about all the residential housing on-campus | https://www.reddit.com/r/Haverford/comments/1tj0y90/a_guide_to_residential_life_at_haverford/ |
| 2 | Reddit | Social Scene at Haverford | https://www.reddit.com/r/Haverford/comments/ti98st/social_scene_at_haverford/ |
| 3 | Reddit | Reddit thread for QnA about Haverford | https://www.reddit.com/r/Haverford/comments/7ngl51/anyone_who_is_applying_have_questions_about/ |
| 4 | Reddit | Another advice/QnA thread | https://www.reddit.com/r/Haverford/comments/1bfvbeg/class_of_27_28/ |
| 5 | WordPress | A freshman guide to Haverford College | https://generalintelligences.wordpress.com/2020/05/16/a-freshman-guide-to-haverford-college/ |
| 6 | The Clerk | Freshman reflection on first month of Haverford College | https://haverfordclerk.com/freshmen-reflect-on-the-first-month-of-college/ |
| 7 | The Clerk | A first-year's experience about Customs (Orientation) | https://haverfordclerk.com/customs-gave-me-a-community-a-first-year-perspective/ |
| 8 | The Clerk | Dining Culture at Haverford according to a Transfer Student | https://haverfordclerk.com/handle-with-care-is-our-dining-center-culture-healthy/ |
| 9 | The Bi-College News | Haverford vs Bryn Mawr Dining Halls | https://bicollegenews.com/2019/10/05/opinion-haverford-vs-bryn-mawrs-dining-halls/ |
| 10 | Niche | Campus Life Review of Haverford | https://www.niche.com/colleges/haverford-college/campus-life/ |

---

## Chunking Strategy

**Chunk size:**
500 characters
**Overlap:**
100 characters
**Reasoning:**
As my documents include reddit comments, student reviews etc, I chose a chunk size which is big enough to extract the student's experience and small enough to preserve the context. I first tried 1000 characters with 200 character overlap but that was leading to the retreival of chunks with high distances. So, I then tested multiple different pairs of chunk size and overlap size to choose the best one. I tested chunk sizes of 1000, 300, 700, and 500. In the end, I concluded that 500 was the best one because it retreived the comparitively lowest distance for the chunks.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers
**Top-k:**
4
**Production tradeoff reflection:**
If cost was not a constraint then I would choose a stronger model which would have a higher context length and accuracy on domain-specific text as my sources are messy reddit threads and student reviews. That would make my output answers more accurate. Also, I would go for a multilingual model too because that would give the user option to ask question in another language and while giving answer, the LLM can translate the answer into the langaue the user asked the question in.
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | How far are the apartments from Tritton Hall. | About 3 minutes of walk |
| 2 | How many students are there in one class usually? | 5-20 students per class |
| 3 | How did first-years feel about the Customs program compared to their expectations before arriving? | They felt skeptical about it before coming but later found that it genuinely built community and one student described it as "sleepaway camp for college students" |
| 4 | How should students manage classes at Haverford? | The classes are generally challenging so students should organize their schedule early, leave time for homework and exams, use weekends to catchup on the work. |
| 5 | Do people eat dinner alone or with friends at Haverford? | Breakfast and Lunch are usually done alone at Haverford because of different schedules but dinner is more like a group activity. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.
If a student makes a claim and then gives reasoning later in the article, then the chunks would get split up and the LLM might give an answer without proper reasoning.
2.
As my documents are all student written scattered over the internet on different websites, written on different dates, some infomation might be outdated, opinionated, and can lead to the LLM giving a subjective answer in a way that is fully true.
---

## Architecture

Document Ingestion → Python loaders and cleaned source files
Chunking → Fixed size chunking with each chunk of 1000 characters with a 200 character overlap
Embedding + Vector Store → all-MiniLM-L6-v2 via sentence-transformers + ChromaDB
Retrieval → ChromaDB search with top-k = 4
Generation → GrokAPI: llama-3.3-70b-versatile, citations must be added in the answer

---

## AI Tool Plan


**Milestone 3 — Ingestion and chunking:**

Document Injestion: I will use Claude to help with the document injestion. I will clean all the documents manually which I can, and ask ChatGPT to help me with any which I cannot and then save all of them as seperate .txt files. I will tell Claude then that I want to get a simple Python structure which will help me save the title, url and the cleaned text.

Chunkiung: I will give claude my chunking strategy section and ask it to implement a chunking function.

**Milestone 4 — Embedding and retrieval:**

Embedding: I will tell claude that we will use the all-MiniLM-L6-v2 model via sentence-transformers

Retreival: I will ask claude to see my retrieval approach section and see the tradeoff and also the top-k = 4. I will also be using a limit on the maximum distance on the top chunk which would be 0.7. If it is more than 0.7 then just say the default no answer sentence. If the top chunk is less than 0.7, then send chunks to the LLM for answer generation.

**Milestone 5 — Generation and interface:**

Generation: I will ask claude to implement GrokAPI: llama-3.3-70b-versatile for the answer/output generation. I will also tell it to make sure to add citation to every answer and in any case when there is no answer, then just tell the user "The answer to your question is not in our database." 

(Claude Ai was used to write the Interface planning part -- I initally used Gradio but that was too simple and I was unable to add the Crimson Red Haverford College Logo color with it so I shfted to StreamLit)

Interface: Build a chat-style interface using Streamlit with st.chat_message and st.chat_input so the UI looks like a real AI assistant. Use a .streamlit/config.toml to apply Haverford's black and crimson color scheme. Sources for each answer will appear in a collapsible expander below the assistant's message. Chat history is preserved in st.session_state for the duration of the session. 