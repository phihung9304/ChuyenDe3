import pandas as pd   # Thư viện xử lý data dạng bảng

# ======================
# 1. LOAD DATA
# ======================
df = pd.read_csv("shopping_trends.csv")   # Đọc file CSV vào DataFrame

print("===== BAN ĐẦU =====")
print(df.info())      # Xem thông tin cột, kiểu dữ liệu, số lượng dữ liệu
print("Shape:", df.shape)   # In số dòng và số cột

# ======================
# 2. XÓA TRÙNG
# ======================
df = df.drop_duplicates()   # Xóa các dòng bị trùng

# ======================
# 3. CHUẨN HÓA TÊN CỘT
# ======================
df.columns = (
    df.columns
    .str.strip()   # Xóa khoảng trắng đầu/cuối
    .str.lower()   # Chuyển thành chữ thường
    .str.replace(" ", "_")   # Thay khoảng trắng bằng _
    .str.replace("(", "", regex=False)   # Xóa dấu (
    .str.replace(")", "", regex=False)   # Xóa dấu )
)

print("\nTên cột:", df.columns)   # In tên cột sau khi chuẩn hóa

# ======================
# 4. CHUẨN HÓA KIỂU DỮ LIỆU
# ======================
df["age"] = pd.to_numeric(df["age"], errors="coerce")  
# Chuyển cột age sang số, lỗi sẽ thành NaN

df["purchase_amount_usd"] = pd.to_numeric(df["purchase_amount_usd"], errors="coerce")  
# Chuyển cột chi tiêu sang số

# ======================
# 5. CHUẨN HÓA TEXT
# ======================
df["gender"] = df["gender"].str.strip().str.capitalize()  
# Xóa khoảng trắng + viết hoa chữ cái đầu

df["item_purchased"] = df["item_purchased"].str.strip()  
# Xóa khoảng trắng tên sản phẩm

if "category" in df.columns:
    df["category"] = df["category"].str.strip().str.title()  
    # Viết hoa chữ cái đầu mỗi từ

# ======================
# 6. XỬ LÝ GIÁ TRỊ THIẾU
# ======================
print("\nMissing trước khi xử lý:")
print(df.isnull().sum())   # Đếm số giá trị bị thiếu

df = df.dropna()   # Xóa tất cả dòng có giá trị thiếu

# ======================
# 7. LỌC DỮ LIỆU HỢP LỆ
# ======================
df = df[(df["age"] >= 18) & (df["age"] <= 100)]  
# Giữ tuổi hợp lệ (18–100)

df = df[df["purchase_amount_usd"] > 0]  
# Giữ giá trị chi tiêu > 0

# ======================
# 8. XỬ LÝ OUTLIER (IQR)
# ======================
Q1 = df["purchase_amount_usd"].quantile(0.25)   # Tính Q1 (25%)
Q3 = df["purchase_amount_usd"].quantile(0.75)   # Tính Q3 (75%)
IQR = Q3 - Q1   # Khoảng tứ phân vị

lower = Q1 - 1.5 * IQR   # Ngưỡng dưới
upper = Q3 + 1.5 * IQR   # Ngưỡng trên

df = df[(df["purchase_amount_usd"] >= lower) &
        (df["purchase_amount_usd"] <= upper)]  
# Loại bỏ giá trị ngoại lai

# ======================
# 9. RESET INDEX
# ======================
df = df.reset_index(drop=True)  
# Đánh lại số thứ tự từ 0

# ======================
# 10. KIỂM TRA SAU CLEAN
# ======================
print("\n===== SAU CLEAN =====")
print(df.info())   # Kiểm tra lại dữ liệu sau khi làm sạch
print("Shape:", df.shape)   # Kích thước cuối

# ======================
# 11. LƯU FILE
# ======================
df.to_csv("shopping_cleaned.csv", index=False)  
# Lưu dữ liệu sạch ra file CSV mới

print("\n✅ Đã lưu file: shopping_cleaned.csv")
