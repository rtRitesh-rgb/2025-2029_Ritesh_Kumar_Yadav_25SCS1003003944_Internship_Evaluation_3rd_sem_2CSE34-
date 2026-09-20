"""
Financial Chatbot Prototype
----------------------------
A simple, rule-based chatbot that answers predefined questions about the
financial data of Microsoft, Apple, and Tesla (FY2023-FY2025), based on
figures extracted from their 10-K filings in Task 1.

This is intentionally simple: it uses if-elif-else logic to match a small
set of predefined queries to canned responses built from the analyzed data.
It does NOT use any machine learning or natural language understanding.

Run this file directly to chat with the bot via the command line:
    python financial_chatbot.py
"""

# ---------------------------------------------------------------------------
# Analyzed data (from Task 1 - figures in USD millions, from each company's
# 10-K filings via SEC EDGAR)
# ---------------------------------------------------------------------------

DATA = {
    "microsoft": {
        2023: {"revenue": 211915, "net_income": 72361, "assets": 411976,
               "liabilities": 205753, "cfo": 87582},
        2024: {"revenue": 245122, "net_income": 88136, "assets": 512163,
               "liabilities": 243686, "cfo": 118548},
        2025: {"revenue": 281724, "net_income": 101832, "assets": 619003,
               "liabilities": 275524, "cfo": 136162},
    },
    "apple": {
        2023: {"revenue": 383285, "net_income": 96995, "assets": 352583,
               "liabilities": 290437, "cfo": 110543},
        2024: {"revenue": 391035, "net_income": 93736, "assets": 364980,
               "liabilities": 308030, "cfo": 118254},
        2025: {"revenue": 416161, "net_income": 112010, "assets": 359241,
               "liabilities": 285511, "cfo": 111482},
    },
    "tesla": {
        2023: {"revenue": 96773, "net_income": 14997, "assets": 106618,
               "liabilities": 43009, "cfo": 13256},
        2024: {"revenue": 97690, "net_income": 7091, "assets": 122070,
               "liabilities": 48390, "cfo": 14923},
        2025: {"revenue": 94827, "net_income": 3794, "assets": 137806,
               "liabilities": 54941, "cfo": 14747},
    },
}

COMPANY_NAMES = {"microsoft": "Microsoft", "apple": "Apple", "tesla": "Tesla"}


def _fmt(amount):
    """Format a $ millions figure as a readable string, e.g. 281724 -> '$281,724M ($281.7B)'."""
    return f"${amount:,}M (${amount / 1000:,.1f}B)"


def _pct_change(old, new):
    return ((new - old) / old) * 100


def _find_company(text):
    """Return 'microsoft', 'apple', or 'tesla' if one is mentioned in the text, else None."""
    for key in DATA:
        if key in text:
            return key
    return None


def _find_year(text):
    """Return 2023, 2024, or 2025 if mentioned in the text, else None."""
    for year in (2023, 2024, 2025):
        if str(year) in text:
            return year
    return None


# ---------------------------------------------------------------------------
# Chatbot logic
# ---------------------------------------------------------------------------

def simple_chatbot(user_query):
    """
    Rule-based chatbot: matches a user query to one of 5 predefined
    financial questions using simple keyword checks, then returns a
    canned response built from the analyzed data.
    """
    query = user_query.lower().strip()

    company = _find_company(query)
    year = _find_year(query) or 2025  # default to most recent year if none given

    # --- Query 1: Total revenue -------------------------------------------
    if "total revenue" in query or "revenue" in query and "growth" not in query and "change" not in query:
        if not company:
            return ("Please specify a company (Microsoft, Apple, or Tesla). "
                     "Example: 'What is Apple's total revenue in 2024?'")
        rev = DATA[company][year]["revenue"]
        return (f"{COMPANY_NAMES[company]}'s total revenue in FY{year} was {_fmt(rev)}.")

    # --- Query 2: Net income change over the last year ---------------------
    elif "net income" in query and ("change" in query or "increase" in query
                                     or "decrease" in query or "last year" in query
                                     or "growth" in query):
        if not company:
            return ("Please specify a company (Microsoft, Apple, or Tesla). "
                     "Example: 'How has Tesla's net income changed?'")
        # Compare the requested year to the prior year (default: 2025 vs 2024)
        curr_year = year if year in DATA[company] and (year - 1) in DATA[company] else 2025
        prev_year = curr_year - 1
        old_ni = DATA[company][prev_year]["net_income"]
        new_ni = DATA[company][curr_year]["net_income"]
        pct = _pct_change(old_ni, new_ni)
        direction = "increased" if pct >= 0 else "decreased"
        return (f"{COMPANY_NAMES[company]}'s net income {direction} by {abs(pct):.1f}% "
                f"from {_fmt(old_ni)} in FY{prev_year} to {_fmt(new_ni)} in FY{curr_year}.")

    # --- Query 3: Total assets ----------------------------------------------
    elif "total assets" in query or ("assets" in query and "liabilities" not in query):
        if not company:
            return ("Please specify a company (Microsoft, Apple, or Tesla). "
                     "Example: 'What are Microsoft's total assets in 2025?'")
        assets = DATA[company][year]["assets"]
        return (f"{COMPANY_NAMES[company]}'s total assets in FY{year} were {_fmt(assets)}.")

    # --- Query 4: Total liabilities ------------------------------------------
    elif "total liabilities" in query or "liabilities" in query:
        if not company:
            return ("Please specify a company (Microsoft, Apple, or Tesla). "
                     "Example: 'What are Tesla's total liabilities in 2023?'")
        liab = DATA[company][year]["liabilities"]
        return (f"{COMPANY_NAMES[company]}'s total liabilities in FY{year} were {_fmt(liab)}.")

    # --- Query 5: Cash flow from operating activities -------------------------
    elif "cash flow" in query or "operating activities" in query or "cfo" in query:
        if not company:
            return ("Please specify a company (Microsoft, Apple, or Tesla). "
                     "Example: 'What was Apple's cash flow from operations in 2024?'")
        cfo = DATA[company][year]["cfo"]
        return (f"{COMPANY_NAMES[company]}'s cash flow from operating activities "
                f"in FY{year} was {_fmt(cfo)}.")

    # --- Fallback for anything unrecognized -----------------------------------
    else:
        return ("Sorry, I can only answer predefined questions about total revenue, "
                "net income change, total assets, total liabilities, or cash flow "
                "from operations for Microsoft, Apple, or Tesla (FY2023-FY2025). "
                "Try asking, for example: 'What is Microsoft's total revenue in 2025?'")


# ---------------------------------------------------------------------------
# Command-line interaction loop
# ---------------------------------------------------------------------------

def run_chat():
    print("=" * 70)
    print("Financial Chatbot Prototype (Microsoft, Apple, Tesla | FY2023-FY2025)")
    print("=" * 70)
    print("Ask me about: total revenue, net income change, total assets,")
    print("total liabilities, or cash flow from operations.")
    print("Example: 'What is Apple's total revenue in 2024?'")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        user_query = input("You: ").strip()
        if user_query.lower() in ("quit", "exit"):
            print("Bot: Goodbye!")
            break
        if not user_query:
            continue
        response = simple_chatbot(user_query)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    run_chat()
