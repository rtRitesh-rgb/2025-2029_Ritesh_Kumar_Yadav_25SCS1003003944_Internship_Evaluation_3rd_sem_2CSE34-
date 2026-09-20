# BCG GenAI Job Simulation – Financial Data Analysis & Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Forage](https://img.shields.io/badge/Forage-BCG%20GenAI%20Job%20Simulation-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

A practical financial data analysis and rule-based chatbot project completed as part of the **BCG GenAI Job Simulation on Forage**.

The project focuses on extracting and analyzing financial data from SEC 10-K filings for Microsoft, Apple, and Tesla, followed by the development of a Python-based financial chatbot that answers predefined financial queries.

---

## 👨‍💻 Author

**Ritesh Kumar Yadav**

- 🎓 B.Tech Computer Science & Engineering
- 🏫 IILM University, Greater Noida
- 📚 2nd Year | Section: 2CSE34
- 🆔 Roll No.: 25SCS1003003944
- 🎓 Batch: 2025–2029

---

## 📌 About the Project

This repository contains the work completed during the **BCG GenAI Job Simulation provided through Forage**.

The simulation involved working with financial data and developing a prototype financial chatbot.

The project was divided into two major tasks:

1. **Financial Data Analysis**
2. **Financial Chatbot Prototype**

The overall workflow can be summarized as:

```text
SEC 10-K Filings
       ↓
Financial Data Extraction
       ↓
Excel / CSV Dataset
       ↓
Python + Pandas Analysis
       ↓
Financial Insights
       ↓
Rule-Based Financial Chatbot
       ↓
Testing & Documentation
```


📊 Task 1 – Financial Data Analysis
Objective

Analyze financial information from the annual 10-K filings of:

Microsoft
Apple
Tesla

for FY2023–FY2025.

Financial Metrics

The following metrics were extracted and analyzed:

Metric	Description
Total Revenue	Company's total reported revenue
Net Income	Reported net income
Total Assets	Total assets reported on the balance sheet
Total Liabilities	Total liabilities reported on the balance sheet
Operating Cash Flow	Cash generated from operating activities
🔍 Data Sources

Financial information was obtained from company SEC 10-K filings through SEC EDGAR.

The analysis also considered an important factor when comparing companies:

Fiscal year-end dates are different across Microsoft, Apple, and Tesla.

Therefore, fiscal years should not automatically be interpreted as identical calendar periods.

🛠️ Analysis Process

The financial analysis followed these steps:

Identify relevant 10-K filings.
Extract required financial metrics.
Organize the data in Excel.
Convert the dataset into CSV format.
Load the data using Pandas.
Perform data aggregation and grouping.
Calculate year-over-year changes.
Calculate selected financial ratios.
Analyze trends across companies.
Document observations and conclusions.
📈 Key Observations
Microsoft

Microsoft showed strong growth across the analyzed period, with increases in:

Revenue
Net Income
Operating Cash Flow

The analysis also showed expansion of the balance sheet alongside continued investment in infrastructure and technology.

Apple

Apple experienced a relatively small decline in revenue and net income during FY2024, followed by a strong recovery in FY2025.

The company also maintained strong operating cash flow relative to net income.

Tesla

Tesla's revenue remained relatively stable across the period, while net income declined significantly.

The analysis highlighted the importance of looking beyond revenue alone when evaluating financial performance.

General Insights

The analysis demonstrated that:

Raw financial figures alone do not provide the complete picture.
YoY changes provide useful context.
Financial ratios can reveal relationships between different metrics.
Fiscal-year differences matter when comparing companies.
Accurate data extraction and provenance are important in financial analysis.
🤖 Task 2 – Financial Chatbot
Objective

Develop a beginner-friendly Python financial chatbot using the dataset created during Task 1.

The chatbot uses rule-based logic rather than machine learning or a generative AI model.

💬 Supported Queries

The chatbot supports predefined queries related to:

Total Revenue
Net Income Change
Total Assets
Total Liabilities
Cash Flow from Operating Activities

It supports:

Microsoft
Apple
Tesla
FY2023
FY2024
FY2025
⚙️ Chatbot Features
User input through Python input()
Company detection
Fiscal year detection
Default FY2025 when a year is not specified
Financial metric detection
if-elif-else based query handling
Missing-company handling
Unsupported-query fallback
Predefined financial responses
Automated testing
🏗️ Chatbot Architecture
             User Query
                  │
                  ▼
        Query / Keyword Detection
                  │
                  ▼
       Company + Fiscal Year
             Detection
                  │
                  ▼
        Financial Dataset
                  │
                  ▼
        Rule-Based Processing
                  │
                  ▼
          Financial Response
🧪 Testing

The chatbot was tested using a separate test script.

Testing included:

Normal financial queries
Different companies
Different fiscal years
Missing company inputs
Unsupported or unrelated queries

Test results are stored in:

test_results.txt
📁 Repository Structure
.
├── financial_chatbot.py
├── test_chatbot.py
├── test_results.txt
├── README.md
│
├── data/
│   └── financial_data.csv
│
├── analysis/
│   ├── financial_analysis.ipynb
│   └── BCG_GenAI_Financial_Analysis.html
│
└── docs/
    └── project_documentation/

Adjust the folder names if your actual repository structure differs.

💻 Technologies & Tools
Programming
Python
Data Analysis
Pandas
Jupyter Notebook
Excel
CSV
Financial Data
SEC EDGAR
Company 10-K filings
Development
Python dictionaries
Conditional logic
Automated testing
Documentation
📚 Skills Demonstrated

This project provided practical experience in:

Financial data extraction
Financial statement analysis
Python programming
Pandas data analysis
Excel and CSV data handling
Data cleaning and structuring
Year-over-year analysis
Financial ratios
Rule-based chatbot development
Testing and debugging
Technical documentation
Data provenance
Working with SEC filings

It also provided an understanding of the difference between a rule-based chatbot and a true AI/ML/GenAI system.

🚀 Future Improvements

The current chatbot is intentionally a simple rule-based prototype.

Potential improvements include:

Automated SEC/XBRL financial data extraction
NLP-based query understanding
Retrieval-Augmented Generation (RAG)
Integration with live financial data
Support for more companies
More financial metrics and ratios
Conversational context
Source citations in chatbot responses
Visualization generation from user queries
GenAI-powered financial question answering

These are future improvements and are not part of the current implementation.

🎯 Project Takeaway

The project demonstrates a complete workflow from:

Financial Documents
       ↓
Data Extraction
       ↓
Data Analysis
       ↓
Financial Insights
       ↓
Python Application
       ↓
Testing
       ↓
Documentation

It provided hands-on exposure to combining financial analysis, Python programming, data processing, and basic AI-oriented application development.

📜 Program

BCG GenAI Job Simulation
Completed through Forage

The experience focused on applying data analysis and AI-related problem-solving concepts to a financial use case.

🔗 References
SEC EDGAR – Financial filings
Microsoft Annual Reports
Apple Annual Reports
Tesla Annual Reports
Python Documentation
Pandas Documentation
Jupyter Documentation
Forage – BCG GenAI Job Simulation
👤 Author

Ritesh Kumar Yadav
B.Tech CSE | IILM University, Greater Noida
Section: 2CSE34
Roll No.: 25SCS1003003944
Batch: 2025–2029
