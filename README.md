#README

Notes and Cheatsheet of DSA goes here. Mainly used as target practice to hone my python skills up. Might need to go deep into the internals of FastAPI/async or whatever the companies I like use.












---


## Introduction

● You will be expected to write some code, usually on a whiteboard or a
notebook
● The problem will usually have several reasonable solutions of varying time
and space complexity, and your goal is to eventually arrive at the optimal
one
● They usually test purely algorithmic knowledge, but sometimes they include
domain knowledge like details of C++ syntax (if you’re applying to a C++
role)
● They will also sometimes require writing a lot of code very quickly (Citadel
and Jane Street love to do this

● The do-you-know-this-language interview:
	○ “Please explain what the Virtual keyword does in C++”
● The write-a-lot-of-code-quickly interview:
	○ “Here is a (somewhat open-ended?) problem with low-algorithmic content, please write a
	reasonable solution and explain your design”
● The algorithms interview:
	○ “Here is a problem that has many algorithms with different complexities. Find the best one
	and implement it”
● The domain-knowledge interview:
	○ “Here is a problem from our industry, explain how your would solve it under these
	constraints”

NOTE:  **Get a good night of sleep & eat properly**


**Check in:** Arrive 15 minutes early and check in for your interview. Have your government-issued photo ID ready (for example, your driver’s license or passport).


**What to expect:** Interviews will be a mixture of questions and discussions about your experience. Be ready with detailed examples. Concise, structured answers are best.


All interviewers will assess your potential for growth beyond the position you’re interviewing for. They’ll evaluate how well your background and skills meet core competencies, along with how they relate to our Leadership Principles. We recommend approaching each interviewer the same way, rather than tailoring answers to their role


You should also know some of the languages’ nuances, such as how memory management works, or the most commonly used collections, libraries, etc.

They’ll be looking for your ability to apply what you know to solve problems efficiently and effectively

Most of the work we do involves storing and providing access to data in efficient ways. This requires a strong background in data structures.

You’ll need to understand the inner workings of common data structures and be able to compare and contrast their usage in various applications. You’ll be expected to know the runtimes for common operations as well as how they use memory.


Your interview will not be focused on rote memorization of algorithms. However, having a good understanding of the most common algorithms will likely make solving some of the questions a lot easier.

Consider reviewing common algorithms such as traversals, divide and conquer, breadth-first search vs. depth-first search and understand the trade-offs for each.

Knowing the runtimes, theoretical limitations, and basic implementation strategies of different classes of algorithms is more important than memorizing the specific details of any given algorithm.

Expect to be asked to write syntactically correct code—no pseudo code

The most important thing an SDE does at Amazon is write scalable, robust, and well-tested code. These are the main evaluation criteria for your code. Make sure that you check for edge cases and validate that no bad input can slip through. This is your chance to show off your coding ability

Object-oriented design

Good design is paramount to extensible, bug-free, long-lived code. We know it’s possible to solve any given software problem in almost limitless ways, but when software needs to be extensible and maintainable, good software design is critical to success.

One way to build lasting software is to use object-oriented design best practices. You should have a working knowledge of a few common and useful design patterns, along with how to write software in an object-oriented way.

You likely won’t be asked to describe the details of how specific design patterns work, but expect to have to defend your design choices.

Databases

Most of the software that we write is backed by a data store. Many of the challenges tech people face arise when figuring out how to most efficiently retrieve and store data for future use.

Amazon has been at the forefront of the non-relational DB movement. We have made Amazon Web Services such as DynamoDB available to the developer community so that they can easily leverage the benefits of non-relational databases.

While we don’t expect any particular level of expertise with non-relational databases, you should be familiar with broad database concepts and their applications. The more you know about trade-offs between relational and non-relational databases, the better prepared you’ll be.

Distributed computing

Systems at Amazon have to work under very strict tolerances at a high load. While we have some internal tools that help us with scaling, it’s important to have an understanding of a few basic distributed computing concepts.

Understanding topics such as service-oriented architectures, map-reduce, distributed caching, load balancing, and others, will help you formulate answers to some of the more complicated distributed architecture questions you might encounter.

Operating systems

You won’t need to know how to build your own operating system from scratch, but you should be familiar with some OS topics that can affect code performance (e.g. memory management, processes, threads, synchronization, paging, and multithreading).

Internet topics

We expect our engineers to be familiar with the fundamentals of how the internet works. Brush up on how browsers function at a high level, from DNS lookups and TCP/IP, to socket connections.

Having a solid understanding of the fundamentals of how the worldwide web works is a requirement.

General machine learning and artificial intelligence

Expect to be asked about data-driven modeling, train/test protocols, error analysis, and statistical significance.

For example, given a problem definition, you should be able to formulate it as a machine learning problem and propose a solution, including ideas for data sources, annotation, modeling approaches, and potential pitfalls. Understand the basic AI/ML methods and algorithms. Revisit your favorite ML and AI textbooks.

## How to practice

**● Leetcode.com**
Blind75 -> Neetcode150 -> Grind169 -> seanprasad

● Conduct lots of mock interviews!

[ primeagen fast-typing interviewing ]

[  ] 1point3acre + amazon tagged Leetcode premium questions + leadership principle and stuff every weekend

[   ] practice interviews with discord communities and pramp seriously. Use notebook, coderpad and whiteboard simultaneously -- be comfortable enough to play around and confident enough to nail most things

[   ]  Do the 6 Hour & 24 Hour Grind 169 + Neetcode 150 Leetcode practice and revise completely
### Do Coding Interview Questions While You're Learning

Keep doing problems while you're learning all this stuff, not after.
You're not being hired for knowledge, but how you apply the knowledge.

Why you need to practice doing programming problems:
- Problem recognition, and where the right data structures and algorithms fit in
- Gathering requirements for the problem
- Talking your way through the problem like you will in the interview
- Coding on a whiteboard or paper, not a computer
- Coming up with time and space complexity for your solutions (see Big-O below)
- Testing your solutions

### Rubber ducky method
○ Vocalize, vocalize, vocalize!

- choose a topic, learn patterns and solutions
- choose another list, solve problems on that topic until you're good at it
- time it, share your thought process, walk the code, test it at the end, differentiate different approaches, get more time to think, simplify the question and ask for hints or ideas 
- Do lots of Contests


I created an excel sheet that had three columns: problem name, explanation of my approach in words and explanation of the optimal solution in words. I also stopped trying to do as many problems as possible and took more time to review each problem. Some days I would spend more time reviewing the problem than I spent doing it.

The number of problems you solve is less important than your ability to recall solutions during the interview. Regular revision will help reinforce strategies and maintain a sense of calm.

But seriously having a notebook to write down important templates and patterns. And writing down problems I find extremely interesting and have similar patterns and application elsewhere

Not being ashamed of memorizing classic patterns and structures.

Leetcode type interviews are not like real world problems, so we should not waste time thinking or talking how we would solve that IRL, unless the interviewer ask.

Focus on deeply understanding questions rather than trying to solve as many as possible

Consistency. It needs to be an everyday thing. Like going to the gym.

My off days I'll do 2 problems (heavy work day, some sundays). My on days I'll do 5+.


Leetcode 30 minutes every day. Only 30 but every day, no excuses (birthday, Christmas, tired - doesn't matter). Low effort, long time. It worked though - a year later I could crack any medium with ease.

You should probably get in the habit of solving and writing code at the same time. Spending 10 min explaining an algo is an absolute waste of time, just give a high level vibe of what you're going for and start writing. Same with the brute force soln, just say "oh we can do XYZ but I presume we want a better runtime than that".

Agree on this. Having done the loop at Meta and Google I spent so much more time explaining the first time around and they do not give a shit beyond:

- state the approach (30s)
    
- catch issues with approach and revise (2 min)
    
- state expected big O for time and memory (1min)
    
- code two test cases (1min)
    
- code the algo (10min)
    
- walk through test case (3min) And repeat.
    
Use a time to gauge yourself


# Advice for Onsite Interviews:

1. **Understand the Problem**: Read through the question carefully and ask clarifying questions to ensure you fully grasp the requirements. Do not jump straight into coding this will be an automatic fail even if you correctly solve the problem.
    
2. **Communicate Effectively**: Clearly explain your thought process as you work through the problem. Be prepared to answer follow-up questions from the interviewer.
    
3. **Time and Space Complexity**: Always consider and explain the time and space complexity of your solutions.
    
4. **Persevere Through Challenges**: It’s not necessary to excel at all technical questions to pass the interview. In my case, I performed very well on the first two questions but struggled with the last one. However, after receiving hints from my interviewer, I was able to develop a solution.
    

In summary, preparation, clear communication, and the ability to adapt to challenges were key to my success.


First pass, look at 100-200 questions and their solutions (dont bother with the 15 min rule) basically I found that the 15 mins were a waste because I sucked so hard

Second pass use your strategy, basically try for 15 mins to remember the solution if you can and then try and regurgitate it and understand why it works

Third pass, work on understanding the answers and work on adding wrinkles and seeing if you can see the patterns

Takes longer but works to build in the patterns all at once, also gives you a better feeling at the start since you probably would be beating yourself up for not knowing the answers in 15 mins

I really had to learn how I learn cause the old college exam strategy of cramming a week before did not work for the interviews cause the question bank and subject material was way too big.

Started off by reading relevant sections of CLRS to build a solid foundation of knowledge (I recommend Skienna’s Algorithm Design Manual these days as CLRS is a bit too academic with proofs for everything. Algorithm Design Manual is far more practical).

After that I started solving a bunch of Leetcode problems, maybe about 150, till I found myself solving most unseen mediums in under 20 mins. I always timed myself solving them and considered it a failure if I took longer than 20 mins to solve a problem (Meta’s standard). This worked and I eventually landed an L4 SDE role with Amazon.

Also, because of the solid foundation, I can usually prepare for interviews in a month or 2 of prep. Unfortunately, the actual work experience doesn’t maintain these skills, what a shocker…

Sure, everything before the lookup reference part of the book. Interview/ Leetcode questions can come from any of those sections.

The second part is supposed to be just a lookup guide to see if the problem you’re solving matches one of those in the book. 99.9% of algorithm problems are covered by that reference but it’s not necessary to read it.

Hey, Googler here who used to suck at leetcode and then got 9+ offers in my career including Snap, Amazon, top startups, etc. And I only did ~100 LC questions. Here are the key takeaways:

I can't stress enough how important it is for you to struggle and attempt to solve it on your own REALLY HARD before checking the solution. No, it is not a waste of time to spend more than 30mins on each problem. You will learn the most from being stuck, struggling, and then things clicking. I will go as far as to say, _a lot of advice you see on these subs are awful;_ the blind are leading the blind.

**Set your mindset to this**: the goal is to learn how to **problem solve**. _Memorizing solutions is not problem solving_. Problem solving when stuck is the signal what good interviewers look for. This is how I got into Google without solving every problem optimally.

I would set the hard cut-off to check the answer at 1hour. At 15min and 30mins, check one hint at a time on leetcode. If there's no hint, check the tagged topics (linked list, graph, etc) which is often a huge hint by itself. DON'T GIVE UP SO EASILY.

This is why I only did 100 LC. It took a lot of time to solve each one. The difference is that _I actually solved them myself;_ therefore, I learned first hand how to think from scratch to the optimal solution.

Not to say either of you is wrong, but rather to shine light on the fact that everyone has different learning styles.

For me, personally, found live-streaming my learning highly useful. Pretending having to explain my process to non-existent viewers served as a sort of rubber ducky. After 5-15 minutes, I’d study the solution, explain it in simple terms to my “viewers”, rinse wash and repeat.

Honestly, I would still do what the top comment said, just look and see the solutions of the first 200, learn patterns, learn built in tricks, then continue with this Google guy approach and bang my head against the desk for 1hr straight until I solve the problem. It is probably smt you ve seen already before, so the solution and the pattern is probably some there hidden inside your brain

My approach is:

- Neetcode 150, first round. Clear Anki list every 50 problems. (Second round)
    
- Solve daily problems from Anki list once finished the neetcode 150, this is my leetcode base.
    
- Do fundamentals and learn the 20-30 top SD designs
    
- Do LLD, OOP or whatever is need
    
- Prepare behaviourals
    
- Do leetcodes focused to companies

This is what worked for me, it might not work for other people. I focused on leetcode interview top 150 and grind 75. First I only did easies, then I did mediums. I prepped over a few different disjointed spurts before I started interviewing. I didn't look up solutions. I tried to solve every problem on my own. Sometimes I would spend 2 hours on a problem, not come up with anything, get sick of it and forget about it, maybe coming back weeks later.

In total, I solved something like 120 to 130 on my own. When I started getting interviews, I ramped up and did two things differently: (1) I started looking at solutions if I couldn't solve a new problem within an hour and (2) I re-did problems I'd done before. Again, if I couldn't remember or find the solution within an hour, I'd look at my old solution. Including ones for which I gave up and looked at the solution, I completed about 160 problems total. This got me good enough to pass technical rounds with multiple companies including FAANG.

There are some important caveats: (1) I studied very hard in university. I took honours discrete math II and DSA II. I feel those classes helped me a lot. Especially in DSA II, we went over things like dynamic programming, linear programming and a lot of graph algorithms. I also took number theory as an elective, which is helpful for some problems. (2) Before passing interviews, I bombed a couple. I bombed some OAs and also a couple live interviews. I feel that this helped me manage my stress in live situations.

I don't feel like I had a systematic way of breaking down problems or classes of problems, I didn't explicitly write out patterns or anything. I guess by just forcing myself to solve problems on my own and by redoing problems, I started to internalise the patterns and recognise them in new problems I hadn't seen before.

tl;dr: I studied very hard in school and took all the algorithm and algorithm-adjacent classes I could. I did ~130 leetcode easies and mediums (and a couple of hards) from interview top 150 and grind 75 without looking up solutions. To grind interview prep I re-did problems to commit them to memory and looked at solutions when I got stuck. I shat the bed in a few interviews, but then got better at it and started passing them.

This is what I do at the moment but I’m not sure if this is optimal, I guess not because I don’t learn much.

1. 15 minutes to think of the solution, (just drawing out everything etc)
    
2. 5 minutes to code the solution
    
3. If I don’t get it, I ask an AI to show me what’s wrong with my current approach and then I ask it for the optimal solution and make sure I understand.
    

That’s it really, but I still don’t seem to learn at times when I come across new questions it just seems hard again.


Recognizing the type of problem and an approach that could work is the way, because otherwise getting to the approach is going to eat your whole interview.

Throughout the week, I tackle 1-2 new medium-level problems daily. On Saturdays, I review all the problems I worked on by reading each problem statement, recalling my approach, and comparing it to my submitted solution on LeetCode. This process focuses on visual memorization and rehearsing explanations, as if presenting to an interviewer, which has significantly improved my recall of strategies.

I also bookmark(screenshot) tricky problems on LeetCode. On the day of an interview, I review only my top bookmarked questions for quick reference. I avoid solving new problems on the interview day, using that time instead to relax and mentally prepare.



Phone Screen

Before starting my preparation, I was familiar with basic algorithms like DFS, BFS, and Topological Sort. While I understood how these algorithms worked, implementing them took me some time. Additionally, I was unfamiliar with over 50% of the Grind169 list. But I would say I was fairly confident on basics of DSA. 

- **How to get solution in algomonster ?** All solutions are free and searchable through google. However, to navigate quickly [https://algo.monster/liteproblems/{problem_number}](https://algo.monster/liteproblems/{problem_number}) replace the {problem_number} in url with the actual number on leetcode.
    
- I focused primarily on medium-level LeetCode problems, skipping many easy and all hard ones, to target those most likely to appear in interviews.
    
- By the time of the phone screen, I had reviewed the questions 3–4 times, focusing heavily on medium problems.

**Implementation Practice**:

- While I skipped some detailed implementations, I practiced key algorithms like DFS and BFS for graphs and trees.
    
- To save time troubleshooting bugs or missing test cases, I copied code into ChatGPT to identify errors and suggest fixes. This was particularly useful when my code was mostly correct but missed specific conditions.
    

**Challenges**:

- Although I was confident in brute force solutions, my implementations were often slow or buggy.
    
- In interviews, I sometimes froze when test cases failed, highlighting the need for more implementation practice under pressure.


**Interview Breakdown**  
Onsite interviews typically involve 30–40 minutes of solving problems, dry runs, follow-ups, and managing pressure. My goal was to implement common algorithms within 10–20 minutes—an initially unrealistic target.

**Implementation**

- Familiar with most Grind169 solutions, I focused on improving implementation efficiency.
    
- Adopted templates from AlgoMonster, identifying patterns for faster problem-solving.
    
- Reviewed Neetcode150 list for additional practice despite overlapping content.

**Spaced Repetition**

- Re-implemented questions to reinforce concepts, focusing on questions I hadn’t solved before.
    
- For questions I was confident about, I reviewed only solutions instead of re-implementing.
    
- Although I didn't complete all of Grind169, I implemented many problems and revised them by topic.
    
- Did few Leetcode Hard problems by attempting solutions independently, most of the time would view the solution along with the implementation details and then implement it myself. 
    

**Key Takeaways**

- Don’t memorize solutions—Google often asks unique problems. Focus on understanding the core type of problem. 
    
- With practice you learn the implementation of all the basic algorithms and this will help you think in pressure situation. 
    
- Practice builds retention and confidence.

   **Approach**:

- Watched videos at 2x speed to save time.
    
- Focused on optimized solutions instead of brute force after first few videos
    
- Learned to use templates, which helped generalize solutions across similar problems.
**Algomonster Templates**  
Link : [https://algo.monster/templates](https://algo.monster/templates)

- Understand templates throughly for common problem types (e.g., Two Pointers, Graphs).
    
- Create your own template if you like.
    
- In interviews, you just have to focus on the specific of the problem as you already know the template of most common algorithm
    
- Templates also helped me explain my approach clearly, as I knew the structure well.

# During the Interview

**Thinking Out Loud**

- I had this habbit of explaining the purpose of each variable in code.
    
- Walk the interviewer through my approach step-by-step (eg. which test case would a given `if` condition would eliminate) to showcase my thought process.
    

**Importance of Dry Runs**

- Interviews often don’t involve running code on a system instead we need to do a dry run. 
    
- If the code has an error, interviewer may provide a test case for manual evaluation.
    
- Take a small test case for dry run. (It is challenging when we have graph/trees/recursive)
    
- Take positive as well as negative test case
    
- While practising know some trivial test case like for graph/tree "no node", for array "empty list" , etc.
    

**How to Dry Run Effectively**

- Write a test case as a comment.
    
- Copy the code below the test case and step through it, explaining variable values and logic.
    
- In comments specify the value of the variable if you think it is important for that test case. 
    
- This method helps spot issues and aids the interviewer in taking notes.
    
- For next case again copy the code above and redo all the steps

# LLD Interview (Amazon)

**Link**: [https://leetcode.com/discuss/interview-question?currentPage=1&orderBy=most_votes&query=OOD&tag=amazon](https://leetcode.com/discuss/interview-question?currentPage=1&orderBy=most_votes&query=OOD&tag=amazon)

**General Tips:**

- Many LLD problems can be approached as LRU or LFU cache challenges.
    
- Use a hashmap to store node references for efficient lookup (useful for the add method).
    
- Use a doubly linked list to remove nodes in O(1) time (useful for the remove method); treat it like a queue.
    

**Approach:**

1. Identify the essential classes first, without focusing on parameters.
    
2. Add additional classes as needed to implement design patterns.
    
3. Define constructors and method parameters while explaining the code.
    
4. Use abstract classes or interfaces for creating hierarchies and subtypes.
    
5. Strive for modular, maintainable code.
    

**Tips:**

- Review solutions in the LeetCode discussion section for ideas.
    
- Use ChatGPT to generate a skeleton, but don’t rely on it for full LLD design (it’s not ideal for comprehensive solutions).
    

**Commonly Used Design Patterns:**

1. Strategy Design Pattern
    
2. Factory Design Pattern
    

**Other Useful Design Patterns:**

1. Observer Design Pattern
    
2. Singleton Design Pattern
    

**Common Interview Questions:** (Note: Most solutions available online are comprehensive, but interviews typically ask simpler version of it)

- Design a Package Delivery System
    
- Design a Hotel Booking System
    
- Design a Parking Lot
    
- Design GoodReads
    
- Implement the Linux find Command
    
- Design a Chess Game
    

# Behavioural Interviews

**STAR method , basics of behavioural interview**  
**Link :** [https://www.techinterviewhandbook.org/behavioral-interview/](https://www.techinterviewhandbook.org/behavioral-interview/)  

- Reviewed past experiences to cover all leadership principles for behavioural questions.
    
- Important to be thoroughly familiar with your experiences for detailed answers(Amazon had many followups).
    
- 5-6 strong examples covering all the leadership principal are sufficient.
    
- Prepare for negative situations as well (e.g., describe a time you missed a deadline).
# Post-Interview process

[   ] Questions to ask the interviewer

- Name, job title, maybe email (for reference later on)
- What made you choose company X?
- What’s the most satisfying project you’ve worked on?
- What’s a typical day for an intern like?
- Any example projects interns have worked on?
- What’s your favorite thing about working for your company?
- How does this company compare to other places you’ve worked before?

Here are some examples of behavioral-based questions:

1. Tell me about a time when you were faced with a problem that had a number of possible solutions. What was the problem and how did you determine the course of action? What was the outcome?

2. When did you take a risk, make a mistake, or fail? How did you respond, and how did you grow?

3. Describe a time you took the lead on a project.

4. What did you do when you needed to motivate a group of people or promote collaboration on a project?

5. How have you used data to develop a strategy?

When you respond, be sure to focus on the question asked. Ensure your answer is well-structured and provide examples using metrics or data if applicable. Reference recent situations whenever possible.

The STAR method is a structured manner of responding to a behavioral-based interview question. Here’s what it looks like:

**SITUATION**

Describe the situation you were in, or the task you needed to do. Give enough detail for the interviewer to understand the complexities of the situation. This example can be from a previous job, school project, volunteer activity, or other relevant event.

**TASK**

Describe your goal.

**ACTION**

Describe the actions you took. Use an appropriate amount of detail. What steps did you take? What was your contribution? Let us know what you did, not what your team or group did. Use the word ‘I,’ not ‘we.’

**RESULT**

Describe the outcome of your actions. Don’t be shy about taking credit for what you did. What happened? How did it end? What did you accomplish? What did you learn? Provide examples using metrics or data if applicable.

Consider your successes and failures in relation to the Leadership Principles. Use examples that showcase your expertise and how you’ve taken risks, succeeded, failed, and grown. Keep in mind that some of our most successful programs have risen from the ashes of failed projects. Failure is a necessary part of innovation. We believe in failing early and persevering until we get it right.

- Practice using the STAR method. Frame your examples in relation to the Leadership Principles.
- Ensure each answer has a beginning, middle, and end. Describe the situation or problem, the actions you took, and the outcome.
- Prepare short descriptions of a handful of situations. Be ready to answer follow-up questions in greater detail. Select examples that highlight your unique skills.
- Have examples that showcase your experience and how you’ve taken risks, succeeded, failed, and grown.
- Specifics are key. Avoid generalizations. Give a detailed account of one situation for each question you answer. Use data or metrics to support your example.
- Be forthcoming. Don’t embellish or omit parts of the story.

- Be prepared to explain what interests you about the role and the team (or teams) you’ll be meeting with.
- Be concise but detailed in your answers. We know it’s hard to gauge how much info is too much versus not enough. A good test is to pause after your answer to ask if you’ve given enough detail or if the interviewer would like you to go into more depth.
- If you’re asked a question but aren’t given enough info to provide a solid answer, don’t be shy about asking for clarification. If additional context isn’t available, focus on how you’d attempt to solve the problem based on limited information.

- We aim to hire smart, thoughtful, customer-obsessed people. “Why Amazon?” is a common question. We want to understand what inspired you to explore an opportunity with us, so we can get a better sense of who you are.
- We try to leave a few minutes at the end of each interview to answer your questions. If we don’t get to all of them, don’t hesitate to ask your recruiting point of contact.

**You must incorporate the principles into your responses because your responses are evaluated and you are rated based on how well you performed according to the leadership principles.**


Answers to behavioral questions should be between 2 and 4 minutes

- know the leadership principles and have stories about yourself that demonstrate you embody these principles
- showcase your accomplishments
- Help the interviewer see how great you have been and will be.

[   ] After the interview
- Thank them for their time!!
- (If you didn’t bomb it) and didn’t hear back in 1 weeks, consider following up
with the recruiter / interviewer!



--------------------------------------------------------------------------

TLE CP-31 Sheet
- Our entire CP training is divided into 4 Levels (or courses).
- Each level is a 12-14 weeks program consisting of 2-3 live classes every week.
- Each level comes with 100+ curated practice problems. We provide 2-3 curated practice problems daily from Monday to Friday based on the week's topics. Each practice problem comes with dedicated hints and a video solution.

How often are classes held each week?

- 2-3 classes per week in each level.

What are the timings of live lectures?

- Most of the classes are held on weekend in one of the two slots: 2-4 pm or 6-8 pm IST
- Some of the classes are held on weekdays at 8-10pm IST

What is the total number of problems in a course level?

- We provide a total of 100+ curated practice problems in each course level. Every day from Monday to Friday you will be provided with 2-3 curated practice problems.
- Along with this you get 3-4 bonus problems every week to challenge you further.

Which platform are the practice problems picked from?

- We pick up the most relevant problems for every topic, the platform is not really important.
- Most problems are picked from Codeforces, while some are picked from CSES problemset, Atcoder, and Leetcode.

What if I am not able to solve a practice problem?

- Read the problem and try to think of a solution for 40-60 minutes.
- Couldn't solve? Look at the 1st hint, think again for 15 minutes.
- Couldn't solve? Look at the 2nd hint, think again for 15 minutes.
- Still couldn't solve? Watch the dedicated video solution.
- Still couldn't solve? See the solution

["The Algorithm Design Manual”](https://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202), which is officially recommended by Google for interview preparation.

● Cracking the Coding Interview
	○ This book is amazing, seriously
● Being a TA
	○ This is literally your job 

10AM-1PM

EXAM: *FREE* Interview Prep Resources : r/leetcode
https://www.reddit.com/r/leetcode/comments/1eomu9y/free_interview_prep_resources/


Learn Amazon specific questions, do tons of self mock interview coding, seanprasad + grind 169 + neetcode 150 + blind75 list for 6 hours everyday 

TLE Eliminators every morning + Primeagen Algo course every evening.  Do the algo design book+ lectures in the morning ++ csefi book x cp book 1&2 problems in the evening ++  clrs book in the evening 


1point3acre + amazon tagged Leetcode premium questions + leadership principle and stuff every weekend

pratice interviews with discord communities and pramp seriously. Use notebook, coderpad and whiteboard simultaneously

Watch NeetcodeIO streams.


- [Grokking the Coding Interview](https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/solution-contains-duplicate) was particularly helpful for one of the questions I encountered.
    
- [LeetCode’s Data Structure Crash Course](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/) provided the foundation for solving two of the technical questions.
    
- I also subscribed to **LeetCode Premium** to access additional problems for targeted practice.
    
- The most valuable resource, in my opinion, was [NeetCode](https://neetcode.io/), which helped me refine my skills and strategies.


CTCI too


**NeetCode Youtube Channel**

**Link :** [https://www.youtube.com/@NeetCode](https://www.youtube.com/@NeetCode)

Sort IP_EVERYDAY + OBSIDIAN and come up with the best roadmap + update in Linear & push the cpxip folder in WSL to github

Go through books like CLRS & Algorithm Design by Éva Tardos.




Learn C++, DSA from CMU & Cornell & any other op UNIs, Read Competitive-Programming books and practice problemsets offline

Learning from First Interview: Practice Contests and do as many mock interviews as you can


This is your new *vault*.

Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

When you're ready, delete this note and make the vault your own.

12 Week program to set strong fundamentals drilled into your head


    Don't go to the editorial after some fixed time like 20 minutes of solving a problem. Give up only if you are stuck for 10-30 minutes (10 in case of easy problems, more for harder ones). As long as you have some ideas, do investigate them and maybe you'll solve the problem yourself.
    Upsolving problems is very important. This way you learn new things. After a contest or virtual participation, try to solve at least one more problem. This should be said early in the PDF, not only in parts about getting red rating.
    I don't think you should copy segment trees from your code library (reference document). It's better to struggle for some time and implement them every time. You will get faster and will understand them better. Plus this is a must for those who prepare for IOI. My friends and I implement seg-trees from scratch every time. I don't remember if I ever used to copy them.
    It's unnecessary to do "50+ virtual participations in CF". Just solve problems slightly above your level. Do some virtual participations if you want to.
    Consider changing "Make a routine that you will do just before the contest. It directly leads to the concentration during the contest." to "don't care about the contest, just have fun solving problems". I'm quite sure people perform better when they are relaxed (but not distracted).
    "Although I experienced competitive programming for 3 years, I think that I don’t know many techniques" — I think that's because you're doing too much virtual participation. You spend a lot of time on easy problems this way.

So, on average, I trains approximately 25-30 hours per week.

### Image 1: LeetcodeKnight-Roadmap

**Subtasks:**

- Blind75, Neetcode 150, Neetcode 250, Grind169 & SeanPrasad174 and other PSETs curated for interviews.
- Consume and Prepare for Mock Interviews: Take lots and lots of practice until it becomes second nature, and there’s no chance for you to mess up even if you want to.
- Learn how to properly grind Leetcode: Take advice from YouTube and solve problems on your own.
- Do Leetcode premium problems, Leaked Company Tagged Questions, and contests from 1point3acres, LeetCareer, and other Chinese websites.
- Watch all videos from Aditya Verma, Back to Back SWE, and Striver’s A2Z DSA Sheet.
- Practice Leetcode and Codeforces through bookmarks + obsidian roadmap + TLE Eliminators: Participate in contests and give lots of mock interviews both IRL and remote.
- Visualize, sketch out what happens, explain your thought process, dry run the code, and do unit tests with examples; draw out how the code will work.
    - Clarifying questions
    - Brainstorm data structures before coding
    - Think of the brute force solution first
    - State that you know this is too long/inefficient and why, then improve upon it
    - You can ask for hints if absolutely stuck!
- Work hard. Take every shortcoming as a learning experience. Doing badly in a contest means you didn’t know how to do something, and you have a wealth of time after contests to learn the techniques that eluded you.
- At 1650, there are still a lot of topics you don’t understand well. Go through the LC tags and work through the ideas you don’t think you know well. Also, do as many contests as you can and review gaps in your knowledge after.
- For the second part, practice comes from a lot of problem-solving: Learning how not to overthink, not knowing how and when to apply these techniques is earned.
- Think just doing more problems will help. Everything takes time. A lot of it has to do with doing so many problems that you start memorizing different tricks/patterns.
- Make sure you know the time/space complexities (big O notation) of each operation and what can be done on each data structure. Make sure you understand why it takes that much time/space rather than memorizing them. This is the whole point of learning data structures.

---

### Image 2: Continued Subtasks

- Practice and practice until you are comfortable finishing medium questions in 25 minutes and hard questions in 45 minutes, on average. Knowing and understanding how to solve is important, but being able to implement it fast is also critical in a timed interview environment (not so much in real life though). This is one of the many aspects why the current interview process is so controversial.
- Problem recognition, and where the right data structures and algorithms fit in:
    - Gathering requirements for the problem
    - Talking your way through the problem like you will in the interview
    - Coding on a whiteboard or paper, not a computer
    - Coming up with time and space complexity for your solutions (see Big-O below)
    - Testing your solutions
- There is a great intro for methodical, communicative problem-solving in an interview. Write code on a whiteboard or paper, not a computer. Test with some sample inputs. Then type it and test it out on a computer.
- Hard work > Talent
- Every hour you spend will be getting you closer to your goal division. Instead of being spent trying different strategies and reinventing the wheel, if you can’t solve a problem on your own, reading the solution and implementing it will not lead to much improvement. To get the most out of every problem, you need to figure out how you should have approached the problem to get to the next step of the solution on your own because this knowledge will be helpful for solving a brand new problem in a contest.
- Reasonable advancement times:
    - Bronze → ~1-3 months
    - Silver → ~1-3 months
    - Gold/Gold → ~1-3 months → Platinum/Platinum → ~5-6 months (but depends on what grade you are in)
    - Camp: The large range of time (1-3 months) comes from how much time a student dedicates to USACO. During summer, it should take 1-2 months, while during the school year, it may take up to 3 months. Any USACO Silver contestant preparing the right way should be ready to make this advancement.
- Be efficient with your time: Every hour you spend will be getting you closer to your goal division, instead of being spent trying different strategies and reinventing the wheel.

---

### Image 3: Final Steps

- Instead, the recommended approach is to learn each topic individually, followed by practicing with a curated list of problems (e.g., the USACO Guide or Codeforces) that require that concept.
- Practice, practice, practice: You should practice several hours per week on online judges | Weekly problem set | Daily contests.
- Take on the pressure of daily contests, along with six lectures | attending four lectures and two contests.
- Blind Practice Phase: Once you’re comfortable with the theoretical aspects, shift to blind practice. This phase helps you apply your knowledge in diverse situations, enhancing your adaptability and problem-solving speed.
- Targeted Practice Phase: As you approach mastery of your current division, identify areas that still pose challenges. Use targeted practice to focus on these topics, refining your skills and eliminating weaknesses.
- Blind practice is about solving problems without prior hints or knowledge of the underlying concepts they test. It mimics the unpredictability of actual competitions, where you don’t know what type of problem you’ll encounter.
- Learning Phase: Begin with acquiring the necessary knowledge base. This includes algorithms, data structures, and techniques pertinent to your division level. Utilize resources like textbooks, online courses, and tutorials to build a solid foundation. The USACO guide is a great resource for learning all things necessary for a particular division.
- Do Virtual Contests.
- Starting with Educational Rounds: For beginners and those looking to solidify their foundational knowledge, the “Educational” rounds on Codeforces are an excellent choice. These rounds focus on fundamental algorithms and problem-solving skills, offering a comprehensive practice experience. With over 150 educational rounds available, they provide a vast resource for consistent learning and practice.
- Progressing to Division Contests: Once you’ve navigated through the educational rounds, or if you’re looking for more diverse challenges, consider participating in Division 1 or Division 2 contests. Your choice should align with your Codeforces rating and your USACO division. Generally, Division 2 contests are suitable for most competitors, but if you are in the USACO Platinum division, venturing into Division 1 contests can offer the advanced challenges you might be seeking.
- While they are rich in content, spending excessive time on them can divert attention from actual problem-solving practice.

Fee includes: training, lectures, meals and accommodation, as well as the leisure and entertainment.

This edition will include lectures from Monday to Saturday

Our basic schedule will have theory classes in the mornings and contests in the afternoons. Each instructor will select classes and contest contents.

After you get basics done, I would say doing the CodeForces weekly contests is big. Reading editorials from past ones is also insanely rewarding.

And for problems, look at the lists on the bottom of this page, probably what helped me improve most: https://acm.timus.ru/problemset.aspx?locale=en

Once you get cracked enough, there is the (legendary) Petrozavodsk training camp (but lowkey codeforces is on the same level imo) - https://acm.timus.ru/problemset.aspx?space=1&tag=ptz
---
