import pandas as pd

# đọc dữ liệu
df = pd.read_csv("shopping_trends.csv")

# ========================
# 1. Chuẩn hóa tên cột
# ========================
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
#strip(): loại bỏ khoảng trắng thừa ở đầu và cuối
#lower(): chuyển tất cả chữ thành chữ thường
#replace(" ", "_"): thay thế khoảng trắng bằng dấu gạch dưới

# ========================
# 2. Xóa dữ liệu trùng
# ========================
df = df.drop_duplicates()

# ========================
# 3. Xử lý missing values
# ========================
print("Missing trước khi xử lý:")
print(df.isnull().sum())

# số → median
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    # có lỗi thì chuyển thành NaN
    df['age'] = df['age'].fillna(df['age'].median())
    # điền NaN bằng giá trị trung vị của cột age

# tiền → median
if 'purchase_amount_(usd)' in df.columns:
    df['purchase_amount_(usd)'] = pd.to_numeric(df['purchase_amount_(usd)'], errors='coerce')
    df['purchase_amount_(usd)'] = df['purchase_amount_(usd)'].fillna(df['purchase_amount_(usd)'].median())

# category → mode
for col in ['gender', 'payment_method', 'item_purchased']:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])

# ========================
# 4. Làm sạch dữ liệu text
# ========================
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.lower()

# ========================
# 5. Xử lý outliers (tuổi)
# ========================
if 'age' in df.columns:
    Q1 = df['age'].quantile(0.25)
    Q3 = df['age'].quantile(0.75)
    IQR = Q3 - Q1

    df = df[(df['age'] >= Q1 - 1.5 * IQR) & (df['age'] <= Q3 + 1.5 * IQR)]

# ========================
# 6. Kiểm tra lại
# ========================
print("\nSau khi làm sạch:")
print("Shape:", df.shape)
print(df.describe())
print(df.isnull().sum())

# ========================
# 7. Lưu file sạch
# ========================
df.to_csv("shopping_trends_clean.csv", index=False)

print("\nĐã lưu file: shopping_trends_clean.csv")