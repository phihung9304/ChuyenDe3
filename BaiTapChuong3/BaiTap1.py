import pandas as pd
import matplotlib.pyplot as plt

# 🔹 1. Đọc file CSV
df = pd.read_csv(r"E:\ChuyenDe3\Chuong3\BaiTapChuong2\students_cleaned_final.csv")

# print("Shape của DataFrame:", df.shape)  # số dòng và số cột

# df.info()  # kiểu dữ liệu, số giá trị không null

# Bài 2

# city_counts = df['City'].value_counts()
# class_counts = df['Class'].value_counts()
# print("Số lượng sinh viên theo City:")
# print(city_counts)
# print("\nSố lượng sinh viên theo Class:")
# print(class_counts)

# Bài 3

# city_counts = df['City'].value_counts()
# class_counts = df['Class'].value_counts()

# plt.figure(figsize=(8,5))
# plt.bar(city_counts.index, city_counts.values, color='skyblue', edgecolor='black')
# plt.title("Số lượng sinh viên theo City", fontsize=14, fontweight='bold')
# plt.xlabel("City", fontsize=12)
# plt.ylabel("Số sinh viên", fontsize=12)

# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,5))
# plt.bar(class_counts.index, class_counts.values, color='skyblue', edgecolor='black')
# plt.title("Số lượng sinh viên theo Class", fontsize=14, fontweight='bold')
# plt.xlabel("Class", fontsize=12)
# plt.ylabel("Số sinh viên", fontsize=12)

# plt.tight_layout()
# plt.show()

# Bài 4
# plt.figure(figsize=(8,5))
# plt.hist(df['Score'], bins=15, color='skyblue', edgecolor='black')
# plt.title("Phổ điểm học sinh (Score)", fontsize=14, fontweight='bold')
# plt.xlabel("Điểm", fontsize=12)
# plt.ylabel("Số học sinh", fontsize=12)

# plt.tight_layout()
# plt.show()

# Bài 5:
# mean_score_city = df.groupby('City')['Score'].mean()
# plt.figure(figsize=(8,5))
# plt.bar(mean_score_city.index, mean_score_city.values, color='skyblue', edgecolor='black')
# plt.title("Điểm trung bình theo City", fontsize=14, fontweight='bold')
# plt.xlabel("City", fontsize=12)
# plt.ylabel("Điểm trung bình", fontsize=12)
# plt.tight_layout()
# plt.show()

# Bài 6:
# plt.figure(figsize=(8,5))
# plt.scatter(df['Age'], df['Score'], color='skyblue', edgecolor='black')
# plt.title("Scatter plot: Tuổi vs Điểm", fontsize=14, fontweight='bold')
# plt.xlabel("Tuổi", fontsize=12)
# plt.ylabel("Score", fontsize=12)

# plt.grid(True, linestyle='--', alpha=0.5)  # thêm lưới
# plt.tight_layout()
# plt.show()

# Bài 7:
# mean_total_class = df.groupby('Class')['Total'].mean()

# plt.figure(figsize=(8,5))
# plt.bar(mean_total_class.index, mean_total_class.values, color='skyblue', edgecolor='black')
# plt.title("Tổng điểm trung bình theo Class", fontsize=14, fontweight='bold')
# plt.xlabel("Class", fontsize=12)
# plt.ylabel("Tổng điểm trung bình", fontsize=12)
# plt.tight_layout()
# plt.show()

# Bài 8:
# def grade_class(score):
#     if score >= 9:
#         return 'A'
#     elif score >= 8:
#         return 'B'
#     elif score >= 7:
#         return 'C'
#     elif score >= 6:
#         return 'D'
#     else:
#         return 'F'

# df['Grade'] = df['Score'].apply(grade_class)

# grade_counts = df['Grade'].value_counts().sort_index()
# plt.figure(figsize=(8,5))
# plt.bar(grade_counts.index, grade_counts.values, color='skyblue', edgecolor='black')
# plt.title("Số lượng sinh viên theo Grade", fontsize=14, fontweight='bold')
# plt.xlabel("Grade", fontsize=12)
# plt.ylabel("Số lượng sinh viên", fontsize=12)


# plt.tight_layout()
# plt.show()