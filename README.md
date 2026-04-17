# 🛒 Customer Shopping Data Analysis

## 📌 1. Giới thiệu

Dự án tập trung vào việc **làm sạch và xử lý dữ liệu khách hàng mua sắm** từ file `shopping_trends.csv`.

Mục tiêu chính là:

* Làm sạch dữ liệu (data cleaning)
* Chuẩn hóa dữ liệu để phục vụ phân tích (EDA)
* Loại bỏ dữ liệu sai lệch và ngoại lai
* Tạo dataset sạch cho các bước phân tích tiếp theo

---

## 🎯 2. Mục tiêu bài toán

* Xóa dữ liệu trùng lặp
* Chuẩn hóa tên cột
* Chuyển đổi kiểu dữ liệu
* Làm sạch dữ liệu text
* Xử lý giá trị thiếu (missing values)
* Lọc dữ liệu hợp lệ
* Loại bỏ outlier
* Xuất dữ liệu sạch

---

## 📂 3. Dataset sử dụng

Dataset: `shopping_trends.csv`

### 👤 Thông tin khách hàng

| Cột         | Ý nghĩa       |
| ----------- | ------------- |
| Customer ID | ID khách hàng |
| Age         | Tuổi          |
| Gender      | Giới tính     |
| Location    | Khu vực       |

### 🛍 Thông tin mua hàng

| Cột                   | Ý nghĩa           |
| --------------------- | ----------------- |
| Item Purchased        | Sản phẩm đã mua   |
| Category              | Danh mục sản phẩm |
| Purchase Amount (USD) | Số tiền mua       |
| Size                  | Kích thước        |
| Color                 | Màu sắc           |

### 📦 Thông tin giao dịch

| Cột              | Ý nghĩa                |
| ---------------- | ---------------------- |
| Payment Method   | Phương thức thanh toán |
| Shipping Type    | Hình thức vận chuyển   |
| Discount Applied | Có giảm giá            |
| Promo Code Used  | Có dùng mã giảm        |

### 🔁 Hành vi khách hàng

| Cột                      | Ý nghĩa             |
| ------------------------ | ------------------- |
| Previous Purchases       | Số lần mua trước    |
| Frequency of Purchases   | Tần suất mua        |
| Subscription Status      | Trạng thái đăng ký  |
| Preferred Payment Method | Thanh toán ưa thích |

### ⭐ Đánh giá

| Cột           | Ý nghĩa  |
| ------------- | -------- |
| Review Rating | Đánh giá |
| Season        | Mùa      |

---

## 🧹 4. Quy trình xử lý dữ liệu

### 📥 1. Load dữ liệu

```python
df = pd.read_csv("shopping_trends.csv")
```

---

### 🧾 2. Xóa dữ liệu trùng

```python
df.drop_duplicates()
```

---

### 🔤 3. Chuẩn hóa tên cột

* Xóa khoảng trắng
* Chuyển chữ thường
* Thay space → `_`
* Xóa ký tự đặc biệt

---

### 🔢 4. Chuẩn hóa kiểu dữ liệu

```python
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["purchase_amount_usd"] = pd.to_numeric(df["purchase_amount_usd"], errors="coerce")
```

---

### 🧽 5. Làm sạch dữ liệu text

* Gender → chuẩn hóa chữ cái
* Item Purchased → xóa khoảng trắng
* Category → viết hoa chữ cái đầu

---

### ❌ 6. Xử lý dữ liệu thiếu

```python
df.isnull().sum()
df.dropna()
```

---

### 🎯 7. Lọc dữ liệu hợp lệ

* Age: 18 → 100
* Purchase > 0

---

### 📉 8. Xử lý Outlier (IQR)

* Tính Q1, Q3
* Tính IQR
* Loại bỏ giá trị ngoài khoảng

---

### 🔄 9. Reset index

```python
df.reset_index(drop=True)
```

---

### 💾 10. Lưu dữ liệu

```python
df.to_csv("shopping_cleaned.csv", index=False)
```

---

## 📁 5. Cấu trúc project

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

## ⚙️ 6. Cách chạy chương trình

### 📦 Cài thư viện

```bash
pip install pandas
```

### ▶️ Chạy chương trình

```bash
python DATACLEANING.py
```

---

## 📊 7. Kết quả

* Dataset sạch: `shopping_cleaned.csv`
* Dữ liệu đã:

  * Không còn trùng lặp
  * Không có missing
  * Không có outlier lớn
  * Chuẩn hóa format

---

## 📌 8. Kết luận

* Dữ liệu ban đầu chứa nhiều lỗi (missing, sai định dạng)
* Sau khi xử lý, dữ liệu đã sẵn sàng cho:

  * Phân tích dữ liệu (EDA)
  * Trực quan hóa
  * Machine Learning

---

## 👥 9. Thành viên nhóm

* Nguyễn Sỹ Quang - 20220744
* Lê Phi Hùng - 20220838
* Hoàng Minh Duy - 20220744

---
