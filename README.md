📊 Customer Sales Analysis & Forecasting
1. Giới thiệu

Dự án này tập trung vào việc phân tích dữ liệu khách hàng và dự báo doanh thu theo tháng cho một cửa hàng bán lẻ. Bài toán thuộc lĩnh vực phân tích dữ liệu chuỗi thời gian (time series analysis), trong đó dữ liệu được thu thập theo từng tháng trong vòng 3 năm.

Mục tiêu chính là khai thác insight từ dữ liệu lịch sử, xác định xu hướng, mùa vụ và các yếu tố ảnh hưởng đến doanh thu, từ đó xây dựng mô hình dự báo doanh thu cho 12 tháng tiếp theo nhằm hỗ trợ ra quyết định kinh doanh.

2. Mục tiêu bài toán
Làm sạch và chuẩn hóa dữ liệu (xử lý missing, duplicate)
Phân tích xu hướng doanh thu theo thời gian
Đánh giá mối quan hệ giữa:
doanh thu và ngân sách marketing
doanh thu và số lượng khách hàng
Trực quan hóa dữ liệu bằng biểu đồ
Xây dựng mô hình dự báo doanh thu
Đánh giá mô hình bằng:
MAE
RMSE
MAPE
Dự báo doanh thu 12 tháng tiếp theo
Đưa ra insight và đề xuất kinh doanh
3. Dataset sử dụng

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
6. Cấu trúc thư mục thực tế
project/
│
├── data/
│   └── sales_data.csv
│
├── outputs/
│   ├── charts/
│   └── forecast.csv
│
├── src/
│   └── sales_analysis.py
│
├── report/
│   └── report.pdf
│
└── README.md
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

👉 Đề xuất:

Tăng marketing vào mùa thấp điểm
Tập trung tăng khách hàng
Áp dụng dự báo để lập kế hoạch kinh doanh
