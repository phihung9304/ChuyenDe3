
📊 Customer Sales Analysis & Forecasting  

1. Giới thiệu

Dự án này tập trung vào việc phân tích dữ liệu khách hàng và dự báo doanh thu theo tháng cho một cửa hàng bán lẻ. Bài toán thuộc lĩnh vực phân tích dữ liệu chuỗi thời gian (time series analysis), trong đó dữ liệu được thu thập theo từng tháng trong vòng 3 năm.

Mục tiêu chính là khai thác insight từ dữ liệu lịch sử, xác định xu hướng, mùa vụ và các yếu tố ảnh hưởng đến doanh thu, từ đó xây dựng mô hình dự báo doanh thu cho 12 tháng tiếp theo nhằm hỗ trợ ra quyết định kinh doanh.

2. Mục tiêu bài toán
    
Làm sạch và chuẩn hóa dữ liệu (xử lý missing, duplicate)

Phân tích xu hướng doanh thu theo thời gian

Đánh giá mối quan hệ giữa:

doanh thu và ngân sách marketing

doanh thu và số lượng  khách hàng

Trực quan hóa dữ liệu bằng  biểu  đồ

Xây dựng mô hình dự báo doanh  thu

Đánh giá mô hình bằng:

MAE

RMSE

MAPE

Dự báo doanh thu 12 tháng tiếp theo

Đưa ra insight và đề xuất kinh doanh

4. Dataset sử dụng

Dataset gồm các cột:

Cột	Ý nghĩa

date	thời gian (cuối mỗi tháng)

sales	doanh thu

promotion_budget	ngân sách marketing

num_customers	số lượng khách hàng

Bước 2. Xử lý dữ liệu thiếu

Kiểm tra dữ liệu thiếu:

df.isnull().sum()

Xử lý:

sales → điền bằng mean

promotion_budget → forward fill

num_customers → forward fill

Xóa dữ liệu trùng:

df.drop_duplicates()


Bước 3. Phân tích mối quan hệ giữa dữ liệu

Phân tích tương quan:

df[['sales','promotion_budget','num_customers']].corr()

Insight:

promotion ↑ → sales ↑ (tương quan dương)

customers ↑ → sales ↑ mạnh hơn

Bước 4. Trực quan hóa

Các biểu đồ sử dụng:

Line chart: doanh thu theo thời gian

Rolling mean: xu hướng mượt

Bar chart: mùa vụ theo tháng

Scatter plot:

promotion vs sales

customers vs sales

Bước 5. Xây dựng mô hình

Sử dụng các mô hình:

Linear Regression

Random Forest

Naive Forecast

Moving Average

Exponential Smoothing

Feature sử dụng:

month, quarter

lag_1, lag_3

rolling_mean_3

Bước 6. Đánh giá mô hình

Các chỉ số:

MAE

RMSE

MAPE

Chọn model tốt nhất dựa trên RMSE thấp nhất.

5. Giải thích chi tiết các file trong project
   
File dữ liệu

sales_data.csv: dữ liệu đầu vào

File code

sales_analysis.py: file chính chạy toàn bộ pipeline

File kết quả trong thư mục outputs/

biểu đồ

file dự báo

File tài liệu

report.pdf: báo cáo đồ án

7. Cấu trúc thư mục thực tế

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
├── DATACLEANING.py/
│  
├── EDA.py/
│   
├── README.md
│
├──shopping_cleaned.csv
│
├──shopping_trends.csv
│
└──VISUALIZATION.py/
```
7. Cách chạy chương trình

Cài đặt thư viện

pip install pandas numpy matplotlib seaborn scikit-learn

Chạy phân tích và huấn luyện mô hình

python sales_analysis.py

Nếu muốn chạy bước làm sạch riêng

Comment các phần code khác và chỉ chạy:

df.isnull().sum()

df.drop_duplicates()

8. Kết luận

Doanh thu có xu hướng tăng theo thời gian

Có yếu tố mùa vụ (cuối năm cao)

Marketing có ảnh hưởng tích cực đến doanh thu

Số lượng khách hàng là yếu tố quan trọng nhất

Random Forest thường cho kết quả tốt nhất

Đề xuất:

Tăng marketing vào mùa thấp điểm

Tập trung tăng khách hàng

Áp dụng dự báo để lập kế hoạch kinh doanh

9. Thành viên nhóm

Nguyễn Sỹ Quang - 20220744

Lê Phi Hùng - 20220838

Hoàng Minh Duy 
