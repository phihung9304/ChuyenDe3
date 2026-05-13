import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def chay_phan_tich_insight():
    # --- 1. FIX LỖI ĐƯỜNG DẪN TRÊN MAC ---
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # --- 2. NẠP DỮ LIỆU ---
    file_name = "shopping_cleaned.csv"
    if not os.path.exists(file_name):
        print(f"❌ Không tìm thấy {file_name}. Hãy chạy DATACLEANING.py trước!")
        return

    df = pd.read_csv(file_name)
    # Chuẩn hóa tên cột gốc để xử lý
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    sns.set_theme(style="whitegrid")

    # Tạo thư mục đầu ra
    for folder in ["outputcsv", "outputpng"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # =========================================================
    # PHẦN 1: PHÂN TÍCH INSIGHTS (TRỰC QUAN HÓA)
    # =========================================================
    print("--- Đang thực hiện phân tích Insights... ---")

    # Insight 1: Doanh thu theo Mùa và Giới tính
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='season', y='purchase_amount_usd', hue='gender', estimator=sum, palette='coolwarm')
    plt.title('Tổng Doanh Thu Theo Mùa và Giới Tính', fontsize=14, fontweight='bold')
    plt.xlabel('Mùa')
    plt.ylabel('Tổng Chi Tiêu (USD)')
    plt.savefig(os.path.join("outputpng", "doanh_thu_theo_mua.png"))
    plt.close()

    # Insight 2: Phân bố đánh giá theo danh mục
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='category', y='review_rating', palette='Set3')
    plt.title('Phân Bố Điểm Đánh Giá Theo Danh Mục Hàng Hóa', fontsize=14)
    plt.xlabel('Danh Mục')
    plt.ylabel('Điểm Đánh Giá')
    plt.savefig(os.path.join("outputpng", "phan_bo_danh_gia.png"))
    plt.close()

    # =========================================================
    # PHẦN 2: TRÍCH XUẤT ĐẶC TRƯNG QUAN TRỌNG
    # =========================================================
    print("--- Đang xác định các yếu tố ảnh hưởng... ---")

    ml_df = df.copy()
    le = LabelEncoder()
    for col in ['gender', 'category', 'season', 'subscription_status']:
        if col in ml_df.columns:
            ml_df[col] = le.fit_transform(ml_df[col].astype(str))

    features = ['age', 'gender', 'purchase_amount_usd', 'review_rating', 'previous_purchases']
    X = ml_df[features]
    y = ml_df['subscription_status']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Tạo bảng kết quả với tiêu đề cột tiếng Việt
    importance_df = pd.DataFrame({
        'Yếu tố ảnh hưởng': ['Tuổi tác', 'Giới tính', 'Số tiền chi tiêu', 'Điểm đánh giá', 'Số lần mua trước'],
        'Mức độ quan trọng (%)': model.feature_importances_ * 100
    }).sort_values(by='Mức độ quan trọng (%)', ascending=False)

    # Xuất CSV tiếng Việt (utf-8-sig để Excel không lỗi font)
    csv_path = os.path.join("outputcsv", "yeu_to_anh_huong_khach_hang.csv")
    importance_df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    # Vẽ biểu đồ mức độ quan trọng bằng tiếng Việt
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Mức độ quan trọng (%)', y='Yếu tố ảnh hưởng', palette='viridis')
    plt.title('Các Yếu Tố Ảnh Hưởng Đến Quyết Định Đăng Ký Hội Viên')
    plt.savefig(os.path.join("outputpng", "yeu_to_quan_trong_insight.png"))
    plt.close()

    print("\n" + "="*40)
    print("✅ HOÀN TẤT PHÂN TÍCH INSIGHT!")
    print(f"1. File CSV đã Việt hóa: {csv_path}")
    print("2. Các biểu đồ tiếng Việt đã lưu vào folder: outputpng")
    print("="*40)

if __name__ == "__main__":
    chay_phan_tich_insight()