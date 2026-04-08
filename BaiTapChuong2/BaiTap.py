import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Bài 1: Đọc và khám phá dữ liệu
# =========================
df = pd.read_csv(r"E:\ChuyenDe3\Chuong3\BaiTap\students_performance.csv")

print("===== 5 dòng đầu =====")
print(df.head())

print("\n===== Thông tin dữ liệu =====")
print(df.info())

print("\n===== Thống kê mô tả =====")
print(df.describe())


# =========================
# Bài 2: Làm sạch dữ liệu
# =========================

# Ép kiểu
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Score"] = pd.to_numeric(df["Score"], errors="coerce")

# Xử lý missing
df = df.fillna({
    "Age": df["Age"].mean(),
    "Score": df["Score"].mean(),
    "City": "UNKNOWN"
})

print("\n===== Missing sau xử lý =====")
print(df.isnull().sum())


# =========================
# Bài 3: Chuẩn hóa dữ liệu
# =========================
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.upper()
df["Class"] = df["Class"].str.strip().str.upper()


# =========================
# Xóa duplicate
# =========================
df = df.drop_duplicates(subset=["Name","Age","Score","City","Bonus","Class"])

print("\n===== Sau khi làm sạch & chuẩn hóa =====")
print(df)


# =========================
# Bài 4: Feature Engineering
# =========================

# Total
df["Total"] = df["Score"] + df["Bonus"]

# Chuẩn hóa Score
df["Score_norm"] = (df["Score"] - df["Score"].min()) / (df["Score"].max() - df["Score"].min())

print("\n===== Sau khi tạo biến mới =====")
print(df)


# =========================
# Bài 5: Phân tích dữ liệu
# =========================

print("\n===== Theo City =====")
print("Mean Score:")
print(df.groupby("City")["Score"].mean())

print("\nSố lượng sinh viên:")
print(df.groupby("City")["ID"].count())

print("\n===== Theo Class =====")
print("Mean Score:")
print(df.groupby("Class")["Score"].mean())

print("\nMax Score:")
print(df.groupby("Class")["Score"].max())

print("\n===== Top 3 Total cao nhất =====")
top3 = df.sort_values(by="Total", ascending=False).head(3)
print(top3[["Name", "Total", "Class", "City"]])


# =========================
# Bài 6: Outliers
# =========================
print("\n===== Dữ liệu bất thường =====")
outliers = df[(df["Score"] > 9.5) | (df["Score"] < 5)]
print(outliers[["ID","Name","Score","Class","City"]])


# =========================
# Bài 7: Trực quan hóa
# =========================
city_counts = df["City"].value_counts()

print("\n===== Số lượng sinh viên theo City =====")
print(city_counts)

plt.figure()
city_counts.plot(kind="bar")
plt.title("So luong sinh vien theo City")
plt.xlabel("City")
plt.ylabel("So luong")
plt.show()


# =========================
# Bài 8: Kết quả
# =========================

print("\n===== DataFrame sau xử lý =====")
print(df)

print("\n===== Mean Score theo City =====")
print(df.groupby("City")["Score"].mean())

print("\n===== Số lượng sinh viên theo City =====")
print(df.groupby("City")["ID"].count())

# =========================
# Bài 9: Lưu dữ liệu
# =========================

df.to_csv(r"E:\ChuyenDe3\Chuong3\BaiTap\students_cleaned_final.csv", index=False)
print("\n===== Đã lưu file students_cleaned_final.csv =====")

