import pandas as pd

df = pd.read_csv("shopping_cleaned.csv")

# # ======================
# # 3.EDA 1: PHÂN TÍCH CHI TIÊU
# # ======================
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
combined.to_csv("outputcsv/phan_tich_chi_tieu.csv", encoding="utf-8-sig")

# # =========================
# # 3.EDA 2: PHÂN TÍCH KHÁCH HÀNG
# # =========================
print("\n=== PHÂN TÍCH KHÁCH HÀNG ===")
print("Tuổi trung bình:", df['age'].mean())

print("\nSố lượng theo giới tính:")
print(df['gender'].value_counts())

print("\nTop 10 địa điểm mua hàng:")
print(df['location'].value_counts().head(10))

result = {
    "Tuổi trung bình": pd.Series({"Giá trị": df['age'].mean()}),

    "Số lượng theo giới tính": df.groupby('gender')['age'].count(),

    "Top 10 địa điểm": df.groupby('location')['age'].count().sort_values(ascending=False).head(10)
}

combined = pd.concat(result, axis=1)
combined.to_csv("outputcsv/phan_tich_khach_hang.csv", encoding="utf-8-sig")

# # =========================
# # 3.EDA 3: PHÂN TÍCH SẢN PHẨM
# # =========================
print("\n=== PHÂN TÍCH SẢN PHẨM ===")
print("\nDanh mục phổ biến:")
print(df['category'].value_counts())

print("\nTop 10 sản phẩm bán nhiều:")
print(df['item_purchased'].value_counts().head(10))

print("\nMùa mua hàng:")
print(df['season'].value_counts())

result = {
    "Danh mục phổ biến": df['category'].value_counts(),

    "Top 10 sản phẩm": df['item_purchased'].value_counts().head(10),

    "Mùa mua hàng": df['season'].value_counts()
}

combined = pd.concat(result, axis=1)
combined.to_csv("outputcsv/phan_tich_san_pham.csv", encoding="utf-8-sig")


# # =========================
# # 3.EDA 4: PHÂN TÍCH HÀNH VI
# # =========================
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
print(df.groupby('gender')['purchase_amount_usd'].mean())

result = {
    "Phương thức thanh toán": df['payment_method'].value_counts(),

    "Tần suất mua hàng": df['frequency_of_purchases'].value_counts(),

    "Đăng ký thành viên": df['subscription_status'].value_counts(),

    "Danh mục sản phẩm": df['category'].value_counts(),

    "Chi tiêu TB theo giới tính": df.groupby('gender')['purchase_amount_usd'].mean()
}

combined = pd.concat(result, axis=1)
combined.to_csv("outputcsv/phan_tich_hanh_vi.csv", encoding="utf-8-sig")

# =========================
# 3.EDA 5: ID mua nhiều nhất
# =========================
print("\n=== TOP KHÁCH HÀNG CHI TIÊU NHIỀU NHẤT ===")

top_customers = df.groupby('customer_id')['purchase_amount_usd']\
    .sum()\
    .sort_values(ascending=False)\
    .head(10)

print(top_customers)

# Xuất CSV
top_customers.to_csv("outputcsv/top_khach_hang.csv", encoding="utf-8-sig")



print("\n=== PHÂN TÍCH KẾT HỢP ===")

print("\nChi tiêu theo giới tính (describe):")
print(df.groupby('gender')['purchase_amount_usd'].describe())

print("\nChi tiêu theo danh mục (describe):")
print(df.groupby('category')['purchase_amount_usd'].describe())

print("\nChi tiêu theo mùa (describe):")
print(df.groupby('season')['purchase_amount_usd'].describe())

result = {
    "Giới tính vs Chi tiêu": df.groupby('gender')['purchase_amount_usd'].describe(),
    "Danh mục vs Chi tiêu": df.groupby('category')['purchase_amount_usd'].describe(),
    "Mùa vs Chi tiêu": df.groupby('season')['purchase_amount_usd'].describe()
}

combined = pd.concat(result, axis=1)
combined.to_csv("outputcsv/phan_tich_ket_hop.csv", encoding="utf-8-sig")


print("\n=== CROSSTAB ===")

gender_category = pd.crosstab(df['gender'], df['category'])
season_category = pd.crosstab(df['season'], df['category'])

print("\nGiới tính vs Danh mục:")
print(gender_category)

print("\nMùa vs Danh mục:")
print(season_category)

result = {
    "Gender vs Category": gender_category,
    "Season vs Category": season_category
}

combined = pd.concat(result, axis=1)
combined.to_csv("outputcsv/phan_tich_crosstab.csv", encoding="utf-8-sig")

print("\n=== PHÂN TÍCH DOANH THU ===")

print("\nDoanh thu theo danh mục:")
print(df.groupby('category')['purchase_amount_usd'].sum())

print("\nDoanh thu theo mùa:")
print(df.groupby('season')['purchase_amount_usd'].sum())

result = {
    "Doanh thu theo danh mục": df.groupby('category')['purchase_amount_usd'].sum(),
    "Doanh thu theo mùa": df.groupby('season')['purchase_amount_usd'].sum()
}

combined = pd.concat(result, axis=1)
combined.to_csv("outputcsv/phan_tich_doanh_thu.csv", encoding="utf-8-sig")