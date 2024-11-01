# Fynd-Expense-calculator

![Fynd Academy Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtiujolOF_HzyTpo4OPFmoNcYnJ42LeKvxDA&s)


## Overview

Fynd Expense Calculator is a simple yet effective application designed to help users manage their expenses. This project was developed as part of the mid-course project for the Fynd Academy Python Full Stack Course. It allows users to track, filter, and report their expenses easily.

## Features

- **Add Expense**: Input the amount, date, category, and description of the expense.
- **View Expenses**: Display all recorded expenses in a user-friendly format.
- **Delete Expense**: Remove expenses by selecting their index.
- **Filter by Category**: View expenses by specific categories.
- **Generate Reports**: Create daily, weekly, or monthly reports of expenses.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/faizalimam990/Fynd-Expense-calculator.git
   cd Fynd-Expense-calculator

# Expense Tracker

## Install Dependencies

Make sure you have Python installed. Then, install any necessary libraries:

```bash
pip install -r requirements.txt
```
   
## How It Works

The application is structured around the `ExpenseTracker` class, which manages expenses stored in a CSV file. The key components include:

- **Expense**: A class representing an individual expense.
- **Category**: Manages expense categories.
- **ReportGenerator**: Generates summary reports based on the expenses logged.

## Code Overview

Here's a brief overview of how the `ExpenseTracker` class operates:

- **Load Expenses**: Loads expenses from a CSV file on startup.
- **Add Expense**: Prompts the user for expense details and saves to the CSV.
- **View Expenses**: Displays expenses in a tabular format.
- **Delete Expense**: Allows users to delete expenses by their index.
- **Filter by Category**: Lets users filter expenses by category.
- **Generate Report**: Generates a report based on user-defined periods (daily, weekly, monthly).



