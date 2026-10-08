KNN Regression - Dự đoán độ lớn động đất

1. Giới thiệu

Project sử dụng K-Nearest Neighbors Regression (KNN Regression) để dự đoán độ lớn động đất (mag) dựa trên các đặc trưng của trận động đất.

Thuật toán KNN Regression được tự cài đặt bằng Python, không sử dụng KNeighborsRegressor của Scikit-learn.

2. Mục tiêu

Hiểu nguyên lý hoạt động của KNN Regression.

Thực hiện tiền xử lý và chuẩn hóa dữ liệu.

Tự cài đặt thuật toán KNN Regression.

Đánh giá mô hình bằng MAE, MSE, RMSE và R².

Trực quan hóa giá trị thực tế và giá trị dự đoán.

3. Dataset

Dataset chứa dữ liệu về các trận động đất.

Số dòng ban đầu: 11,063

Số cột: 22

Biến mục tiêu: mag

Train: 8,498 mẫu

Test: 2,125 mẫu

4. Các đặc trưng sử dụng

Mô hình sử dụng 9 đặc trưng:

latitude
longitude
depth
nst
gap
dmin
rms
horizontalError
depthError

Biến cần dự đoán:

mag

5. Phương pháp

5.1. Tiền xử lý

Đọc dữ liệu từ CSV.

Chọn 9 đặc trưng và mag.

Loại bỏ các dòng thiếu dữ liệu cần thiết.

Chia dữ liệu 80% train và 20% test.

Chuẩn hóa bằng Standardization.

Mean và standard deviation được tính từ tập train, sau đó áp dụng cho train và test để tránh data leakage.

5.2. KNN Regression

Mô hình sử dụng K = 5.

Các bước:

Tính khoảng cách Euclidean từ mẫu cần dự đoán đến các mẫu train.

Sắp xếp khoảng cách.

Chọn 5 hàng xóm gần nhất.

Tính trung bình giá trị mag của 5 hàng xóm.

Kết quả là giá trị dự đoán.

5.3. Đánh giá

Project tự cài đặt:

MAE - Mean Absolute Error

MSE - Mean Squared Error

RMSE - Root Mean Squared Error

R² - R-squared

6. Kết quả

Metric

Kết quả

MAE

0.2999

MSE

0.1689

RMSE

0.4109

R²

0.8936

R² ≈ 0.8936 cho thấy mô hình giải thích được khoảng 89.36% độ biến thiên của mag trên tập test.

7. Cấu trúc project

KNN_Regression/
├── data/
│   └── earthquake.csv
├── docs/
│   ├── 01_define.md
│   ├── 02_design.md
│   ├── 03_data_loading.md
│   ├── 04_preprocessing.md
│   ├── 05_knn_regression.md
│   ├── 06_evaluation.md
│   ├── 07_visualization.md
│   └── 08_main_pipeline.md
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── knn_regression.py
│   ├── metrics.py
│   ├── visualization.py
│   └── main.py
├── .gitignore
└── README.md

8. Cách chạy

Cài đặt thư viện:

pip install pandas numpy matplotlib

Chạy từ thư mục gốc project:

python src/main.py

Pipeline:

Load Dataset
    ↓
Preprocessing
    ↓
KNN Regression (K=5)
    ↓
Prediction
    ↓
Evaluation
    ↓
Visualization

9. Công nghệ sử dụng

Python

NumPy

Pandas

Matplotlib

Git / GitHub

Không sử dụng:

sklearn.neighbors.KNeighborsRegressor

Khoảng cách Euclidean, tìm K hàng xóm gần nhất và phép dự đoán đều được tự cài đặt.

10. Vibe Coding Workflow

Define → Design → Describe → Generate → Review → Run → Test → Refactor → Commit

Project được phát triển và kiểm tra từng phần trước khi commit lên GitHub.