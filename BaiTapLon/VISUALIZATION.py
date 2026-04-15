import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shopping_cleaned.csv")

# ======================
# 4. VISUALIZATION
# ======================

# 1. Số tiền mua hàng
plt.figure(figsize=(10, 5))
plt.hist(df['purchase_amount_usd'], bins=20, edgecolor='black')
plt.title("Số tiền mua hàng")
plt.xlabel("Số tiền USD")
plt.ylabel("Số lượng đơn hàng")

plt.savefig("so_tien_mua_hang.png", dpi=250, bbox_inches='tight')
plt.show()


# 2. Chi tiêu theo giới tính
plt.figure(figsize=(10, 5))
avg_gender = df.groupby('gender')['purchase_amount_usd'].mean()
plt.bar(avg_gender.index, avg_gender.values, edgecolor='black')

plt.title("Chi tiêu trung bình theo giới tính")
plt.xlabel("Giới tính")
plt.ylabel("Chi tiêu trung bình (USD)")

plt.savefig("chi_tieu_theo_gioi_tinh.png", dpi=250, bbox_inches='tight')
plt.show()


# 3. Chi tiêu theo độ tuổi
plt.figure(figsize=(10, 5))
plt.scatter(df['age'], df['purchase_amount_usd'])

plt.title("Phân nhóm khách hàng theo tuổi và chi tiêu")
plt.xlabel("Tuổi")
plt.ylabel("Chi tiêu (USD)")

plt.savefig("chi_tieu_theo_tuoi.png", dpi=250, bbox_inches='tight')
plt.show()


# 4. Danh mục sản phẩm
plt.figure(figsize=(10, 5))
category_counts = df['category'].value_counts()
plt.bar(category_counts.index, category_counts.values, edgecolor='black')

plt.title("Hành vi mua hàng theo danh mục")
plt.xlabel("Danh mục")
plt.ylabel("Số lượng")

plt.savefig("danh_muc_san_pham.png", dpi=250, bbox_inches='tight')
plt.show()


# 5. Phương thức thanh toán
plt.figure(figsize=(10, 5))
payment_counts = df['payment_method'].value_counts()
plt.bar(payment_counts.index, payment_counts.values, edgecolor='black')

plt.title("Phương thức thanh toán")
plt.xlabel("Loại thanh toán")
plt.ylabel("Số lượng")
plt.xticks(rotation=45)

plt.savefig("phuong_thuc_thanh_toan.png", dpi=250, bbox_inches='tight')
plt.show()