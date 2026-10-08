# Task 05 - KNN Regression

## 1. Mục tiêu

Tạo file:

src/knn_regression.py

File này tự cài đặt thuật toán **K-Nearest Neighbors Regression (KNN Regression)**.

Đây là phần cốt lõi của project.

Không sử dụng thư viện có sẵn để thực hiện KNN Regression.

## 2. Input

Thuật toán nhận:
X_train
y_train
X_test

và tham số k
Trong đó:

* `X_train`: dữ liệu feature của tập train đã được chuẩn hóa.
* `y_train`: giá trị `mag` tương ứng của tập train.
* `X_test`: dữ liệu feature của tập test đã được chuẩn hóa.
* `k`: số lượng hàng xóm gần nhất.

Giá trị mặc định:

k = 5

## 3. Thuật toán KNN Regression

Đối với mỗi mẫu trong `X_test`:

### Bước 1: Tính khoảng cách

Sử dụng khoảng cách Euclidean giữa mẫu test và từng mẫu train:

distance = sqrt(sum((x_test - x_train)^2))

### Bước 2: Tìm K hàng xóm gần nhất

Sắp xếp các khoảng cách từ nhỏ đến lớn.

Chọn `k` mẫu có khoảng cách nhỏ nhất.

### Bước 3: Dự đoán

KNN Regression dự đoán bằng trung bình giá trị target của K hàng xóm:

prediction = mean(y_neighbors)

## 4. Yêu cầu tự cài đặt

Phải tự viết:

* Tính khoảng cách Euclidean.
* Tìm K hàng xóm gần nhất.
* Tính trung bình target.
* Dự đoán cho nhiều mẫu test.

Không được sử dụng:

from sklearn.neighbors import KNeighborsRegressor

Không sử dụng bất kỳ thư viện nào để thay thế toàn bộ thuật toán KNN.

Có thể sử dụng NumPy để thực hiện phép tính toán học cơ bản.

## 5. Thiết kế class

Tạo class:

KNNRegressor

Class có:

__init__(self, k=5)

để thiết lập số lượng hàng xóm.

Tạo các phương thức:

fit(self, X_train, y_train)
predict(self, X_test)

### `fit()`

Lưu dữ liệu train:

X_train
y_train

Không cần huấn luyện theo nghĩa truyền thống vì KNN là thuật toán lazy learning.

### `predict()`

Thực hiện KNN Regression cho từng mẫu trong X_test và trả về mảng prediction.

## 6. Kiểm tra dữ liệu đầu vào

Trong class cần kiểm tra:

* `k > 0`
* `k` không lớn hơn số lượng mẫu train.
* Số lượng dòng của `X_train` và `y_train` phải giống nhau.
* `predict()` chỉ được gọi sau `fit()`.

Nếu dữ liệu không hợp lệ thì báo lỗi rõ ràng.

## 7. Thư viện được phép sử dụng

Được phép:

import numpy as np

Không sử dụng:

sklearn

Đặc biệt không sử dụng:

KNeighborsRegressor

## 8. Kiểm tra thuật toán

Sau khi tạo class, cần kiểm tra bằng dataset thật.

Sử dụng:

data/earthquake.csv

và các hàm preprocessing đã tạo trong Task 04.

Thiết lập:
k = 5
Sau đó:

1. Load dataset.
2. Preprocess dataset.
3. Tạo `KNNRegressor(k=5)`.
4. Gọi `fit()` với X_train và y_train.
5. Gọi `predict()` với X_test.
6. In ra một số prediction đầu tiên.

Ví dụ:

print("5 predictions đầu tiên:")
print(y_pred[:5])

## 9. Không làm trong Task này

Không thực hiện:

* MAE
* MSE
* RMSE
* R²
* Visualization
* Tuning K
* Cross-validation

Các phần này sẽ được thực hiện ở những task sau.

## 10. Tiêu chí hoàn thành

Task được xem là hoàn thành khi:

1. Có file `src/knn_regression.py`.
2. Có class `KNNRegressor`.
3. Có `fit()`.
4. Có `predict()`.
5. Tự tính khoảng cách Euclidean.
6. Tự tìm K hàng xóm gần nhất.
7. Tự tính trung bình target.
8. Chạy được với dataset earthquake.
9. Không sử dụng `sklearn`.
10. Prediction trả về đúng số lượng mẫu test.
11. Chương trình chạy không báo lỗi.

## 11. Quy trình Vibe Coding

Thực hiện theo thứ tự:

Read this prompt
↓
Generate src/knn_regression.py
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

