# Task 04 - Data Preprocessing

## 1. Mục tiêu

Tạo file:

src/preprocessing.py

File này chịu trách nhiệm chuẩn bị dữ liệu cho mô hình KNN Regression.

Chỉ thực hiện các bước tiền xử lý dữ liệu, chưa cài đặt thuật toán KNN, chưa tính metric và chưa vẽ biểu đồ.

## 2. Dữ liệu đầu vào

Dataset:

data/earthquake.csv

DataFrame được truyền vào từ module `data_loader.py`.

Target cần dự đoán:

mag

Các feature sử dụng:

latitude
longitude
depth
nst
gap
dmin
rms
horizontalError
depthError

Không sử dụng các cột:

time
magType
net
id
updated
place
type
status
locationSource
magSource
magError
magNst

## 3. Xử lý giá trị thiếu

Dataset có một số giá trị thiếu.

Yêu cầu:

* Xóa các dòng có giá trị thiếu bằng `dropna()`.
* Không được sửa trực tiếp file `data/earthquake.csv`.
* Việc xóa dữ liệu chỉ thực hiện trên DataFrame trong chương trình.

Sau khi xử lý, X và y không được chứa giá trị thiếu.

## 4. Tạo X và y

Tạo:
X = các feature
y = target mag


Trong đó:
X.shape = (số mẫu, 9)
y.shape = (số mẫu,)

## 5. Chia dữ liệu Train/Test

Chia dữ liệu theo tỷ lệ:

80% Train
20% Test

Yêu cầu:

* Có xáo trộn dữ liệu.
* Sử dụng `random_state = 42`.
* Không sử dụng `sklearn.model_selection.train_test_split`.
* Tự cài đặt việc chia dữ liệu bằng NumPy.

Kết quả cần có:
X_train
X_test
y_train
y_test

## 6. Chuẩn hóa dữ liệu

KNN sử dụng khoảng cách giữa các điểm dữ liệu nên cần chuẩn hóa feature.

Sử dụng Standardization:

z = (x - mean) / std

Yêu cầu quan trọng:

* Tính `mean` và `std` chỉ trên `X_train`.
* Dùng `mean` và `std` của `X_train` để chuẩn hóa cả `X_train` và `X_test`.
* Không được tính riêng mean/std của `X_test`.
* Không sử dụng `sklearn.preprocessing.StandardScaler`.

Mục đích là tránh Data Leakage.

## 7. Hàm chính

Tạo hàm:

preprocess_data(df)

Hàm trả về:

X_train, X_test, y_train, y_test

## 8. Thư viện được phép sử dụng

Được phép:

import pandas as pd
import numpy as np

Không sử dụng:

sklearn

Đặc biệt không sử dụng:
train_test_split
StandardScaler
KNeighborsRegressor

## 9. Kiểm tra kết quả

Sau khi preprocessing cần kiểm tra:

* Số lượng mẫu sau khi xóa missing.
* Số lượng feature.
* Shape của X_train, X_test, y_train, y_test.
* Không còn giá trị thiếu.
* Mean của từng feature trong X_train sau chuẩn hóa gần 0.
* Standard deviation của từng feature trong X_train sau chuẩn hóa gần 1.

Có thể sử dụng các lệnh kiểm tra như:

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

print(np.isnan(X_train).sum())
print(np.isnan(X_test).sum())

## 10. Không làm trong Task này

Không thực hiện:

* KNN Regression
* Tính khoảng cách Euclidean
* Tìm K hàng xóm gần nhất
* Dự đoán
* MAE
* MSE
* RMSE
* R²
* Vẽ biểu đồ

Các phần này sẽ được thực hiện ở các task sau.

## 11. Tiêu chí hoàn thành

Task được xem là hoàn thành khi:

1. Có file `src/preprocessing.py`.
2. Đọc được DataFrame từ `data_loader.py`.
3. Xử lý được missing values.
4. Tạo được X và y.
5. Chia Train/Test theo tỷ lệ 80/20.
6. Chuẩn hóa đúng bằng thống kê của tập Train.
7. Không sử dụng thư viện sklearn.
8. Không có Data Leakage.
9. Chạy chương trình không báo lỗi.
10. Kết quả shape và dữ liệu được kiểm tra rõ ràng.

## 12. Quy trình Vibe Coding

Thực hiện theo thứ tự:

Read this prompt
↓
Generate src/preprocessing.py
↓
Review code
↓
Run
↓
Test
↓
Fix nếu có lỗi
↓
Refactor nếu cần
↓
Git commit
