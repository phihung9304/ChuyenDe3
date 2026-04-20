import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def run_modeling():
    # --- BƯỚC 1: NẠP DỮ LIỆU ---
    df = pd.read_csv("shopping_cleaned.csv")
    print("--- Đang huấn luyện mô hình dự đoán Hội viên... ---")

    # --- BƯỚC 2: TIỀN XỬ LÝ (DATA PREPROCESSING) ---
    ml_df = df.copy()
    le = LabelEncoder()
    for col in ['gender', 'category', 'season', 'subscription_status']:
        ml_df[col] = le.fit_transform(ml_df[col])

    # --- BƯỚC 3: CHỌN ĐẶC TRƯNG (FEATURE SELECTION) ---
    features = ['age', 'gender', 'purchase_amount_usd', 'review_rating', 'previous_purchases']
    X = ml_df[features]
    y = ml_df['subscription_status']

    # --- BƯỚC 4: CHIA DỮ LIỆU TRAIN/TEST ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- BƯỚC 5: HUẤN LUYỆN MÔ HÌNH ---
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # --- BƯỚC 6: PHÂN TÍCH ĐỘ QUAN TRỌNG ---
    importance_df = pd.DataFrame({
        'Yếu tố': features,
        'Mức độ ảnh hưởng': model.feature_importances_
    }).sort_values(by='Mức độ ảnh hưởng', ascending=False)

    # --- BƯỚC 7: XUẤT KẾT QUẢ VÀO THƯ MỤC CỤ THỂ ---
    
    # Tạo thư mục nếu chưa tồn tại để tránh lỗi
    if not os.path.exists("outputcsv"):
        os.makedirs("outputcsv")
    if not os.path.exists("outputpng"):
        os.makedirs("outputpng")

    # 1. Lưu file CSV vào thư mục outputcsv
    csv_path = os.path.join("outputcsv", "ket_qua_du_doan_quan_trong.csv")
    importance_df.to_csv(csv_path, index=False)

    # 2. Vẽ và lưu biểu đồ vào thư mục outputpng
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Mức độ ảnh hưởng', y='Yếu tố', palette='viridis')
    plt.title('Yếu tố quyết định khách hàng trung thành')
    
    png_path = os.path.join("outputpng", "cac_yeu_to_anh_huong.png")
    plt.savefig(png_path)
    plt.close()

    print(f"✅ Modeling thành công!")
    print(f"-> File CSV đã lưu: {csv_path}")
    print(f"-> Biểu đồ đã lưu: {png_path}")

if __name__ == "__main__":
    run_modeling()