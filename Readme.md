# 📊 Expense Tracker

**A simple command-line application for tracking your expenses!** This tool allows users to manage their expenses efficiently, providing functionalities to add, delete, update, summarize, and display expenses. You can check out the project details [Expense Tracker](https://roadmap.sh/projects/expense-tracker).

## 🚀 Features: 
- **Add Expenses:** Track your spending by adding new expenses with descriptions and amounts. 
- **Delete Expenses:** Remove any expense from your records by its unique ID. 
- **Update Expenses:** Modify existing expenses (either the description or the amount). 
- **Summary View:** Get a quick overview of total expenses for a specific month or overall. 
- **Display List:** View all expenses in a neat tabular format.

## 📋 Prerequisites: 
Make sure you have the following installed: 
- Python 3.x 
- `pandas` library (install it using: `pip install pandas`)

## 📦 Usage: 
1. Clone this repository or download the script. 
2. Ensure you have a JSON file named `expense.json` in the same directory (the program will create one if it doesn't exist). 
3. Run the script using the command line.

### 🔧 Command Syntax:
```bash
python expense_tracker.py <function> [--description <description>] [--amount <amount>] [--id <id>] [--month <month>]
