import pandas as pd
import matplotlib.pyplot as plt

# 🔹 1. Đọc file CSV
df = pd.read_csv(r"E:\ChuyenDe3\Chuong3\BaiTapChuong3-2\students_cleaned_final.csv")

# print("Shape của DataFrame:", df.shape)  # số dòng và số cột

# print("\nThông tin về DataFrame:")
# print(df.info())

# print("\nKiểm tra Missing Values:") # kiếm tra có NaN không
# print(df.isnull().sum())

# # 4. Thống kê mô tả các cột số
# print("\nThống kê mô tả:")
# print(df.describe())

# Bài 2

# SL_city = df['City'].value_counts()
# SL_class = df['Class'].value_counts()
# print("Số lượng sinh viên theo City:")
# print(SL_city)
# print("\nSố lượng sinh viên theo Class:")
# print(SL_class)


# plt.figure(figsize=(8,5))

# plt.bar(SL_city.index, SL_city.values, color='skyblue', edgecolor='black')

# plt.title("Số lượng sinh viên theo City", fontsize=14, fontweight='bold')

# plt.xlabel("City", fontsize=12)
# plt.ylabel("Số sinh viên", fontsize=12)

# plt.show()

# Bài 3
# plt.figure(figsize=(8,5))

# plt.hist(df['Score'], bins=6, color='skyblue', edgecolor='black')

# plt.title("Phổ điểm học sinh (Score)", fontsize=14, fontweight='bold')

# plt.xlabel("Điểm", fontsize=12)
# plt.ylabel("Số học sinh", fontsize=12)

# plt.show()

# Bài 4:
# mean_score_city = df.groupby('City')['Score'].mean()
# mean_score_class = df.groupby('Class')['Total'].mean()

# plt.figure(figsize=(8,5))
# plt.bar(mean_score_city.index, mean_score_city.values, color='skyblue', edgecolor='black')
# plt.title("Điểm trung bình theo City", fontsize=14, fontweight='bold')
# plt.xlabel("City", fontsize=12)
# plt.ylabel("Điểm trung bình", fontsize=12)
# plt.show()

# plt.figure(figsize=(8,5))
# plt.bar(mean_score_class.index, mean_score_class.values, color='skyblue', edgecolor='black')
# plt.title("Điểm trung bình theo Class", fontsize=14, fontweight='bold')
# plt.xlabel("Class", fontsize=12)
# plt.ylabel("Điểm trung bình", fontsize=12)
# plt.show()

# Bài 5:
# plt.figure(figsize=(8,5))
# plt.scatter(df['Age'], df['Score'], color='skyblue', edgecolor='black')
# plt.title("Scatter plot: Tuổi vs Điểm", fontsize=14, fontweight='bold')
# plt.xlabel("Tuổi", fontsize=12)
# plt.ylabel("Score", fontsize=12)

# plt.grid(True)
# plt.show()

# Bài 6:
# def grade_class(Total):
#     if Total >= 10:
#         return 'A'
#     elif Total >= 9:
#         return 'B'
#     elif Total >= 8:
#         return 'C'
#     elif Total >= 7:
#         return 'D'
#     else:
#         return 'F'

# df['Grade'] = df['Total'].apply(grade_class)

# grade_counts = df['Grade'].value_counts().sort_index()
# plt.figure(figsize=(8,5))
# plt.bar(grade_counts.index, grade_counts.values, color='skyblue', edgecolor='black')
# plt.title("Số lượng sinh viên theo Grade", fontsize=14, fontweight='bold')
# plt.xlabel("Grade", fontsize=12)
# plt.ylabel("Số lượng sinh viên", fontsize=12)

# plt.show()

# Bài 7:
# corr = ['Age', 'Score', 'Bonus', 'Total']
# correlation = df[corr].corr()

# print("Ma trận tương quan:")
# print(correlation)

# top5_SV = df.sort_values(by='Total', ascending=False).head(5) #df.sort_values sắp xếp giá trị theo total, ascending=False giảm dần
# print("Top 5 sinh viên điểm cao nhất dựa theo Total:")
# print(top5_SV[['ID', 'Name', 'Class', 'Score', 'Bonus', 'Total']])

# missing = df.isnull().sum() #df.isnull() kiểm tra dữ liệu NaN, sum() tính tổng số giá trị thiếu theo cột
# print("Số giá trị thiếu theo cột:")
# print(missing)

