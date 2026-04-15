import pandas as pd

df = pd.read_csv("shopping_cleaned.csv")

# ======================
# 3.EDA 1: PHÂN TÍCH CHI TIÊU
# ======================
print("=== PHÂN TÍCH CHI TIÊU ===")
# Số tiền khách hàng chi cho mỗi đơn hàng
print(df['purchase_amount_usd'].describe())

print("\nChi tiêu trung bình theo giảm giá:")
print(df.groupby('discount_applied')['purchase_amount_usd'].mean())

print("\nChi tiêu trung bình theo mã khuyến mãi:")
print(df.groupby('promo_code_used')['purchase_amount_usd'].mean())

result = {
    "Thống kê mô tả": df['purchase_amount_usd'].describe(),
    "TB theo giảm giá": df.groupby('discount_applied')['purchase_amount_usd'].mean(),
    "TB theo mã KM": df.groupby('promo_code_used')['purchase_amount_usd'].mean()
}

combined = pd.concat(result, axis=1)
combined.to_csv("analysis_output.csv", encoding="utf-8-sig")

# =========================
# 3.EDA 2: PHÂN TÍCH KHÁCH HÀNG
# =========================
print("\n=== PHÂN TÍCH KHÁCH HÀNG ===")
print("Tuổi trung bình:", df['age'].mean())

print("\nSố lượng theo giới tính:")
print(df['gender'].value_counts())

print("\nTop 10 địa điểm mua hàng:")
print(df['location'].value_counts().head(10))


import pandas as pd

# Giá trị
age = round(df['age'].mean(), 2)

gender_values = [f"{k}: {v}" for k, v in df['gender'].value_counts().items()]
location_values = [f"{k}: {v}" for k, v in df['location'].value_counts().head(10).items()]

# Header (cột)
columns = (
    ["Tuổi trung bình"] +
    ["Giới tính"] * len(gender_values) +
    ["Top địa điểm"] * len(location_values)
)

# Data (1 dòng)
data = [age] + gender_values + location_values

# Tạo DataFrame
final = pd.DataFrame([data], columns=columns)

# Xuất CSV
final.to_csv("phan_tich_1dong.csv", index=False, encoding="utf-8-sig")
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