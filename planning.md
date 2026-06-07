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
| 5 | Reddit | A freshman guide to Haverford College | https://generalintelligences.wordpress.com/2020/05/16/a-freshman-guide-to-haverford-college/ |
| 6 | The Clerk | Freshman reflection on first month of Haverford College | https://haverfordclerk.com/freshmen-reflect-on-the-first-month-of-college/ |
| 7 | The Clerk | A first-year's experience about Customs (Orientation) | https://haverfordclerk.com/customs-gave-me-a-community-a-first-year-perspective/ |
| 8 | The Clerk | Dining Culture at Haverford according to a Transfer Student | https://haverfordclerk.com/handle-with-care-is-our-dining-center-culture-healthy/ |
| 9 | The Bi-College News | Haverford vs Bryn Mawr Dining Halls | https://bicollegenews.com/2019/10/05/opinion-haverford-vs-bryn-mawrs-dining-halls/ |
| 10 | Niche | Campus Life Review of Haverford | https://www.niche.com/colleges/haverford-college/campus-life/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
1000
**Overlap:**
200
**Reasoning:**
As my documents include reddit comments, student reviews etc, I chose a chunk size of 1000 and overlap of 200 so that it is big enough to extract the student's experience and small enough to preserve the context. 

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
| 3 | Does the customs program help build community and friends? | Yes, it helps build community and friends. |
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

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
