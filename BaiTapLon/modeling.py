import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, classification_report, 
                             confusion_matrix, roc_auc_score, RocCurveDisplay)

def chay_mo_hinh_chuyen_nghiep():
    # --- 1. ĐỊNH VỊ THƯ MỤC & NẠP DỮ LIỆU ---
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file_path = "shopping_cleaned.csv"
    
    if not os.path.exists(file_path):
        print(f"❌ Không tìm thấy file {file_path}. Vui lòng chạy DATACLEANING.py trước.")
        return

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # --- 2. TIỀN XỬ LÝ & CHIẾN LƯỢC CHIA DỮ LIỆU ---
    ml_df = df.copy()
    le = LabelEncoder()
    cat_cols = ['gender', 'category', 'season', 'subscription_status']
    for col in cat_cols:
        if col in ml_df.columns:
            ml_df[col] = le.fit_transform(ml_df[col].astype(str))

    features = ['age', 'purchase_amount_usd', 'review_rating', 'previous_purchases', 'gender']
    X = ml_df[features]
    y = ml_df['subscription_status']

    # Sử dụng stratify=y để đảm bảo tỷ lệ Hội viên/Khách thường đồng nhất ở 2 tập
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # --- 3. MODEL COMPARISON & BENCHMARK ---
    print("\n" + "="*50)
    print("BƯỚC 1: SO SÁNH MÔ HÌNH (BENCHMARK)")
    print("="*50)
    
    models = {
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Logistic Regression (Baseline)": LogisticRegression(max_iter=1000)
    }

    results = []
    for name, model in models.items():
        # Huấn luyện
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        # Kiểm tra chéo (Cross-Validation)
        cv_scores = cross_val_score(model, X, y, cv=5)
        
        print(f"[{name}] Accuracy: {acc:.4f} | CV Accuracy: {cv_scores.mean():.4f}")
        results.append({"Model": name, "Accuracy": acc, "CV_Mean": cv_scores.mean()})

    # --- 4. ĐÁNH GIÁ CHI TIẾT (ACCURACY, PRECISION, RECALL, F1, ROC-AUC) ---
    print("\n" + "="*50)
    print("BƯỚC 2: CHỈ SỐ CHỨNG MINH HIỆU NĂNG (RANDOM FOREST)")
    print("="*50)
    
    rf_model = models["Random Forest"]
    y_pred_rf = rf_model.predict(X_test)
    y_proba_rf = rf_model.predict_proba(X_test)[:, 1]

    # In báo cáo chi tiết
    print(classification_report(y_test, y_pred_rf, target_names=['Khách thường', 'Hội viên']))
    print(f"Chỉ số ROC-AUC: {roc_auc_score(y_test, y_proba_rf):.4f}")

    # --- 5. XUẤT KẾT QUẢ (CSV & PNG) ---
    if not os.path.exists("outputcsv"): os.makedirs("outputcsv")
    if not os.path.exists("outputpng"): os.makedirs("outputpng")

    # Lưu bảng so sánh mô hình
    pd.DataFrame(results).to_csv("outputcsv/so_sanh_mo_hinh.csv", index=False, encoding="utf-8-sig")

    # Vẽ Confusion Matrix (Ma trận nhầm lẫn)
    plt.figure(figsize=(7, 6))
    cm = confusion_matrix(y_test, y_pred_rf)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Đoán Thường', 'Đoán Hội viên'], yticklabels=['Thực tế Thường', 'Thực tế Hội viên'])
    plt.title('Ma Trận Nhầm Lẫn - Chứng minh độ chính xác thực tế')
    plt.savefig("outputpng/ma_tran_nham_lan_final.png")
    plt.close()

    # Vẽ Feature Importance (Tầm quan trọng thực tế)
    plt.figure(figsize=(10, 6))
    feat_importances = pd.Series(rf_model.feature_importances_, index=['Tuổi', 'Số tiền mua', 'Đánh giá', 'Lần mua trước', 'Giới tính'])
    feat_importances.sort_values().plot(kind='barh', color='teal')
    plt.title('Tầm quan trọng của các yếu tố ảnh hưởng')
    plt.xlabel('Mức độ ảnh hưởng (%)')
    plt.savefig("outputpng/yeu_to_quan_trong_final.png")
    plt.close()

    # Vẽ ROC Curve
    plt.figure(figsize=(8, 6))
    RocCurveDisplay.from_estimator(rf_model, X_test, y_test)
    plt.title('Biểu đồ ROC Curve')
    plt.savefig("outputpng/bieu_do_roc.png")
    plt.close()

    print("\n✅ HOÀN TẤT: Mô hình đã được chứng minh đầy đủ các chỉ số.")
    print("👉 Kết quả lưu tại: outputcsv/so_sanh_mo_hinh.csv và thư mục outputpng/")

if __name__ == "__main__":
    chay_mo_hinh_chuyen_nghiep()