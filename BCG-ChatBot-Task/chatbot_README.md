# Financial Chatbot Prototype — Documentation

## Overview
This is a simple, rule-based chatbot prototype built for the BCG GenAI Consulting job
simulation (Task 2). It answers predefined questions about the financial data of
**Microsoft, Apple, and Tesla** for **FY2023–FY2025**, using the figures extracted
and analyzed from each company's 10-K filings in Task 1.

The chatbot does **not** use machine learning, NLP, or any external API. It relies on
simple `if-elif-else` keyword matching in Python, as specified by the task instructions.

## Files included
- `financial_chatbot.py` — the chatbot script (data + logic + interactive `input()` loop)
- `test_chatbot.py` — a script that runs a batch of sample queries automatically
- `test_results.txt` — captured output from running `test_chatbot.py`
- `README.md` — this documentation

## How it works
1. The analyzed financial data (revenue, net income, total assets, total liabilities,
   and cash flow from operations for each company/year) is stored in a Python
   dictionary called `DATA`.
2. When a user types a question, the `simple_chatbot()` function:
   - Converts the text to lowercase and checks it for keywords (e.g., "revenue",
     "net income", "assets", "liabilities", "cash flow").
   - Looks for a company name ("microsoft", "apple", "tesla") and a year
     ("2023", "2024", "2025") mentioned in the question.
   - If a query type is matched, it looks up the relevant number(s) in `DATA` and
     returns a formatted sentence with the answer.
   - If a company isn't specified, it asks the user to clarify.
   - If the year isn't specified, it defaults to the most recent year (FY2025).
   - If nothing matches, it returns a fallback message explaining what it can help with.
3. `run_chat()` provides a command-line loop using `input()` so a user can type
   questions interactively and type `quit` or `exit` to stop.

## Supported (predefined) queries
The chatbot supports 5 categories of questions, for any of the three companies and
any of the three fiscal years (2023–2025):

| # | Query type | Example |
|---|---|---|
| 1 | Total revenue | "What is Microsoft's total revenue in 2025?" |
| 2 | Net income change vs. prior year | "How has Tesla's net income changed over the last year?" |
| 3 | Total assets | "What are Apple's total assets in 2023?" |
| 4 | Total liabilities | "What are Tesla's total liabilities in 2024?" |
| 5 | Cash flow from operating activities | "What was Apple's cash flow from operations in 2024?" |

If no year is mentioned, the chatbot defaults to FY2025. If no company is mentioned,
it asks the user to specify one rather than guessing.

## How to run it

**Requirements:** Python 3.7+ (no external libraries needed — only the standard library).

1. Make sure `financial_chatbot.py` and `test_chatbot.py` are in the same folder.
2. To chat interactively, run:
   ```
   python financial_chatbot.py
   ```
   Then type questions at the `You:` prompt, e.g.:
   ```
   You: What is Apple's total revenue in 2024?
   Bot: Apple's total revenue in FY2024 was $391,035M ($391.0B).
   ```
   Type `quit` or `exit` to end the session.

3. To run the automated test queries instead:
   ```
   python test_chatbot.py
   ```
   This prints 10 sample query/response pairs, including two unrecognized
   queries to demonstrate the fallback behavior.

## Sample test results
See `test_results.txt` for the full output. A few examples:
- **Q:** "What is Microsoft's total revenue in 2025?"
  **A:** "Microsoft's total revenue in FY2025 was $281,724M ($281.7B)."
- **Q:** "How has Tesla's net income changed over the last year?"
  **A:** "Tesla's net income decreased by 46.5% from $7,091M ($7.1B) in FY2024 to $3,794M ($3.8B) in FY2025."
- **Q:** "What is the weather today?" *(unrelated query)*
  **A:** "Sorry, I can only answer predefined questions about total revenue, net income
  change, total assets, total liabilities, or cash flow from operations for
  Microsoft, Apple, or Tesla (FY2023-FY2025)..."

## Limitations
- **No real natural language understanding** — the bot only matches keywords
  (e.g., "revenue", "assets"), so it can misinterpret unusual phrasing or typos.
- **Fixed dataset** — only supports Microsoft, Apple, and Tesla for FY2023–FY2025.
  It cannot look up any other company, year, or metric (e.g., it doesn't know
  stock price, EPS, or segment-level data).
- **No conversational memory** — each query is handled independently; the bot
  doesn't remember earlier questions in the same session (e.g., it can't handle
  "What about last year?" as a follow-up).
- **Simple ambiguity handling** — if a question mentions multiple companies or
  years, the bot may not pick the one the user intended.
- **Not production-ready** — this is a learning prototype meant to demonstrate
  rule-based logic, not a robust or scalable chatbot architecture. A real-world
  version would likely use NLP/LLM-based intent recognition and a proper
  database instead of a hardcoded dictionary.
