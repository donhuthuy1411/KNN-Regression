# Task 03 – Data Loading

## 1. Mục tiêu

Tạo module `src/data_loader.py` để đọc dataset động đất từ file:

data/earthquake.csv

Module chỉ có nhiệm vụ **đọc dữ liệu và kiểm tra dữ liệu ban đầu**.

Không thực hiện preprocessing, scaling, train/test split hoặc KNN trong task này.

## 2. Input

File dữ liệu:

data/earthquake.csv

Dataset có khoảng 11,063 dòng và 22 cột.

## 3. Output

Module phải cung cấp hàm:

load_data(file_path)
Hàm này:

* Nhận đường dẫn đến file CSV.
* Đọc file bằng pandas.
* Trả về một `DataFrame`.

## 4. Yêu cầu kiểm tra dữ liệu

Sau khi đọc dữ liệu, chương trình cần kiểm tra:

* Số dòng và số cột.
* Tên các cột.
* Kiểu dữ liệu của các cột.
* Số lượng giá trị thiếu ở mỗi cột.

Có thể sử dụng các lệnh pandas như:

df.shape
df.columns
df.dtypes
df.isnull().sum()

Không cần xử lý giá trị thiếu trong task này.

## 5. Yêu cầu code

Tạo file:

src/data_loader.py

Code cần:

* Sử dụng Python.
* Sử dụng pandas.
* Có hàm `load_data(file_path)`.
* Có kiểm tra file có tồn tại hay không.
* Code dễ đọc, phù hợp với sinh viên mới học Machine Learning.
* Có comment ngắn giải thích những phần quan trọng.
* Không viết code KNN.
* Không sử dụng `KNeighborsRegressor`.
* Không sử dụng `sklearn`.

## 6. Kiểm thử

Sau khi tạo code, cần kiểm tra bằng dataset thật:

data/earthquake.csv
Kết quả kiểm tra cần cho biết:

Dataset shape
Column names
Data types
Missing values

Nếu đọc dữ liệu thành công thì không cần sửa file CSV gốc.

## 7. Giới hạn của Task

Task này CHỈ thực hiện:

CSV → đọc dữ liệu → kiểm tra dữ liệu

Không thực hiện:

* Xóa dòng thiếu dữ liệu.
* Chọn feature.
* Chọn target.
* Train/test split.
* Scaling.
* KNN Regression.
* Evaluation.
* Visualization.

Các phần trên sẽ được thực hiện ở những task tiếp theo.

## 8. Tiêu chí hoàn thành

Task được xem là hoàn thành khi:

* `src/data_loader.py` được tạo.
* Dataset `data/earthquake.csv` được đọc thành công.
* Có thể lấy được `DataFrame`.
* Kiểm tra được shape, columns, dtypes và missing values.
* Không sử dụng thư viện KNN có sẵn.
* Code chạy không báo lỗi.

Sau khi kiểm tra thành công mới thực hiện Git commit.
