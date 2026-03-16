# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- 1. The history would not be cleared even user start a new game, and the game cannot submit guess when start a new game whether the user won last time
- 2. The hint is opponent. If user input a number higher than the secret number, the hint would say go higher; if user input a number lower than the secret number, the hint would say go lower.
- 3. The range should be 1 to 100, however, numbers out of this range are also be accepted.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- The AI sugguest that the user cannot restart game is because the status is not set back to playing when initial the new game. I reviewed the code and found it is true. Then I used AI's suggestioned code and run the APP, the bug is fixed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- The AI suggeste the raw guess is compared with secret value as text, however, it is parsed to int. 


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Check if it passed the testcases, and run APP to test it by myself.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- I run the pytest and it shows 100% passes. It showed me that the bug I found has been fixed.
- Did AI help you design or understand any tests? How?
- Yes, it helped me to write the testcases about issues that I want to check.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- Everytime the user starts a new game, the previous records including the secret number will be updated.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- The Streamlit will rerun the entire python script again whenever user interacts with the APP, the variables will be reset because the script resuns everytime. But session state can remember variables between different reruns.
- What change did you make that finally gave the game a stable secret number?
- I changed secret number range from 1-100 to variable low-high, so it fits different difficulty
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  -I get a environment issue about the streamlit, giving the context and asking AI to fix it is useful. I want to reuse it in future projects?
- What is one thing you would do differently next time you work with AI on a coding task?
- I may use prompt to limit AI's answer length, sometimes it is too long to read and waste tokens.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- The AI code with contexts makes it easy to debug, it is much faster than do it by myself. AI can understand each variables and how it works, it makes it possible to fix bug quickly. But it has some issues when I asked AI to generate new code like write pytest. I got a bug of the testcase and I found the issue by myself, then ask AI to fix it. It looks like if human found the bug, AI can fix it quickly, however, it cannot easily found bugs that write by itself.
