import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def run_full_analysis():
    # --- BƯỚC CHUẨN BỊ THƯ MỤC ---
    # Tự động tạo thư mục nếu chưa tồn tại để tránh lỗi "Folder not found"
    for folder in ["outputcsv", "outputpng"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # --- NẠP DỮ LIỆU ---
    df = pd.read_csv("shopping_cleaned.csv")
    sns.set_theme(style="whitegrid")

    # =========================================================
    # PHẦN 1: PHÂN TÍCH INSIGHTS (LƯU VÀO outputpng)
    # =========================================================
    print("--- Đang thực hiện phân tích Insights... ---")

    # Insight 1: Doanh thu theo Mùa và Giới tính
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='season', y='purchase_amount_usd', hue='gender', estimator=sum, palette='coolwarm')
    plt.title('Tổng doanh thu theo Mùa và Giới tính', fontsize=14, fontweight='bold')
    plt.savefig(os.path.join("outputpng", "doanh_thu_theo_mua.png")) # Lưu vào thư mục outputpng
    plt.close()

    # Insight 2: Mức độ hài lòng của Hội viên
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='subscription_status', y='review_rating', palette='Set2')
    plt.title('Mức độ hài lòng: Hội viên vs Khách thường')
    plt.savefig(os.path.join("outputpng", "danh_gia_theo_hoi_vien.png"))
    plt.close()

    # Insight 3: Phương thức thanh toán theo nhóm tuổi
    df['age_group'] = pd.cut(df['age'], bins=[18, 30, 45, 60, 75], labels=['18-30', '31-45', '46-60', '60+'])
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='age_group', hue='preferred_payment_method')
    plt.title('Phương thức thanh toán theo nhóm độ tuổi')
    plt.savefig(os.path.join("outputpng", "thanh_toan_theo_do_tuoi.png"))
    plt.close()

    # =========================================================
    # PHẦN 2: MODELING (LƯU CSV VÀ PNG VÀO ĐÚNG THƯ MỤC)
    # =========================================================
    print("--- Đang huấn luyện mô hình dự đoán... ---")

    ml_df = df.copy()
    le = LabelEncoder()
    for col in ['gender', 'category', 'season', 'subscription_status']:
        ml_df[col] = le.fit_transform(ml_df[col])

    features = ['age', 'gender', 'purchase_amount_usd', 'review_rating', 'previous_purchases']
    X = ml_df[features]
    y = ml_df['subscription_status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    importance_df = pd.DataFrame({
        'Yếu tố': features,
        'Mức độ ảnh hưởng': model.feature_importances_
    }).sort_values(by='Mức độ ảnh hưởng', ascending=False)

    # Lưu kết quả CSV vào outputcsv
    importance_df.to_csv(os.path.join("outputcsv", "ket_qua_du_doan_quan_trong.csv"), index=False)

    # Vẽ và lưu biểu đồ vào outputpng
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Mức độ ảnh hưởng', y='Yếu tố', palette='viridis')
    plt.title('Các yếu tố quyết định khả năng đăng ký Hội viên')
    plt.savefig(os.path.join("outputpng", "cac_yeu_to_anh_huong.png"))
    plt.close()

    print("\n✅ TẤT CẢ HOÀN TẤT!")
    print(f"-> Hình ảnh đã lưu trong: outputpng/")
    print(f"-> File dữ liệu đã lưu trong: outputcsv/")

if __name__ == "__main__":
    run_full_analysis()