# Expense Tracker CLI

A command-line expense tracker written in Python, using only the standard library — no dependencies to install. Expenses are saved to a local JSON file.

## Usage
```bash
git clone https://github.com/workwithpranayaa-dotcom/expense-tracker-cli.git
cd expense-tracker-cli

# add an expense
python expense_tracker.py add --amount 450 --category food --note "Lunch"

# list all expenses
python expense_tracker.py list

# see totals by category
python expense_tracker.py summary

# delete an expense by id
python expense_tracker.py delete --id 3
```

## Features
- Add, list, delete expenses
- Category summary with totals
- Filter list by category or date
- Data persisted to `expenses.json` (auto-created)

## Built with
Python (standard library only: `argparse`, `json`, `datetime`)

## Author
Pranaya Simkhada
