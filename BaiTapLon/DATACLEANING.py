import pandas as pd
import matplotlib.pyplot as plt
# ======================
# 1. LOAD DATA
# ======================
df = pd.read_csv("shopping_trends.csv")

# ======================
# 2. DATA CLEANING
# ======================
# Kiểm tra dữ liệu thiếu
# True thiếu, False không thiếu, sum gộp lại số lượng thiếu theo cột
print("Dữ liệu thiếu:")
print(df.isnull().sum())

# Xóa dữ liệu trùng
df = df.drop_duplicates()

# Chuẩn hóa tên cột: loại bỏ khoảng trắng, chuyển thành chữ thường, thay thế khoảng trắng bằng dấu gạch dưới
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
# Kiểm tra lại tên cột sau khi chuẩn hóa
print("\nShape sau khi chuẩn hóa:", df.shape)

df.to_csv("shopping_cleaned.csv", index=False)





