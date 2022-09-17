import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Advertising.csv')
df['total_spend'] = df['Insta'] + df['YT'] + df['Facebook']
sns.scatterplot(data=df, x='total_spend', y='sales')

x = df['total_spend']
y = df['sales']
np.polyfit(x,y,deg=1)
potential_spend = np.linspace(0,500,100)
predicted_sales = 0.04868788 * potential_spend + 4.24302822
sns.scatterplot(data=df, x='total_spend', y='sales')
plt.plot(potential_spend, predicted_sales)

spend = 200
predicted_sale = 0.04868788 * spend + 4.24302822

np.polyfit(x, y, 3)
pot_spend = np.linspace(0, 500, 100)
pred_sales = 3.07615033e-07 * pot_spend**3 + \
            -1.8939244e-04 * pot_spend**2 + \
            8.20886302e-02 * pot_spend + \
            2.70495053e+00

sns.scatterplot(data=df, x='total_spend', y='sales')
plt.plot(pot_spend, pred_sales, color='red')


