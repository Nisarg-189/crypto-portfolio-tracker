# Portfolio Tracker – CS50P Final Project

#### Video Demo: https://youtube.com/shorts/RUZJbtCgFmY?si=I0ASoswlbU1BrUQH

## Description

This is my final project for CS50P: a **Portfolio Tracker** that allows users to manage and evaluate their investments in both stocks and cryptocurrencies. The project includes functionality for adding assets, calculating profit/loss, saving data to disk, loading saved portfolios, and estimating portfolio value. Everything is written in Python using object-oriented programming, JSON file handling, and pytest for validation.

---

## Project Overview

The goal of this project is to provide a clean and simple command-line portfolio management tool. It supports:

- **Crypto assets**
- **Stock assets**
- **Any symbol-based investment**

The user can store multiple assets, track their buy prices, simulate current prices, and compute total portfolio performance.

---

## Features

### 🔹 Asset Management
- Add any stock/crypto using its symbol
- Auto-detect type (Stock/Crypto)
- Stores quantity and buy price
- Calculates current value
- Calculates individual profit/loss

### 🔹 Portfolio Management
- Add multiple assets
- Remove sold assets
- Get total portfolio value
- Get total portfolio profit/loss
- View all holdings

### 🔹 Save & Load (JSON File)
The portfolio is saved permanently into: portfolio.json


When the program is started again, it automatically loads and restores all saved holdings.

### 🔹 Utility Functions
- `estimate_portfolio_value(portfolio)`
- `track_profit_loss(portfolio)`
- `get_current_price(symbol)`

### 🔹 Testing With pytest
Complete test suite using:

- `monkeypatch` to mock price functions
- `tmp_path` to test file saving/loading safely

All major classes and functions are tested.

---

## Project Structure
project/
│── project.py # Main logic and classes
│── test_project.py # All pytest test cases
│── requirements.txt # Required Python libraries
│── README.md # Project documentation
│── portfolio.json # Auto-created during save function

---


---

## File Descriptions

### 📌 project.py
Contains the main classes and logic.

#### **Class: Asset**
Represents a single crypto or stock asset.
Attributes: `symbol`, `quantity`, `buy_price`, `asset_type`.
Methods:
- `current_price()` – returns simulated or monkeypatched price
- `current_value()`
- `profit_loss()`

#### **Class: Portfolio**
Manages a list of Asset objects.
Methods include:
- `add_stock()`
- `remove_stock()`
- `total_value()`
- `total_profit_loss()`
- `save_to_file()`
- `load_from_file()`

#### **Helper Functions**
- `estimate_portfolio_value(portfolio)`
- `track_profit_loss(portfolio)`
- `get_current_price(symbol)` (dummy API replacement)

---

## Design Choices

### ✔ JSON for Persistent Storage
I used JSON because it:
- Is built into Python
- Stores structured data easily
- Is readable and lightweight

### ✔ Object-Oriented Design
I chose OOP because it keeps the project modular and scalable.
Assets and portfolios behave like real entities, making logic clear and reusable.

### ✔ Comprehensive Testing
I created a full pytest suite because:
- It ensures functions behave correctly
- It catches mistakes early
- It follows real software engineering practices

`monkeypatch` was used to mock dynamic prices.
`tmp_path` was used to test file I/O safely.

---

## Future Improvements
- Add a graphical interface (Tkinter or Web UI)
- Fetch real-time stock/crypto prices from an API
- Add graphs using matplotlib
- Add export options (PDF or Excel reports)
- Add user authentication
- Add categories (Long-term, Short-term assets)

---

## Conclusion

This Portfolio Tracker project demonstrates my understanding of:

- Python object-oriented programming
- File handling with JSON
- Structured program design
- Writing & running automated tests
- Using industry-style workflows

This project satisfies all requirements for the CS50P Final Project.
Thank you for reviewing my work!





# crypto-portfolio-tracker
