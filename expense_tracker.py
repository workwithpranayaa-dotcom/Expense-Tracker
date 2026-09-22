#!/usr/bin/env python3
"""
Expense Tracker CLI
A simple command-line tool for tracking personal expenses.
Author: Pranaya Simkhada
"""

import argparse
import json
import os
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def next_id(expenses):
    return (max((e["id"] for e in expenses), default=0)) + 1


def cmd_add(args):
    expenses = load_expenses()
    expense = {
        "id": next_id(expenses),
        "amount": args.amount,
        "category": args.category.lower(),
        "note": args.note or "",
        "date": args.date or date.today().isoformat(),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense #{expense['id']}: {args.amount} ({expense['category']})")


def cmd_list(args):
    expenses = load_expenses()

    if args.category:
        expenses = [e for e in expenses if e["category"] == args.category.lower()]
    if args.date:
        expenses = [e for e in expenses if e["date"] == args.date]

    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<4}{'Date':<12}{'Category':<14}{'Amount':<10}Note")
    print("-" * 55)
    for e in expenses:
        print(f"{e['id']:<4}{e['date']:<12}{e['category']:<14}{e['amount']:<10}{e['note']}")


def cmd_summary(args):
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("Spending by category:")
    for category, total in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {category:<14}{total}")
    print("-" * 26)
    print(f"  {'Total':<14}{sum(totals.values())}")


def cmd_delete(args):
    expenses = load_expenses()
    remaining = [e for e in expenses if e["id"] != args.id]
    if len(remaining) == len(expenses):
        print(f"No expense found with id {args.id}")
        return
    save_expenses(remaining)
    print(f"Deleted expense #{args.id}")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple command-line expense tracker.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_p = subparsers.add_parser("add", help="Add a new expense")
    add_p.add_argument("--amount", type=float, required=True, help="Expense amount")
    add_p.add_argument("--category", type=str, required=True, help="Expense category")
    add_p.add_argument("--note", type=str, default="", help="Optional note")
    add_p.add_argument("--date", type=str, help="Date (YYYY-MM-DD), defaults to today")
    add_p.set_defaults(func=cmd_add)

    list_p = subparsers.add_parser("list", help="List expenses")
    list_p.add_argument("--category", type=str, help="Filter by category")
    list_p.add_argument("--date", type=str, help="Filter by date (YYYY-MM-DD)")
    list_p.set_defaults(func=cmd_list)

    summary_p = subparsers.add_parser("summary", help="Show totals by category")
    summary_p.set_defaults(func=cmd_summary)

    delete_p = subparsers.add_parser("delete", help="Delete an expense by id")
    delete_p.add_argument("--id", type=int, required=True, help="Expense id to delete")
    delete_p.set_defaults(func=cmd_delete)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
