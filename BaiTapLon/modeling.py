import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def run_modeling():
    # --- BƯỚC 1: NẠP DỮ LIỆU ---
    # Đọc file dữ liệu đã làm sạch
    df = pd.read_csv("shopping_cleaned.csv")
    print("--- Đang huấn luyện mô hình dự đoán Hội viên... ---")

    # --- BƯỚC 2: TIỀN XỬ LÝ (DATA PREPROCESSING) ---
    # Tạo một bản sao để xử lý, tránh làm hỏng dữ liệu gốc (df)
    ml_df = df.copy()
    
    # LabelEncoder: Chuyển đổi các cột dạng chữ (Male, Female, Clothing...) thành số (0, 1, 2...)
    # Vì thuật toán máy học (Random Forest) không thể đọc trực tiếp chữ cái
    le = LabelEncoder()
    for col in ['gender', 'category', 'season', 'subscription_status']:
        ml_df[col] = le.fit_transform(ml_df[col])

    # --- BƯỚC 3: CHỌN ĐẶC TRƯNG (FEATURE SELECTION) ---
    # features (X): Các yếu tố dùng để dự đoán (Độ tuổi, Giới tính, Số tiền chi tiêu...)
    features = ['age', 'gender', 'purchase_amount_usd', 'review_rating', 'previous_purchases']
    X = ml_df[features]
    
    # target (y): Kết quả muốn dự đoán (Khách hàng có là Hội viên hay không)
    y = ml_df['subscription_status']

    # --- BƯỚC 4: CHIA DỮ LIỆU TRAIN/TEST ---
    # test_size=0.2: Giữ lại 20% dữ liệu để kiểm tra (Test), dùng 80% để dạy máy học (Train)
    # random_state=42: Đảm bảo kết quả giống nhau mỗi lần Duy chạy code
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- BƯỚC 5: HUẤN LUYỆN MÔ HÌNH (TRAINING MODEL) ---
    # Sử dụng Random Forest (Rừng ngẫu nhiên) - một thuật toán rất mạnh để phân loại
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train) # Máy bắt đầu học các quy luật từ X_train và y_train

    # --- BƯỚC 6: PHÂN TÍCH ĐỘ QUAN TRỌNG (FEATURE IMPORTANCE) ---
    # model.feature_importances_: Trả về điểm số xem yếu tố nào ảnh hưởng nhất đến kết quả dự đoán
    importance_df = pd.DataFrame({
        'Yếu tố': features,
        'Mức độ ảnh hưởng': model.feature_importances_
    }).sort_values(by='Mức độ ảnh hưởng', ascending=False)

    # --- BƯỚC 7: XUẤT KẾT QUẢ RA THƯ MỤC CHÍNH (PRINT OUT) ---
    # Lưu bảng điểm quan trọng ra file CSV ngay tại thư mục BaitapLon
    importance_df.to_csv("ket_qua_du_doan_quan_trong.csv", index=False)

    # Vẽ biểu đồ cột để minh họa các yếu tố ảnh hưởng
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Mức độ ảnh hưởng', y='Yếu tố', palette='viridis')
    plt.title('Yếu tố quyết định khách hàng trung thành')
    
    # Lưu ảnh biểu đồ ra thư mục chính
    plt.savefig("cac_yeu_to_anh_huong.png")
    plt.close() # Giải phóng bộ nhớ máy tính

    print(f"✅ Modeling thành công!")
    print(f"-> File CSV đã lưu: ket_qua_du_doan_quan_trong.csv")
    print(f"-> Biểu đồ đã lưu: cac_yeu_to_anh_huong.png")

if __name__ == "__main__":
    run_modeling()