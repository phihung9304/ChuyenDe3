import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_insights():
    # Khởi tạo thư mục
    png_dir = "outputpng"
    if not os.path.exists(png_dir): os.makedirs(png_dir)

    # Load dữ liệu
    df = pd.read_csv("shopping_cleaned.csv")
    sns.set_theme(style="whitegrid")

    print("--- Đang phân tích Insights sâu... ---")

    # Insight 1: Doanh thu theo mùa và Giới tính
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='season', y='purchase_amount_usd', hue='gender', estimator=sum, palette='coolwarm')
    plt.title('Tổng doanh thu theo Mùa và Giới tính', fontsize=14, fontweight='bold')
    # ĐỔI TÊN: insight_seasonal_revenue.png -> doanh_thu_theo_mua.png
    plt.savefig(os.path.join(png_dir, "doanh_thu_theo_mua.png"))
    plt.close()

    # Insight 2: Điểm đánh giá (Rating) theo Hội viên
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='subscription_status', y='review_rating', palette='Set2')
    plt.title('Sự khác biệt về Điểm đánh giá giữa Hội viên và Khách thường')
    # ĐỔI TÊN: insight_rating_by_sub.png -> danh_gia_theo_hoi_vien.png
    plt.savefig(os.path.join(png_dir, "danh_gia_theo_hoi_vien.png"))
    plt.close()

    # Insight 3: Phương thức thanh toán theo độ tuổi
    df['age_group'] = pd.cut(df['age'], bins=[18, 30, 45, 60, 75], labels=['18-30', '31-45', '46-60', '60+'])
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='age_group', hue='preferred_payment_method')
    plt.title('Phương thức thanh toán theo nhóm độ tuổi')
    plt.legend(title='Thanh toán', bbox_to_anchor=(1.05, 1), loc='upper left')
    # ĐỔI TÊN: insight_payment_by_age.png -> thanh_toan_theo_do_tuoi.png
    plt.savefig(os.path.join(png_dir, "thanh_toan_theo_do_tuoi.png"))
    plt.close()

    print(f"✅ Đã lưu các biểu đồ vào thư mục: {png_dir}")

if __name__ == "__main__":
    generate_insights()