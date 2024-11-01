# Fynd-Expense-calculator

![Fynd Academy Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtiujolOF_HzyTpo4OPFmoNcYnJ42LeKvxDA&s)


## Overview

Fynd Expense Calculator is a simple yet effective application designed to help users manage their expenses. This project was developed as part of the mid-course project for the Fynd Academy Python Full Stack Course. It allows users to track, filter, and report their expenses easily.

![Overview](https://i.imgur.com/CpC3E4d.png)
## Features

- **Add Expense**: Input the amount, date, category, and description of the expense.
- **View Expenses**: Display all recorded expenses in a user-friendly format.
- **Delete Expense**: Remove expenses by selecting their index.
- **Filter by Category**: View expenses by specific categories.
- **Generate Reports**: Create daily, weekly, or monthly reports of expenses.
## Objectives

The Fynd Expense Calculator aims to empower users to take control of their finances by providing an intuitive platform for managing expenses. Our key objectives include:

- **Simplifying Expense Tracking**: Make it easy for users to record and monitor their daily expenses without any hassle.
- **Enhancing Financial Awareness**: Help users gain insights into their spending habits through detailed reports and visualizations.
- **Encouraging Responsible Spending**: Provide tools that enable users to categorize their expenses, making it easier to identify areas where they can save.
- **Fostering User Engagement**: Create an interactive experience that motivates users to actively manage their finances.
- **Supporting Financial Goals**: Assist users in setting and tracking their financial goals through comprehensive reporting features.

By achieving these objectives, we hope to make personal finance management accessible and enjoyable for everyone!

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/faizalimam990/Fynd-Expense-calculator.git
   cd Fynd-Expense-calculator


2. **Install Dependencies**

Make sure you have Python installed. Then, install any necessary libraries:

```bash
pip install -r requirements.txt
```

2. **Run the Program**

After installation, you can run the application using the following command:

```bash
python expense_track.py
```
## Examples of Interaction

- **Adding an Expense**:
  - When prompted, enter the amount, date, category, and description. For example:
    ```
    Amount: 50.00
    Date: 2024-11-01
    Category: Food
    Description: Dinner at a restaurant
    ```

- **Viewing Expenses**:
  - Choose the option to view all expenses, and they will be displayed in a table format, such as:
    ```
    | Index | Date       | Amount | Category | Description                 |
    |-------|------------|--------|----------|-----------------------------|
    | 1     | 2024-11-01 | 50.00  | Food     | Dinner at a restaurant      |
    | 2     | 2024-11-02 | 30.00  | Transport | Taxi to airport             |
    ```

- **Deleting an Expense**:
  - Select the index of the expense you want to remove. For example, to delete the first expense:
    ```
    Enter the index of the expense to delete: 1
    ```

- **Filtering by Category**:
  - Enter the desired category to view related expenses. For instance:
    ```
    Enter category to filter by: Food
    ```

- **Generating Reports**:
  - Choose a time frame (daily, weekly, monthly) to generate a report. You might see a prompt like:
    ```
    Select report period: 
    1. Daily
    2. Weekly
    3. Monthly
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



