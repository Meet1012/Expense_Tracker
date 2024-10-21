# Expense Tracker

This is a simple command-line application for tracking expenses. It allows users to add, delete, update, summarize, and display expenses. The data is stored in a JSON file.

## Features

- Add new expenses with a description and amount.
- Delete existing expenses by their ID.
- Update expenses (either description or amount).
- View total expenses for a specific month or overall.
- Display a list of all expenses in a tabular format.

## Prerequisites

- Python 3.x
- `pandas` library (install using `pip install pandas`)

## Usage

1. Clone this repository or download the script.
2. Ensure you have a JSON file named `expense.json` in the same directory (the program will create one if it doesn't exist).
3. Run the script using the command line.

### Command Syntax

```bash
python expense_tracker.py <function> [--description <description>] [--amount <amount>] [--id <id>] [--month <month>]
