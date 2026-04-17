import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def run_modeling():
    csv_dir = "outputcsv"
    png_dir = "outputpng"
    for folder in [csv_dir, png_dir]:
        if not os.path.exists(folder): os.makedirs(folder)

    df = pd.read_csv("shopping_cleaned.csv")
    print("--- Đang huấn luyện mô hình dự đoán Hội viên... ---")

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

    # ĐỔI TÊN CSV: modeling_importance_results.csv -> ket_qua_du_doan_quan_trong.csv
    importance_df.to_csv(os.path.join(csv_dir, "ket_qua_du_doan_quan_trong.csv"), index=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Mức độ ảnh hưởng', y='Yếu tố', palette='viridis')
    plt.title('Yếu tố quyết định khách hàng trung thành')
    # ĐỔI TÊN PNG: modeling_feature_importance.png -> cac_yeu_to_anh_huong.png
    plt.savefig(os.path.join(png_dir, "cac_yeu_to_anh_huong.png"))
    plt.close()

    print(f"✅ Modeling thành công!")
    print(f"-> File CSV: {csv_dir}/ket_qua_du_doan_quan_trong.csv")
    print(f"-> Biểu đồ: {png_dir}/cac_yeu_to_anh_huong.png")

if __name__ == "__main__":
    run_modeling()