import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def run_full_analysis():
    # --- NẠP DỮ LIỆU ---
    # Đọc file dữ liệu sạch từ thư mục hiện tại
    df = pd.read_csv("shopping_cleaned.csv")
    sns.set_theme(style="whitegrid")

    # =========================================================
    # PHẦN 1: PHÂN TÍCH INSIGHTS (LƯU THẲNG RA NGOÀI)
    # =========================================================
    print("--- Đang thực hiện phân tích Insights... ---")

    # Insight 1: Doanh thu theo Mùa và Giới tính
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='season', y='purchase_amount_usd', hue='gender', estimator=sum, palette='coolwarm')
    plt.title('Tổng doanh thu theo Mùa và Giới tính', fontsize=14, fontweight='bold')
    # Lưu trực tiếp vào thư mục hiện tại (BaitapLon)
    plt.savefig("doanh_thu_theo_mua.png")
    plt.close()

    # Insight 2: Mức độ hài lòng của Hội viên
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='subscription_status', y='review_rating', palette='Set2')
    plt.title('Mức độ hài lòng: Hội viên vs Khách thường')
    plt.savefig("danh_gia_theo_hoi_vien.png")
    plt.close()

    # Insight 3: Phương thức thanh toán theo nhóm tuổi
    df['age_group'] = pd.cut(df['age'], bins=[18, 30, 45, 60, 75], labels=['18-30', '31-45', '46-60', '60+'])
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='age_group', hue='preferred_payment_method')
    plt.title('Phương thức thanh toán theo nhóm độ tuổi')
    plt.savefig("thanh_toan_theo_do_tuoi.png")
    plt.close()

    # =========================================================
    # PHẦN 2: MODELING (DỰ ĐOÁN & LƯU CSV RA NGOÀI)
    # =========================================================
    print("--- Đang huấn luyện mô hình dự đoán... ---")

    ml_df = df.copy()
    le = LabelEncoder()
    
    # Mã hóa dữ liệu sang số để máy học
    for col in ['gender', 'category', 'season', 'subscription_status']:
        ml_df[col] = le.fit_transform(ml_df[col])

    features = ['age', 'gender', 'purchase_amount_usd', 'review_rating', 'previous_purchases']
    X = ml_df[features]
    y = ml_df['subscription_status']

    # Huấn luyện Model Random Forest
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Tính toán mức độ quan trọng của các yếu tố
    importance_df = pd.DataFrame({
        'Yếu tố': features,
        'Mức độ ảnh hưởng': model.feature_importances_
    }).sort_values(by='Mức độ ảnh hưởng', ascending=False)

    # Lưu kết quả CSV thẳng ra ngoài thư mục chính
    importance_df.to_csv("ket_qua_du_doan_quan_trong.csv", index=False)

    # Vẽ biểu đồ mức độ quan trọng
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Mức độ ảnh hưởng', y='Yếu tố', palette='viridis')
    plt.title('Các yếu tố quyết định khả năng đăng ký Hội viên')
    plt.savefig("cac_yeu_to_anh_huong.png")
    plt.close()

    print("\n✅ TẤT CẢ HOÀN TẤT!")
    print("Mọi file ảnh (.png) và bảng biểu (.csv) đã được lưu tại thư mục chính.")

if __name__ == "__main__":
    run_full_analysis()