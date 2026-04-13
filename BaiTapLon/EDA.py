import pandas as pd

df = pd.read_csv("shopping_cleaned.csv")

# ======================
# 3.EDA 1: PHÂN TÍCH CHI TIÊU
# ======================
print("=== PHÂN TÍCH CHI TIÊU ===")
# Số tiền khách hàng chi cho mỗi đơn hàng
print(df['purchase_amount_(usd)'].describe())

print("\nChi tiêu trung bình theo giảm giá:")
print(df.groupby('discount_applied')['purchase_amount_(usd)'].mean())

print("\nChi tiêu trung bình theo mã khuyến mãi:")
print(df.groupby('promo_code_used')['purchase_amount_(usd)'].mean())


# =========================
# 3.EDA 2: PHÂN TÍCH KHÁCH HÀNG
# =========================
print("\n=== PHÂN TÍCH KHÁCH HÀNG ===")
print("Tuổi trung bình:", df['age'].mean())

print("\nSố lượng theo giới tính:")
print(df['gender'].value_counts())

print("\nTop 10 địa điểm mua hàng:")
print(df['location'].value_counts().head(10))


# =========================
# 3.EDA 3: PHÂN TÍCH SẢN PHẨM
# =========================
print("\n=== PHÂN TÍCH SẢN PHẨM ===")
print("\nDanh mục phổ biến:")
print(df['category'].value_counts())

print("\nTop 10 sản phẩm bán nhiều:")
print(df['item_purchased'].value_counts().head(10))

print("\nMùa mua hàng:")
print(df['season'].value_counts())


# =========================
# 3.EDA 4: PHÂN TÍCH HÀNH VI
# =========================
print("\n=== PHÂN TÍCH HÀNH VI ===")
print("\nPhương thức thanh toán:")
print(df['payment_method'].value_counts())

print("\nTần suất mua hàng:")
print(df['frequency_of_purchases'].value_counts())

print("\nSố lượng khách có/không đăng ký thành viên:")
print(df['subscription_status'].value_counts())

print("\nSố lượng theo từng danh mục sản phẩm:")
print(df['category'].value_counts())

print("\nChi tiêu trung bình theo giới tính:")
print(df.groupby('gender')['purchase_amount_(usd)'].mean())