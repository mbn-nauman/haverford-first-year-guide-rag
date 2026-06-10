# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

Haverford College incoming first-year survival guide. This information is generally hard to find because it is through the student's perspectives so it is not on official college website, but instead it is scattered on places like reddit threads, student news paper articles and review sites.

---

## Document Sources

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
500 characters

**Overlap:**
100 characters

**Reasoning:**
As my documents include reddit comments, student reviews etc, I chose a chunk size which is big enough to extract the student's experience and small enough to preserve the context. I first tried 1000 characters with 200 character overlap but that was leading to the retreival of chunks with high distances. So, I then tested multiple different pairs of chunk size and overlap size to choose the best one. I tested chunk sizes of 1000, 300, 700, and 500. In the end, I concluded that 500 was the best one because it retreived the comparitively lowest distance for the chunks.

**Final chunk count:**
156

---

## Sample Chunks

**Chunk 1** — Source: A Guide to Residential Life at Haverford
> Tritton is all single dorms. It has four quadrants of 20 people who all have their own singles. The layout is kind of like a hotel; you walk down the halls and there are rooms to one side. Each group of 20 shares a common room (which has a big TV, couches, and a kitchenette), two bathrooms (4 showers and 6 stalls total), and a laundry room (two washers and two dryers). Tritton is generally regarded as one of the quieter dorms on campus.

**Chunk 2** — Source: A Freshman Guide to Haverford College
> Classes here are very challenging, and you would be taught by amazing professors who are passionate about teaching. Most classes are small, ranging anywhere from 5-20 people per class. Intro-level classes might be significantly larger in size, but the smaller setting allows for more student engagement. The professors can get to know you better, and you would not feel like another face in the class.

**Chunk 3** — Source: Customs Gave Me a Community: A First-Year Perspective
> In my experience at Haverford, the Customs program was integral in creating a welcoming environment. My good friend perfectly described this one-of-a-kind orientation as sleepaway camp for college students. Fun-filled activities consumed the day and night for the new students. After a hectic move-in, Customs began with a personal and sincere message from the President of the College herself, Wendy Raymond.

**Chunk 4** — Source: Handle With Care: Is Our Dining Center Culture Healthy?
> Since customs week it has been instilled in me that most Haverford students find it acceptable to go to breakfast or lunch alone, mainly because our daily schedules do not always match up with our friends' schedules. However, dinner at Haverford is a group activity. Many students I talked to have chosen the take-out option for dinner when they had no one to sit with, too uncomfortable with the idea of sitting alone at a large table.

**Chunk 5** — Source: Freshmen Reflect on the First Month of College
> Bi also attributed many newfound friendships to the active role she took in joining "clubs…to meet new people." Phoebe Hawthorne '29 was also appreciative of the many clubs and activities present on campus. Two freshmen, Logan White and Harry Kallen, also expressed gratitude for the kindness of people at Haverford, with Kallen saying, "I've never met this amount of nice people."

---

## Retrieval Test Results

### Q1: How far are the apartments from Tritton Hall?

| Rank | Distance | Source | Chunk preview |
|------|----------|--------|---------------|
| 1 | 0.4273 | A Guide to Residential Life at Haverford | "...if it was possible to get floor plans for the residence halls. I was able to look at the blueprints for Tritton because the architectural firm has published them online..." |
| 2 | 0.4548 | A Guide to Residential Life at Haverford | "...Kim Hall: Mirror image of Tritton... HCA (Haverford Apartments): Located on the southernmost end of campus..." |
| 3 | 0.4788 | A Guide to Residential Life at Haverford | "A Guide to Residential Life at Haverford. When arriving at Haverford, I wanted to know as much about the dorms as possible..." |
| 4 | 0.5127 | A Guide to Residential Life at Haverford | "Tritton is all single dorms. It has four quadrants of 20 people who all have their own singles..." |

---

### Q2: How many students are there in one class usually?

| Rank | Distance | Source | Chunk preview |
|------|----------|--------|---------------|
| 1 | 0.3654 | A Freshman Guide to Haverford College | "...ranging anywhere from 5-20 people per class. Intro-level classes might be significantly larger in size, but the smaller setting allows for more student engagement..." |
| 2 | 0.5428 | A Guide to Residential Life at Haverford | "Tritton is all single dorms. It has four quadrants of 20 people who all have their own singles..." |
| 3 | 0.5625 | Handle With Care: Is Our Dining Center Culture Healthy? | "...simply less stressful with 50 people around you, as opposed to 250..." |
| 4 | 0.5726 | Handle With Care: Is Our Dining Center Culture Healthy? | "...dinner at Haverford is a group activity. Many students I talked to have chosen the take-out option for dinner..." |

---

### Q4: How should students manage classes at Haverford?

| Rank | Distance | Source | Chunk preview |
|------|----------|--------|---------------|
| 1 | 0.3186 | A Freshman Guide to Haverford College | "Classes at Haverford are definitely very challenging, and you are taught by some of the best professors out there..." |
| 2 | 0.3235 | A Freshman Guide to Haverford College | "...I think my most important advice is this: Go into Haverford with an open mind and make the journey your own." |
| 3 | 0.3529 | A Freshman Guide to Haverford College | "...taking classes at University of Pennsylvania requires more planning. Study spots on campus: Lutnick Library is often packed, but some other amazing spots are the Science Library, CPGC Cafe in Stokes..." |
| 4 | 0.3647 | Reddit QnA about Haverford | "Haverford does foster an environment that is open to civil debate... Food is okay, there's one dining hall and then the Coop..." |

---

## Embedding Model

**Model used:**
all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:**
If cost was not a constraint then I would choose a stronger model which would have a higher context length and accuracy on domain-specific text as my sources are messy reddit threads and student reviews. That would make my output answers more accurate. Also, I would go for a multilingual model too because that would give the user option to ask question in another language and while giving answer, the LLM can translate the answer into the langauge the user asked the question in.

---

## Grounded Generation

**System prompt grounding instruction:**
The system prompt tells the model to act like a senior Haverford College student. It tells the model to only use the notes (top-k chunks) it has been given to give the answer to the query. The model is also told to speak directly and like a friend and is explicitly told not to use phrases like "according to", "Source 1" etc. These explicit phrases were added later because when in testing, it was seen that the model was giving citations within the answer. The model is also told to not to give its own interpretation like "this implies.." as the model was doing it when the it was being tested. In the end the model is strictly told to answer with ""The answer to your question is not in our database" when the answer is not in the chunks. If the top most chunk (as my chunks are ordered by increasing distance) has a distance of greater than 0.7, then the LLM is never called. Instead an automatic response of the same line "The answer to your question is not in our database" is given. This was done so the LLM does not hallucinate the answer.

**How source attribution is surfaced in the response:**
The source attribution (or citations) are not left to the LLM to do. Instead, we do it programmatically. After the generation by the LLM is done, the code extracts the title of the document and its URL from the metadata of the chunks and uses those to build a source list in Python. This list then appears as embedded links in the Streamlit UI beneath the answer.

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | How far are the apartments from Tritton Hall. | About 3 minutes of walk |Distance not specified in documents. (summarized using Claude) | Partially relevant, they are from the right document but do not contain the correct chunk for the answer | Inaccurate, the system said that the distance is not specified but it is in the document which makes it a retreival error and not a generation error. |
| 2 | How many students are there in one class usually? | 5-20 students per class | 5-20 students per class; intro courses may be larger. (summarized using Claude) | Partially Relevant, the first chunk is the exact one with the answer in it. The other three chunks are off topic. They most probably were retreived because they had words like "students" and "people". | Accurate, the LLM got the answer exactly right. It got the answer from the top chunk and ignored the rest of them. |
| 3 | How did first-years feel about the Customs program compared to their expectations before arriving? | They felt skeptical about it before coming but later found that it genuinely built community and one student described it as "sleepaway camp for college students" | Skeptical beforehand, but pleasantly surprised — Customs genuinely built community, described as 'sleepaway camp for college students. (summarized using Claude) | Relevant, all distances are pretty low and contain the direct answer to the question. | Accurate, the answer is fully accurate according to the chunks the LLM received and the expected answer. | 
| 4 | How should students manage classes at Haverford? | The classes are generally challenging so students should organize their schedule early, leave time for homework and exams, use weekends to catchup on the work. | Plan schedule early, account for Penn transport time if cross-registering, and find a good study spot like the Science Library or CPGC Cafe. (summarized using Claude) | Partially Relevant, 2 out of the 4 chunks were useful. The first and third chunk had the information we needed, while the second and fourth chunk were too vague or off-topic. | Partially Accurate, the answer is correct but not the same as the expected answer. The LLM took the right information from the correct chunks and ignored the vage/off-topic ones, but it was not the answer we expected. 
| 5 | Do people eat dinner alone or with friends at Haverford? | Breakfast and Lunch are usually done alone at Haverford because of different schedules but dinner is more like a group activity. | Dinner is a group activity — students arrive with friends, often post-sports practice. Eating alone feels uncomfortable; some take-out to avoid it. (summarized using Claude) | Relevant, as all 4 chunks are from the right document and with the lowest distance when compared to the other 4 questions before this. | Partially Accurate, it answered the part about dinner but missed the breakfast and lunch part. | 

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
