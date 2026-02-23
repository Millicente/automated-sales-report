# Automated Sales Reporting System

## Description
A Python automation project that connects to a SQLite database, pulls sales data, analyzes it, and automatically generates a professional Excel report with styled tables and charts — scheduled to run daily or weekly and delivered automatically via email.

## Tech Stack
- Python 3
- SQLite
- Pandas
- Openpyxl
- Matplotlib
- Schedule
- Smtplib

## Project Structure
automated-sales-report/
├── data/                  # Contains the SQLite database
├── output/                # Contains the generated Excel report
├── logs/                  # Contains automation log files
├── .env                   # Stores email credentials (not pushed to GitHub)
├── src/
│   ├── create_database.py # Creates and populates the database
│   ├── query_sales.py     # Queries and displays sales data
│   ├── generate_report.py # Generates and emails the styled Excel report
│   └── automate_report.py # Schedules the report automatically
└── README.md

## Setup
1. Download or copy the project files into a folder
2. Create a virtual environment: `python -m venv env`
3. Activate it: `source env/Scripts/activate`
4. Install dependencies: `pip install pandas openpyxl matplotlib schedule python-dotenv`
5. Create a `.env` file with your email credentials:
   - EMAIL_ADDRESS=your_email@gmail.com
   - EMAIL_PASSWORD=your_app_password
   - EMAIL_RECEIVER=receiver_email@gmail.com
6. Create the database: `python src/create_database.py`

## Usage
- Run once: `python src/automate_report.py`
- Run daily at 08:00: `python src/automate_report.py --daily`
- Run every Monday at 08:00: `python src/automate_report.py --weekly`
