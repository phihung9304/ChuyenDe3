import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv(r"E:\ChuyenDe3\Chuong3\Chuong4\dataset.csv")

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df.head())
print(df.dtypes)

# CONVERT DATE
df['date'] = pd.to_datetime(df['date'], errors='coerce')

print("\n=== SAU KHI CONVERT DATETIME ===")
print(df.head())
print(df['date'].dtype)

# SET INDEX
df = df.set_index('date')
df = df.sort_index()

print("\n=== SAU KHI SET INDEX ===")
print(df.head())
print(df.index.dtype)

# Resample về tháng (monthly)
df_monthly = df.resample('ME').sum()

# In kết quả
print("=== DỮ LIỆU SAU KHI RESAMPLE MONTHLY ===")
print(df_monthly.head())

print("\nShape sau resample:", df_monthly.shape)
print("\nIndex sau resample:")
print(df_monthly.index)

df_plot = df_monthly.copy()

df_plot['month'] = df_plot.index.month
df_plot['quarter'] = df_plot.index.quarter

df_plot['lag_1'] = df_plot['sales'].shift(1)
df_plot['lag_3'] = df_plot['sales'].shift(3)

df_plot['rolling_mean_3'] = df_plot['sales'].rolling(3).mean()
# ===== Hiển thị bảng =====
print("=== BẢNG FEATURE ===")
print(df_plot[['sales', 'month', 'quarter', 'lag_1', 'lag_3', 'rolling_mean_3']].head(15))

print("=== SALES THEO THỜI GIAN ===")
print(df_monthly['sales'])

df_vis = df_monthly.copy()

df_vis['rolling_3'] = df_vis['sales'].rolling(3).mean()
df_vis['rolling_6'] = df_vis['sales'].rolling(6).mean()

print("=== SALES + ROLLING MEAN ===")
print(df_vis[['sales', 'rolling_3', 'rolling_6']].head(20))

print("=== TREND ANALYSIS ===")

start = df_monthly['sales'].iloc[0]
end = df_monthly['sales'].iloc[-1]

print("Sales đầu kỳ:", start)
print("Sales cuối kỳ:", end)

if end > start:
    print("Xu hướng: TĂNG")
elif end < start:
    print("Xu hướng: GIẢM")
else:
    print("Xu hướng: KHÔNG ĐỔI")

df_season = df_monthly.copy()
df_season['month'] = df_season.index.month

season_avg = df_season.groupby('month')['sales'].mean()

print("=== MÙA VỤ (TRUNG BÌNH THEO THÁNG) ===")
print(season_avg)

corr1 = df_monthly['sales'].corr(df_monthly['promotion_budget'])
print("Correlation sales vs promotion:", corr1)

corr2 = df_monthly['sales'].corr(df_monthly['num_customers'])
print("Correlation sales vs customers:", corr2)


# Bước 3
plt.figure(figsize=(10,5))

plt.plot(df_monthly.index, df_monthly['sales'])

plt.title("Sales theo thời gian")
plt.xlabel("Time")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.show()

# Bar Chart
df_bar = df_monthly.copy()
df_bar['month'] = df_bar.index.month

monthly_sales = df_bar.groupby('month')['sales'].sum()

plt.figure(figsize=(8,5))

plt.bar(monthly_sales.index, monthly_sales.values)

plt.title("Sales theo tháng")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))

plt.scatter(df_monthly['promotion_budget'], df_monthly['sales'])

plt.title("Promotion vs Sales")
plt.xlabel("Promotion Budget")
plt.ylabel("Sales")

plt.show()

df_lr = df_monthly.copy()

# bỏ missing (do lag/rolling nếu có sau này)
df_lr = df_lr.dropna()

X = df_lr[['promotion_budget', 'num_customers']]
y = df_lr['sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("=== MODEL EVALUATION ===")

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("=== MODEL COEFFICIENT ===")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

df_ma = df_monthly.copy()

# moving average 3 tháng
df_ma['MA_3'] = df_ma['sales'].rolling(window=3).mean()

# moving average 6 tháng
df_ma['MA_6'] = df_ma['sales'].rolling(window=6).mean()

print("=== MOVING AVERAGE ===")
print(df_ma[['sales', 'MA_3', 'MA_6']].head(15))

df_eval = df_monthly.copy()

# Moving Average 3 tháng
df_eval['ma_pred'] = df_eval['sales'].rolling(3).mean()

ma_data = df_eval.dropna()

rmse_ma = np.sqrt(mean_squared_error(ma_data['sales'], ma_data['ma_pred']))

print("RMSE Moving Average:", rmse_ma)

rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred))

print("RMSE Linear Regression:", rmse_lr)
print("=== MODEL COMPARISON ===")
print("Moving Average RMSE:", rmse_ma)
print("Linear Regression RMSE:", rmse_lr)
if rmse_lr < rmse_ma:
    print("Best Model: Linear Regression")
else:
    print("Best Model: Moving Average")

df_forecast = df_monthly.copy()

# danh sách lưu forecast
forecast_values = []

# lấy 3 tháng cuối
last_values = df_forecast['sales'].tolist()

for i in range(12):
    next_pred = sum(last_values[-3:]) / 3
    forecast_values.append(next_pred)
    last_values.append(next_pred)

# tạo index cho 12 tháng tiếp theo
future_dates = pd.date_range(
    start=df_forecast.index[-1] + pd.offsets.MonthEnd(1),
    periods=12,
    freq='ME'
)

df_future = pd.DataFrame({
    'forecast': forecast_values
}, index=future_dates)

print("=== FORECAST 12 THÁNG ===")
print(df_future)

plt.figure(figsize=(12,6))

# actual
plt.plot(df_monthly.index, df_monthly['sales'], label='Actual')

# forecast
plt.plot(df_future.index, df_future['forecast'], linestyle='--', label='Forecast')

plt.title("Actual vs Forecast (12 months)")
plt.xlabel("Time")
plt.ylabel("Sales")

plt.legend()
plt.xticks(rotation=45)
plt.show()