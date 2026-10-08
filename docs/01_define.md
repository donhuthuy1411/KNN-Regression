# DEFINE - KNN Regression

## 1. Project Name

**KNN Regression - Dự đoán độ lớn động đất**

## 2. Problem

Xây dựng một chương trình sử dụng thuật toán **K-Nearest Neighbors Regression (KNN Regression)** để dự đoán độ lớn (`mag`) của một trận động đất dựa trên các thông tin quan trắc của trận động đất.

Mục tiêu chính của dự án là giúp người học hiểu được cách hoạt động của KNN Regression thông qua việc **tự cài đặt thuật toán**, thay vì sử dụng mô hình KNN có sẵn từ các thư viện Machine Learning.

## 3. Target Users

* Sinh viên đang học Machine Learning.
* Người mới tìm hiểu thuật toán KNN Regression.
* Người xem bài thuyết trình/demo về Machine Learning.

Dự án được xây dựng với mục đích **học tập và trình diễn**, không nhằm sử dụng để dự đoán động đất trong thực tế.

## 4. Input

### Dataset

Dataset chứa thông tin về các trận động đất.

File dữ liệu:
data/earthquake.csv

Dataset ban đầu có **11.063 dòng và 22 cột**.

### Features được sử dụng

Sau khi phân tích dataset, sử dụng 9 đặc trưng số:

1. `latitude` - Vĩ độ
2. `longitude` - Kinh độ
3. `depth` - Độ sâu
4. `nst` - Số trạm địa chấn
5. `gap` - Khoảng cách góc
6. `dmin` - Khoảng cách đến trạm gần nhất
7. `rms` - Sai số RMS
8. `horizontalError` - Sai số vị trí theo phương ngang
9. `depthError` - Sai số độ sâu

### Target

mag

`mag` biểu diễn độ lớn của trận động đất và là giá trị liên tục, phù hợp với bài toán Regression.

### Tham số K

Thuật toán cho phép lựa chọn giá trị `K`, ví dụ:
K = 3
K = 5
K = 7

## 5. Output

Chương trình cần tạo ra:

* Giá trị `mag` dự đoán cho các mẫu dữ liệu.
* Giá trị `mag` thực tế để so sánh.
* Các chỉ số đánh giá mô hình:

  * MAE
  * MSE
  * RMSE
  * R²
* Biểu đồ so sánh giá trị thực tế và giá trị dự đoán.

Ví dụ:
Actual Magnitude    Predicted Magnitude
4.50                4.62
3.80                3.71
5.10                4.95

## 6. Data Preprocessing

Dữ liệu cần được xử lý trước khi đưa vào KNN.

Các bước chính:

1. Đọc dataset từ file CSV.
2. Chọn các feature và target cần thiết.
3. Loại bỏ các dòng có giá trị thiếu.
4. Tách features `X` và target `y`.
5. Chia dữ liệu thành tập train và test.
6. Chuẩn hóa các feature để các đặc trưng có thang đo phù hợp khi tính khoảng cách.

Dataset gốc trong `data/earthquake.csv` phải được giữ nguyên và không chỉnh sửa trực tiếp.

## 7. Core Features

Chương trình cần có các chức năng chính:

### 7.1. Load Dataset

Đọc dữ liệu từ:
data/earthquake.csv

### 7.2. Preprocessing

* Chọn feature.
* Xử lý missing values.
* Chuẩn hóa dữ liệu.
* Tách dữ liệu train/test.

### 7.3. KNN Regression

Tự cài đặt thuật toán KNN Regression gồm:

1. Tính khoảng cách Euclidean.
2. Tính khoảng cách từ mẫu cần dự đoán đến các mẫu train.
3. Sắp xếp các mẫu theo khoảng cách.
4. Chọn `K` hàng xóm gần nhất.
5. Tính trung bình giá trị target của `K` hàng xóm.
6. Trả về giá trị dự đoán.

### 7.4. Evaluation

Đánh giá kết quả bằng:

* MAE
* MSE
* RMSE
* R²

### 7.5. Visualization

Tạo biểu đồ giúp người xem dễ hiểu sự khác biệt giữa:

Giá trị thực tế và Giá trị dự đoán

## 8. Technology Constraints

### Ngôn ngữ
Python

### Được phép sử dụng

Có thể sử dụng các thư viện hỗ trợ cho:

* Đọc và xử lý dữ liệu.
* Tính toán số học.
* Vẽ biểu đồ.

Ví dụ:
pandas
numpy
matplotlib

### Không được phép

Không sử dụng mô hình KNN Regression có sẵn từ thư viện Machine Learning.

Không được sử dụng:

from sklearn.neighbors import KNeighborsRegressor


Thuật toán KNN Regression phải được **tự cài đặt bằng Python**.

Các thành phần cốt lõi như tính khoảng cách, tìm K hàng xóm gần nhất và tính giá trị dự đoán phải do chương trình tự thực hiện.

## 9. Evaluation

Dự án được đánh giá dựa trên:

### 9.1. Kết quả mô hình

Sử dụng:

* MAE
* MSE
* RMSE
* R²

### 9.2. Tính đúng của thuật toán

Kiểm tra:

* Khoảng cách được tính đúng.
* Chọn đúng K hàng xóm gần nhất.
* Giá trị dự đoán được tính bằng trung bình của K hàng xóm.
* Kết quả thay đổi hợp lý khi thay đổi K.

### 9.3. Yêu cầu Vibe Coding

Mỗi nhiệm vụ phát triển phải có một file `.md` trong thư mục: docs/

Quy trình phát triển:

Describe
↓
Generate
↓
Review
↓
Run
↓
Test
↓
Refactor
↓
Commit

## 10. Project Scope

Dự án tập trung vào việc **giải thích và minh họa KNN Regression**.

Không tập trung vào:

* Dự đoán động đất trong thực tế.
* Xây dựng hệ thống Machine Learning production.
* So sánh nhiều thuật toán Machine Learning.
* Tối ưu mô hình phức tạp.