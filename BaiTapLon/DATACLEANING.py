import pandas as pd

# ======================
# 1. LOAD DATA
# ======================
df = pd.read_csv("shopping_trends.csv")

print("===== BAN ĐẦU =====")
print(df.info())
print("Shape:", df.shape)

# ======================
# 2. XÓA TRÙNG
# ======================
df = df.drop_duplicates()

# ======================
# 3. CHUẨN HÓA TÊN CỘT
# ======================
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

print("\nTên cột:", df.columns)

# ======================
# 4. CHUẨN HÓA KIỂU DỮ LIỆU
# ======================
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["purchase_amount_usd"] = pd.to_numeric(df["purchase_amount_usd"], errors="coerce")

# ======================
# 5. CHUẨN HÓA TEXT
# ======================
df["gender"] = df["gender"].str.strip().str.capitalize()
df["item_purchased"] = df["item_purchased"].str.strip()

if "category" in df.columns:
    df["category"] = df["category"].str.strip().str.title()

# ======================
# 6. XỬ LÝ GIÁ TRỊ THIẾU
# ======================
print("\nMissing trước khi xử lý:")
print(df.isnull().sum())

df = df.dropna()

# ======================
# 7. LỌC DỮ LIỆU HỢP LỆ
# ======================
df = df[(df["age"] >= 18) & (df["age"] <= 100)]
df = df[df["purchase_amount_usd"] > 0]

# ======================
# 8. XỬ LÝ OUTLIER (IQR)
# ======================
Q1 = df["purchase_amount_usd"].quantile(0.25)
Q3 = df["purchase_amount_usd"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["purchase_amount_usd"] >= lower) &
        (df["purchase_amount_usd"] <= upper)]

# ======================
# 9. RESET INDEX
# ======================
df = df.reset_index(drop=True)

# ======================
# 10. KIỂM TRA SAU CLEAN
# ======================
print("\n===== SAU CLEAN =====")
print(df.info())
print("Shape:", df.shape)

# ======================
# 11. LƯU FILE
# ======================
df.to_csv("shopping_cleaned.csv", index=False)

print("\n✅ Đã lưu file: shopping_cleaned.csv")