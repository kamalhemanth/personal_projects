import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
# Load dataset
df = pd.read_csv('covid19_india.csv')

# Display the first few rows
print(df.head())
# Group data by states and aggregate confirmed and death cases
state_data = df.groupby('State')[['Confirmed', 'Deaths']].sum().reset_index()

# Sort the data for top states with the highest confirmed cases
top_states_confirmed = state_data.sort_values('Confirmed', ascending=False).head(10)

# Plot the results
plt.figure(figsize=(10,6))
sns.barplot(x='Confirmed', y='State', data=top_states_confirmed)
plt.title('Top 10 States with Highest Confirmed Cases')
plt.show()

# Similarly for death cases
top_states_deaths = state_data.sort_values('Deaths', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x='Deaths', y='State', data=top_states_deaths)
plt.title('Top 10 States with Highest Death Cases')
plt.show()
# Filter data for Maharashtra
maharashtra_data = df[df['State'] == 'Maharashtra']

# Plot the trend of confirmed cases
plt.figure(figsize=(10,6))
plt.plot(maharashtra_data['Date'], maharashtra_data['Confirmed'], label='Confirmed Cases', color='blue')
plt.title('Increase in COVID-19 Cases in Maharashtra')
plt.xticks(rotation=45)
plt.show()
# Convert date to ordinal (numeric format)
maharashtra_data['Date'] = pd.to_datetime(maharashtra_data['Date'])
maharashtra_data['Date_ordinal'] = maharashtra_data['Date'].map(pd.Timestamp.toordinal)

# Prepare data for linear regression
X = maharashtra_data[['Date_ordinal']]
y = maharashtra_data['Confirmed']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future cases
future_dates = pd.date_range(start='2023-01-01', periods=30)
future_dates_ordinal = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
predictions = model.predict(future_dates_ordinal)

# Plot the predictions
plt.figure(figsize=(10,6))
plt.plot(future_dates, predictions, label='Predicted Cases', color='red')
plt.title('Predicted COVID-19 Cases in Maharashtra')
plt.xticks(rotation=45)
plt.show()
