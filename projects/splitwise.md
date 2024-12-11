# Project: Splitwise Clone

**Course**: Advanced Python
**Project Name**: Splitwise Clone
**Description**: A Python-based Splitwise clone focused on creating a robust, graph-driven system for managing and simplifying shared expenses among groups, housemates, and friends.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Architecture](#project-architecture)
3. [Features](#features)
4. [Graph Theory in the Project](#graph-theory-in-the-project)
5. [Usage](#usage)

---
## Overview
This project is a Python implementation of an expense-sharing application inspired by Splitwise, designed to minimize the stress of managing shared expenses with friends, housemates, and groups. The application allows users to keep track of balances, expenses, and repayments, providing a visual representation and simplification of expense-related data through graph theory.

## Project Architecture

The project is built around a graph-based data structure where:
- **Nodes** represent users.
- **Edges** represent financial obligations between users.
- **Weights on edges** represent the owed amounts between nodes.

This structure supports complex group transactions and allows for advanced algorithms, including:
- **Debt Simplification**: Reducing the number of transactions required to settle up.
- **Centrality Calculation**: Identifying users with high centrality in the graph to optimize payment routes.
  
**Directory Structure**
```plaintext
splitwise_clone/
│
├── core/                      # Core application files
│   ├── graph.py               # Graph and centrality algorithms
│   ├── debt_simplification.py # Debt simplification functions
│   └── balance_calculation.py # Balance and expense calculations
│
├── models/                    # Data models
│   ├── user.py                # User model
│   └── group.py               # Group model
│
├── utils/                     # Utility functions
│   ├── currency_conversion.py # Currency conversion utilities
│   ├── receipt_scanner.py     # Receipt scanning tools
│   └── storage.py             # storage management
│
└── README.md                  # Project README
```

---

## Features

### Core Features
1. **Track Balances**: Monitor shared expenses, who owes whom, and current balances.
2. **Organize Expenses**: Organize expenses for various groups (e.g., housemates, friends, family, trips).
3. **Add Expenses Easily**: Add expenses quickly, specifying who paid and who owes.
4. **Pay Friends Back**: Record repayments, with options for cash or online payments.
5. **Graphs and Charts**: Visualize expenses and balances.

### Detailed Feature List
- **Add Groups and Friends**: Create groups and add friends or contacts to keep track of expenses within a specific group.
- **Split Expenses**: Log and split expenses with individuals or groups.
- **Equal or Unequal Splits**: Split expenses equally or set custom ratios.
- **Split by Percentage or Shares**: Flexible splitting by percentage or share-based allocations.
- **Calculate Total Balances**: Calculate the total owed balances per person and per group.
- **Simplify Debts**: Use graph simplification algorithms to reduce debt loops and minimize repayments.
- **Recurring Expenses**: Track recurring expenses for items like rent, utilities, or subscriptions.
- **Offline Mode**: Access and manage expenses offline with data sync when back online.
- **Spending Totals**: Calculate spending totals by user, category, or group.
- **Categorize Expenses**: Group expenses by categories such as Food, Travel, Utilities, and more.
- **Transaction Import**: Import expenses from external sources.
- **Charts and Graphs** (Bonus): Display graphical data on spending trends, balances, and group expenses.
- **Save Default Splits**: Predefine default splits to streamline repetitive entries.
- **Expense Search**: Search for past expenses by user, date, or description.

---
## Graph Theory in the Project

This project leverages graph theory to improve the user experience in tracking and simplifying expenses:

1. **Graph Representation of Debts**:
   - Each user in the system is a **node**.
   - **Edges** with weights between nodes represent financial obligations.
   - This graph structure helps to visualize who owes whom and by how much.

2. **Debt Simplification Using Cost Graph Simplification**:
   - The graph structure enables simplification of debts through **cost graph simplification** algorithms, which reduce the total number of required transactions.
   - This feature minimizes the debt cycle within groups by merging and simplifying mutual debts.

3. **Centrality Calculation**:
   - Centrality measures (e.g., degree centrality) are used to identify users who are central within the debt network, helping prioritize or optimize payment routes.
   - Centrality can aid in determining the optimal path for debt repayments within groups, saving users effort.

4. **Graph Algorithms for Optimized Balance Calculations**:
   - Algorithms for calculating shortest paths, cycle detection, and weighted balancing are implemented for efficient financial tracking.
  ---
## Usage

1. **Adding Users and Groups**:
   - Create a group and add members to start tracking expenses.

2. **Adding and Splitting Expenses**:
   - Add expenses with options for equal or custom splits.
   - Choose between percentage, shares, or equal splits.

3. **Debt Simplification and Centrality**:
   - View simplified debts by clicking on the "Simplify Debts" option.
   - Review suggestions for optimized payment routes based on centrality scores.
