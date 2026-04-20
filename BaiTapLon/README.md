# 📊 Customer Sales Analysis & Forecasting

## 📌 1. Giới thiệu

Dự án tập trung vào việc phân tích dữ liệu khách hàng và dự báo doanh thu theo tháng cho một cửa hàng bán lẻ.
Bài toán thuộc lĩnh vực **Time Series Analysis**, với dữ liệu được thu thập theo từng tháng trong vòng 3 năm.

Mục tiêu là:

* Khai thác insight từ dữ liệu lịch sử
* Xác định xu hướng và mùa vụ
* Xây dựng mô hình dự báo doanh thu 12 tháng tiếp theo
* Hỗ trợ ra quyết định kinh doanh

---

## 🎯 2. Mục tiêu bài toán
Bài toán được triển khai theo quy trình:

Data Cleaning → EDA → Visualization → Modeling → Insight

* Data Cleaning: Làm sạch và chuẩn hóa dữ liệu (xử lý missing values, loại bỏ duplicates)
* EDA (Exploratory Data Analysis):
 * Phân tích xu hướng doanh thu theo thời gian
 * Khám phá phân phối dữ liệu và phát hiện bất thường

* Visualization:
 * Trực quan hóa xu hướng doanh thu
 * Phân tích mối quan hệ:
 * Doanh thu và ngân sách marketing
 * Doanh thu và số lượng khách hàng

* Modeling:
 * Xây dựng mô hình dự báo doanh thu
* Đánh giá mô hình bằng các chỉ số:
```
MAE
RMSE
MAPE
```

* Forecasting:
 * Dự báo doanh thu cho 12 tháng tiếp theo
* Insight & Recommendation:
 * Rút ra insight từ dữ liệu và mô hình
 * Đề xuất chiến lược kinh doanh phù hợp

---

## 📂 3. Dataset sử dụng

Dataset gồm các cột:

| Cột                       | Ý nghĩa                         |
| ------------------------- | ------------------------------- |
| customer_id               | id khách hàng                   |
| age                       | tuổi                            |
| gender                    | giới tính                       |
| item_purchased            | sản phẩm đã mua                 |
| category                  | danh mục                        |
| purchase_amout_usd        | số tiền mua ( USD )             |
| location                  | vị trí                          |
| size                      | kích thước                      |
| color                     | màu sắc                         |
| season                    | mùa                             |
| review_rating             | đánh giá                        |
| subscription_status       | trạng thái đăng ký              |
| payment_method            | phương thức thánh toán          |
| shipping_type             | loại vận chuyển                 |
| discount_applied          | áp dụng giảm giá                |
| promo_code_used           | mã khuyến mãi sử dụng           |
| previous_purchases        | các đơn mua hàng trước          |
| preferred_payment_method  | phương thức thanh toán ưa thích |
| frequency_of_purchases    | tần suất mua hàng               |

---

## 🧹 4. Tiền xử lý dữ liệu

### 🔍 Kiểm tra dữ liệu thiếu

```python
df.isnull().sum()
```

### 🛠 Xử lý

* `sales` → điền bằng **mean**
* `promotion_budget` → **forward fill**
* `num_customers` → **forward fill**

### 🧾 Xóa dữ liệu trùng

```python
df.drop_duplicates()
```

---

## 📊 5. Phân tích dữ liệu

### 📌 Tương quan

```python
df[['sales','promotion_budget','num_customers']].corr()
```

### 💡 Insight

* Marketing ↑ → Sales ↑ (tương quan dương)
* Customers ↑ → Sales ↑ mạnh hơn

---

## 📈 6. Trực quan hóa

Các biểu đồ sử dụng:

* 📉 Line chart: Doanh thu theo thời gian
* 📊 Rolling mean: Xu hướng mượt
* 📊 Bar chart: Mùa vụ theo tháng
* 🔵 Scatter plot:

  * Promotion vs Sales
  * Customers vs Sales

---

## 🤖 7. Xây dựng mô hình

### 🔧 Các mô hình sử dụng

* Linear Regression
* Random Forest
* Naive Forecast
* Moving Average
* Exponential Smoothing

### 📌 Feature sử dụng

* `month`, `quarter`
* `lag_1`, `lag_3`
* `rolling_mean_3`

---

## 📏 8. Đánh giá mô hình

Các chỉ số:

```
MAE
RMSE
MAPE
```

👉 Chọn mô hình tốt nhất dựa trên **RMSE thấp nhất**

---

## 📁 9. Cấu trúc project

```
BAITAPLON/
│
├── outputcsv/
│   ├── phan_tich_chi_tieu.csv
│   ├── phan_tich_crosstab.csv
│   ├── phan_tich_doanh_thu.csv
│   ├── phan_tich_hanh_vi.csv
│   ├── phan_tich_ket_hop.csv
│   ├── phan_tich_khach_hang.csv
│   ├── phan_tich_san_pham.csv
│   └── top_khach_hang.csv   
│
├── outputpng/
│   ├── boxplot_chi_tieu_gioi_tinh.png
│   ├── chi_tieu_subscription.png
│   ├── chi_tieu_theo_danh_muc.png
│   ├── chi_tieu_theo_gioi_tinh.png
│   ├── chi_tieu_theo_mua.png
│   ├── chi_tieu_theo_tuoi.png
│   ├── danh_muc_san_pham.png
│   ├── doanh_thu_theo_danh_muc.png
│   ├── phuong_thuc_thanh_toan.png
│   └── so_tien_mua_hang.png  
│
├── DATACLEANING.py
├── EDA.py
├── VISUALIZATION.py
│
├── sales_analysis.py
│
├── shopping_cleaned.csv
├── shopping_trends.csv
│
└── README.md
```

---

## ⚙️ 10. Cách chạy chương trình

### 📦 Cài đặt thư viện

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### ▶️ Chạy chương trình

```bash
python sales_analysis.py
```

### 🔄 Chạy riêng bước làm sạch

```python
df.isnull().sum()
df.drop_duplicates()
```

---

## 📌 11. Kết luận

* Doanh thu có xu hướng tăng theo thời gian
* Có yếu tố mùa vụ (cuối năm cao)
* Marketing ảnh hưởng tích cực đến doanh thu
* Số lượng khách hàng là yếu tố quan trọng nhất
* Random Forest cho kết quả tốt nhất

### 💡 Đề xuất

* Tăng marketing vào mùa thấp điểm
* Tập trung phát triển khách hàng
* Áp dụng mô hình dự báo để lập kế hoạch

---

## 👥 12. Thành viên nhóm

* Nguyễn Sỹ Quang - 20220744
* Lê Phi Hùng - 20220838
* Hoàng Minh Duy - 20220794

---
