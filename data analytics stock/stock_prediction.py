import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


stock_data = yf.download("TSLA", start="2000-01-01",end="2024-01-01")
stock_data = stock_data[['Close']]  
print(stock_data.head())


stock_data['Shifted_Close'] = stock_data['Close'].shift(-1)  
stock_data.dropna(inplace=True)  

X = np.array(stock_data[['Close']])
y = np.array(stock_data['Shifted_Close'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

plt.figure(figsize=(10, 5))
plt.plot(y_test, label="Actual Price", color='blue')
plt.plot(y_pred, label="Predicted Price", color='red')
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.title("Stock Price Prediction using Linear Regression")
plt.legend()
plt.show()
