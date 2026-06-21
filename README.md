

# Sales Data Analysis Project

A beginner data analysis project exploring 300 rows of retail sales data across Indian cities. Built using Python and pandas to find business insights from raw CSV data.

---

## Dashboard Output

![Sales Dashboard](sales_dashboard.png)

---

## Project Structure

```
sales-data-analysis/
│
├── sales_data.csv          # Raw dataset (300 rows)
├── sales_data_clean.csv    # Cleaned dataset with Revenue and Month columns
│
├── sales-data-analysis.py
│
├── sales_dashboard.png     # Final dashboard output
└── README.md
```

---

## Dataset

- 300 orders from January to December 2024
- 5 product categories: Electronics, Clothing, Groceries, Home & Kitchen, Books
- 8 Indian cities: Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Pune, Kolkata, Ahmedabad
- 5 payment methods: UPI, Credit Card, Debit Card, Cash, Net Banking

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Date | Order date (YYYY-MM-DD) |
| Product | Product name |
| Category | Product category |
| City | Customer city |
| Quantity | Units ordered |
| Price | Price per unit (Rs) |
| Payment_Method | Mode of payment |

---

## Business Questions Answered

- Which product category generates the most revenue?
- Which month had the highest sales?
- Which city spends the most?
- What is the average order value?
- Which payment method is most popular?
- What are the top 5 products by revenue?

---

## Tools Used

- Python 3
- pandas
- matplotlib

---

## How to Run

1. Clone this repository
2. Make sure pandas and matplotlib are installed:
```
pip install pandas matplotlib
```
3. Run the steps in order:
```
python step1_explore.py
python step2_clean.py
python step3_analyse.py
python step4_visualise.py
```

---

## Key Findings

- Electronics was the highest revenue category due to high-value products like laptops and smartphones
- UPI was the most popular payment method
- Revenue was spread fairly evenly across all 8 cities
- Average order value was approximately Rs 8,000

---

*This is a beginner portfolio project built to practice core data analyst skills: data cleaning, exploratory data analysis, and visualisation.*
