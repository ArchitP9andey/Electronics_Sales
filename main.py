import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from pandas.io.feather_format import to_feather

df = pd.read_csv('https://raw.githubusercontent.com/ArchitP9andey/Electronics_Sales/refs/heads/main/Sales.csv')

df['date'] = pd.to_datetime(df['date'])

today = datetime.today().date()

df['date'] = df['date'].dt.date

df = df.loc[df['date'] == today]

df = df.groupby('product').agg(totals_sales = ('sales', 'sum'))
df = df.reset_index()

df.to_csv(f'{today} report.csv')

plt.bar(df['product'], df['totals_sales'])

plt.savefig(f'{today} report.png')