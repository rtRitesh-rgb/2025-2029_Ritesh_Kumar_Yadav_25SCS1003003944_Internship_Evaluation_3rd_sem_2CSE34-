"""
Test script for financial_chatbot.py

Runs a batch of sample queries through simple_chatbot() and prints the
question/answer pairs so results can be reviewed or saved as evidence
of testing (Step 4 of the task).
"""

from financial_chatbot import simple_chatbot

TEST_QUERIES = [
    # Query type 1: total revenue
    "What is Microsoft's total revenue in 2025?",
    "What is Apple's total revenue?",  # no year -> defaults to 2025

    # Query type 2: net income change
    "How has Tesla's net income changed over the last year?",
    "How has Microsoft's net income changed in 2025?",

    # Query type 3: total assets
    "What are Apple's total assets in 2023?",

    # Query type 4: total liabilities
    "What are Tesla's total liabilities in 2024?",

    # Query type 5: cash flow from operations
    "What was Apple's cash flow from operations in 2024?",

    # Missing company (should ask for clarification)
    "What is the total revenue?",

    # Completely unrelated / unknown query (should trigger fallback)
    "What is the weather today?",
    "Tell me a joke.",
]

if __name__ == "__main__":
    print("Running chatbot test queries...\n")
    for i, q in enumerate(TEST_QUERIES, start=1):
        answer = simple_chatbot(q)
        print(f"Test {i}")
        print(f"  Query:    {q}")
        print(f"  Response: {answer}\n")
