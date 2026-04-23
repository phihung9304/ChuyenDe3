# Customer Sales Analysis & Forecasting

## 1. Giới thiệu

Dự án tập trung vào việc phân tích dữ liệu khách hàng và dự báo doanh thu theo tháng cho một cửa hàng bán lẻ.
Bài toán thuộc lĩnh vực **Time Series Analysis**, với dữ liệu được thu thập theo từng tháng trong vòng 3 năm.
Mục tiêu là:
* Khai thác insight từ dữ liệu lịch sử
* Xác định xu hướng và mùa vụ
* Xây dựng mô hình dự báo doanh thu 12 tháng tiếp theo
* Hỗ trợ ra quyết định kinh doanh

---

## 2. Mục tiêu bài toán

Bài toán được triển khai theo quy trình:

**Data Cleaning → EDA → Visualization → Modeling → Insight**

- **Data Cleaning**: Làm sạch và chuẩn hóa dữ liệu (xử lý missing values, loại bỏ duplicates)

- **EDA (Exploratory Data Analysis)**:
  - Phân tích xu hướng doanh thu theo thời gian
  - Khám phá phân phối dữ liệu và phát hiện bất thường

- **Visualization**:
  - Trực quan hóa xu hướng doanh thu
  - Phân tích mối quan hệ:
    - Doanh thu và ngân sách marketing
    - Doanh thu và số lượng khách hàng

- **Modeling**:
  - Xây dựng mô hình dự báo doanh thu
  - Đánh giá mô hình bằng các chỉ số:
    ```
    MAE
    RMSE
    MAPE
    ```

- **Forecasting**:
  - Dự báo doanh thu cho 12 tháng tiếp theo

- **Insight & Recommendation**:
  - Rút ra insight từ dữ liệu và mô hình
  - Đề xuất chiến lược kinh doanh phù hợp

---
## 3. Dataset sử dụng

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

## 4. Phân tích mối quan hệ giữa các yếu tố và doanh thu

Project thực hiện các phân tích chính nhằm khám phá mối quan hệ giữa hành vi khách hàng và doanh thu:

- Phân tích mối quan hệ giữa **doanh thu và số lượng khách hàng**
- Phân tích ảnh hưởng của **khuyến mãi (promotion) đến doanh thu**
- Thống kê doanh thu theo:
  - Danh mục sản phẩm
  - Giới tính
  - Độ tuổi
  - Mùa mua sắm

Kết quả nổi bật:

- Doanh thu có xu hướng tăng khi số lượng khách hàng tăng  
- Các chương trình khuyến mãi giúp cải thiện doanh thu đáng kể  
- Một số nhóm khách hàng và danh mục sản phẩm đóng góp phần lớn doanh thu  

---

## 5. Trực quan hóa

Các biểu đồ được lưu trong thư mục `outputpng/`:

- **chi_tieu_theo_gioi_tinh.png**: So sánh chi tiêu giữa các nhóm giới tính  
- **chi_tieu_theo_tuoi.png**: Phân tích chi tiêu theo độ tuổi  
- **chi_tieu_theo_mua.png**: Xu hướng chi tiêu theo mùa  
- **chi_tieu_theo_danh_muc.png**: Phân tích chi tiêu theo danh mục sản phẩm  
- **doanh_thu_theo_danh_muc.png**: Doanh thu theo từng danh mục  
- **doanh_thu_theo_mua.png**: Biến động doanh thu theo mùa  
- **phuong_thuc_thanh_toan.png**: Phân tích phương thức thanh toán  
- **boxplot_chi_tieu_gioi_tinh.png**: Phân phối chi tiêu theo giới tính  
- **cac_yeu_to_anh_huong.png**: Tổng hợp các yếu tố ảnh hưởng đến doanh thu  

---

## 6. Xây dựng mô hình

Project sử dụng mô hình hồi quy để dự đoán doanh thu.

Pipeline thực hiện:

- Làm sạch và chuẩn hóa dữ liệu  
- Chia dữ liệu train/test  
- Xây dựng mô hình hồi quy  
- Huấn luyện mô hình trên tập dữ liệu đã xử lý  

---

## 7. Đánh giá mô hình

Hiệu năng mô hình được đánh giá bằng các chỉ số:

- **MAE (Mean Absolute Error)**  
- **RMSE (Root Mean Squared Error)**  
- **MAPE (Mean Absolute Percentage Error)**  

Ý nghĩa:

- **MAE**: Sai lệch trung bình giữa giá trị dự đoán và thực tế  
- **RMSE**: Nhạy hơn với các sai số lớn  
- **MAPE**: Thể hiện sai số dưới dạng phần trăm  

---

## 8. Insight

- Hành vi khách hàng có ảnh hưởng trực tiếp đến doanh thu  
- Các yếu tố như độ tuổi, giới tính và danh mục sản phẩm tạo ra sự khác biệt rõ rệt trong chi tiêu  
- Khuyến mãi là yếu tố quan trọng giúp tăng doanh thu trong ngắn hạn  

---

## 9. Cấu trúc project

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
├── modeling.py
├── Insight.py
│
├── shopping_cleaned.csv
├── shopping_trends.csv
│
└── README.md
```

---

---

## 10. Giải thích chi tiết các file trong project

### File dữ liệu
- **shopping_trends.csv**: Bộ dữ liệu gốc ban đầu, chứa thông tin về khách hàng, hành vi mua sắm và doanh thu.
- **shopping_cleaned.csv**: Dữ liệu sau khi đã được làm sạch và tiền xử lý, sử dụng cho các bước phân tích và mô hình hóa.

---

### Thư mục outputcsv/
Chứa các file kết quả phân tích dạng bảng (CSV):

- **phan_tich_chi_tieu.csv**: Thống kê và phân tích chi tiêu của khách hàng  
- **phan_tich_doanh_thu.csv**: Phân tích doanh thu theo các yếu tố khác nhau  
- **phan_tich_khach_hang.csv**: Phân tích đặc điểm và hành vi khách hàng  
- **phan_tich_san_pham.csv**: Phân tích theo danh mục sản phẩm  
- **phan_tich_hanh_vi.csv**: Phân tích hành vi mua sắm  
- **phan_tich_crosstab.csv**: Bảng chéo giữa các biến để tìm mối quan hệ  
- **phan_tich_ket_hop.csv**: Phân tích kết hợp nhiều yếu tố  
- **top_khach_hang.csv**: Danh sách khách hàng có giá trị cao nhất  
- **ket_qua_du_doan_quan_trong.csv**: Kết quả dự đoán từ mô hình  

---

### Thư mục outputpng/
Chứa các biểu đồ trực quan hóa phục vụ phân tích:

- **chi_tieu_theo_gioi_tinh.png**: So sánh chi tiêu giữa các giới tính  
- **chi_tieu_theo_tuoi.png**: Phân tích chi tiêu theo độ tuổi  
- **chi_tieu_theo_mua.png**: Xu hướng chi tiêu theo mùa  
- **chi_tieu_theo_danh_muc.png**: Chi tiêu theo danh mục sản phẩm  
- **doanh_thu_theo_danh_muc.png**: Doanh thu theo từng danh mục  
- **doanh_thu_theo_mua.png**: Biến động doanh thu theo mùa  
- **danh_muc_san_pham.png**: Phân bố sản phẩm  
- **danh_gia_theo_hoi_vien.png**: Đánh giá theo loại khách hàng (membership)  
- **phuong_thuc_thanh_toan.png**: Phân tích phương thức thanh toán  
- **so_tien_mua_hang.png**: Phân phối số tiền chi tiêu  
- **thanh_toan_theo_do_tuoi.png**: Mối quan hệ giữa độ tuổi và thanh toán  
- **boxplot_chi_tieu_gioi_tinh.png**: Boxplot chi tiêu theo giới tính  
- **cac_yeu_to_anh_huong.png**: Các yếu tố ảnh hưởng đến doanh thu  
- **chi_tieu_subscription.png**: Chi tiêu theo đăng ký dịch vụ  

---

### File mã nguồn

- **DATACLEANING.py**: Thực hiện làm sạch dữ liệu (xử lý missing values, loại bỏ dữ liệu trùng lặp)  
- **EDA.py**: Phân tích khám phá dữ liệu (Exploratory Data Analysis)  
- **VISUALIZATION.py**: Thực hiện trực quan hóa dữ liệu thông qua các biểu đồ (bar chart, scatter plot, boxplot, ...) nhằm hỗ trợ phân tích và hiểu rõ các mối quan hệ trong dữ liệu  
- **modeling.py**: Xây dựng và huấn luyện mô hình dự báo  
- **Insight.py**: Tổng hợp insight và rút ra kết luận từ dữ liệu
  

---

### File tài liệu

- **README.md**: Tài liệu mô tả project, mục tiêu và cách thực hiện  
- **Bảng phân công công việc.docx**: Tài liệu phân chia công việc trong nhóm  

---

---

## 11. Cách chạy chương trình

### Cài đặt thư viện

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Chạy chương trình

```bash
python DATACLEANING.py
python EDA.py
python VISUALIZATION.py
python modeling.py
python Insight.py
```
---

## 12. Kết luận

* Doanh thu có xu hướng tăng theo thời gian
* Có yếu tố mùa vụ (cuối năm cao)
* Marketing ảnh hưởng tích cực đến doanh thu
* Số lượng khách hàng là yếu tố quan trọng nhất
* Random Forest cho kết quả tốt nhất

### Đề xuất

* Tăng marketing vào mùa thấp điểm
* Tập trung phát triển khách hàng
* Áp dụng mô hình dự báo để lập kế hoạch

---

## 13. Thành viên nhóm

* Nguyễn Sỹ Quang - 20220744
* Lê Phi Hùng - 20220838
* Hoàng Minh Duy - 20220794

---
