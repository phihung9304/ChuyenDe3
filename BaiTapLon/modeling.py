import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, classification_report, 
                             confusion_matrix, roc_auc_score)

def chay_mo_hinh():
    # --- 1. ĐỊNH VỊ THƯ MỤC (CHỐNG LỖI ĐƯỜNG DẪN) ---
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    du_lieu_file = "shopping_cleaned.csv"
    if not os.path.exists(du_lieu_file):
        print(f"❌ Không tìm thấy file: {du_lieu_file}")
        return

    # --- 2. ĐỌC VÀ CHUẨN HÓA DỮ LIỆU ---
    df = pd.read_csv(du_lieu_file)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    ml_df = df.copy()
    le = LabelEncoder()
    # Mã hóa các cột phân loại
    cac_cot_chu = ['gender', 'category', 'season', 'subscription_status']
    for cot in cac_cot_chu:
        if cot in ml_df.columns:
            ml_df[cot] = le.fit_transform(ml_df[cot].astype(str))

    # Chọn các yếu tố dự đoán
    bien_doc_lap = ['age', 'purchase_amount_usd', 'review_rating', 'previous_purchases', 'gender']
    bien_muc_tieu = 'subscription_status'

    X = ml_df[bien_doc_lap]
    y = ml_df[bien_muc_tieu]

    # Chia dữ liệu: 80% huấn luyện, 20% kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # --- 3. HUẤN LUYỆN MÔ HÌNH RANDOM FOREST ---
    print("\n--- Đang huấn luyện mô hình dự đoán Hội viên... ---")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # --- 4. TỔNG HỢP CHỈ SỐ ĐÁNH GIÁ ---
    y_pred = rf.predict(X_test)
    y_proba = rf.predict_proba(X_test)[:, 1]
    
    # Tạo báo cáo chi tiết bằng tiếng Việt
    print("\n" + "="*40)
    print("BÁO CÁO KẾT QUẢ MÔ HÌNH")
    print("="*40)
    
    # Xuất báo cáo ra dataframe để lưu CSV tiếng Việt
    bao_cao_dict = classification_report(y_test, y_pred, output_dict=True)
    bao_cao_df = pd.DataFrame(bao_cao_dict).transpose()
    bao_cao_df.columns = ['Độ chính xác (Precision)', 'Độ bao phủ (Recall)', 'Điểm F1', 'Số mẫu (Support)']
    
    # In ra màn hình console
    print(f"Độ chính xác tổng thể (Accuracy): {accuracy_score(y_test, y_pred):.4f}")
    print(f"Chỉ số ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}")

    # Kiểm tra chéo (Cross-Validation)
    kiem_tra_cheo = cross_val_score(rf, X, y, cv=5)
    print(f"Độ ổn định trung bình (Cross-Val): {kiem_tra_cheo.mean():.4f}")

    # --- 5. XUẤT KẾT QUẢ (CSV & BIỂU ĐỒ) ---
    if not os.path.exists("outputcsv"): os.makedirs("outputcsv")
    if not os.path.exists("outputpng"): os.makedirs("outputpng")

    # Lưu file CSV báo cáo (Dùng encoding utf-8-sig để Excel không lỗi font tiếng Việt)
    bao_cao_df.to_csv("outputcsv/bao_cao_mo_hinh.csv", encoding="utf-8-sig")
    
    # Vẽ Ma trận nhầm lẫn
    plt.figure(figsize=(7, 6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title('Ma Trận Nhầm Lẫn (Confusion Matrix)')
    plt.ylabel('Thực tế')
    plt.xlabel('Dự đoán')
    plt.savefig("outputpng/ma_tran_nham_lan.png")
    
    # Vẽ Tầm quan trọng của các yếu tố
    plt.figure(figsize=(10, 6))
    bien_quan_trong = pd.Series(rf.feature_importances_, index=['Tuổi', 'Số tiền mua', 'Đánh giá', 'Lần mua trước', 'Giới tính'])
    bien_quan_trong.sort_values().plot(kind='barh', color='teal')
    plt.title('Các yếu tố ảnh hưởng nhất đến đăng ký Hội viên')
    plt.xlabel('Mức độ ảnh hưởng')
    plt.savefig("outputpng/yeu_to_quan_trong.png")

    print("\n✅ HOÀN TẤT! Kết quả đã được dịch sang tiếng Việt và lưu tại:")
    print("- CSV: outputcsv/bao_cao_mo_hinh.csv")
    print("- Ảnh: outputpng/ma_tran_nham_lan.png và yeu_to_quan_trong.png")

if __name__ == "__main__":
    chay_mo_hinh()