import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shopping_cleaned.csv")
# ======================
# 4. VISUALIZATION
# ======================

# Số tiền mua hàng
# plt.figure(figsize=(10, 5))
# plt.hist(df['purchase_amount_(usd)'],bins=20,color="skyblue",edgecolor='black')
# plt.title("Số tiền mua hàng")
# plt.xlabel("Số tiền USD")
# plt.ylabel("Số lượng đơn hàng")
# plt.show()

# # Chi tiêu theo giới tính
# plt.figure(figsize=(10, 5))
# avg_gender = df.groupby('gender')['purchase_amount_(usd)'].mean()
# plt.bar(avg_gender.index, avg_gender.values,color="skyblue",edgecolor='black')
# plt.title("Chi tiêu trung bình theo giới tính")
# plt.xlabel("Giới tính")
# plt.ylabel("Chi tiêu trung bình (USD)")
# plt.show()

# # Chi tiêu mỗi độ tuổi
# plt.figure(figsize=(10, 5))
# plt.scatter(df['age'], df['purchase_amount_(usd)'])
# plt.title("Phân nhóm khách hàng theo tuổi và chi tiêu")
# plt.xlabel("Tuổi")
# plt.ylabel("Chi tiêu (USD)")
# plt.show()

# Số hàng mua nhiều
# plt.figure(figsize=(10, 5))
# category_counts = df['category'].value_counts()
# plt.bar(category_counts.index, category_counts.values,color="skyblue",edgecolor='black')
# plt.title("Hành vi mua hàng theo danh mục")
# plt.xlabel("Danh mục")
# plt.ylabel("Số lượng")
# plt.show()

# # Phương thức thanh toán được sử dụng nhiều
# payment_counts = df['payment_method'].value_counts()
# plt.figure(figsize=(10, 5))
# plt.bar(payment_counts.index, payment_counts.values,color='skyblue', edgecolor='black')
# plt.title("Phương thức thanh toán")
# plt.xlabel("Loại thanh toán")
# plt.ylabel("Số lượng")
# plt.xticks(rotation=45)
# plt.show()