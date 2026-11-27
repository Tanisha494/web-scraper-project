
# Personal Expense Tracker

A simple Python command-line application to manage daily expenses.

## Features

- Add new expenses.
- View all recorded expenses.
- Filter expenses by category.
- Calculate totals for each category.
- Save expenses permanently in a CSV file.
- Validate dates and expense amounts.
- Menu-driven interface.

## Technologies Used

- Python
- CSV module
- Datetime module
- Decimal module

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

   python expense_tracker.py

## CSV File

All expenses are stored in `expenses.csv`.

The CSV file contains sample data with 10 expense records.

## Problem Fixed

Initially, invalid dates and amounts could cause incorrect expense records. I fixed this by adding input validation using datetime and Decimal. I also used `newline=""` when opening CSV files to avoid extra blank lines.

## Author

Tanisha
