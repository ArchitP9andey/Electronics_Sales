📊 Electronics Sales Data Analyzer

A Python data analysis project that reads electronic sales data from a CSV file and filters it for analytics — including today’s data and nearby dates.

🚀 Project Overview

This project uses Python, Pandas, and Matplotlib to:

Load a sales dataset (Sales.csv)

Convert date columns to datetime

Filter sales for specific dates (including today’s date)

Display or analyze filtered results

It’s ideal for learning:
✔ Data filtering in Pandas
✔ Working with dates
✔ Basic analytics pipelines
✔ Preparing data for visualization

📂 Repository Structure
Electronics_Project/
├── main.py
├── Sales.csv
├── README.md
├── .venv/ (virtual environment)
├── External Libraries/
└── Scratches and Consoles/

🛠️ Technologies Used
Tool	Purpose
Python	Main language
Pandas	Data manipulation
Matplotlib	Plotting data
datetime	Date processing
GitHub	Version control
PyCharm	Development IDE
🧠 How It Works

Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


Load Sales Data

Loads sales information:

df = pd.read_csv('Sales.csv')


Convert Dates

Convert the date column into Python date objects:

df['date'] = pd.to_datetime(df['date']).dt.date


Filter for Today

This checks if entries exist for today’s date:

today = datetime.today().date()
today_sales = df[df['date'] == today]
print(today_sales)

📈 Demo Example

Before filtering:

date,product,sales
2026-02-06,Laptop,450
2026-02-05,Mobile,230
2026-02-07,Tablet,180


After filtering for today (e.g., 2026-02-06):

date,product,sales
2026-02-06,Laptop,450

📁 Sample CSV with Today + Nearby Dates

You can use this sample CSV that includes today + nearby dates to test the logic:

🔗 Sales_today_nearby.csv

🚀 How to Run

Clone the repository:

git clone https://github.com/<your-username>/Electronics_Project.git


Install dependencies:

pip install pandas matplotlib


Run the script:

python main.py


Check the output in your console.

🛠 Tips & Enhancements

✔ Add graphs to visualize trends
✔ Add weekly / monthly filters
✔ Export filtered results to Excel
✔ Deploy as a small web app (Streamlit / Flask)

🙌 Credits

Made with ❤️ while learning Python data analysis techniques.
