# Task 06 - Evaluation

## 1. Mục tiêu

Tạo module đánh giá kết quả dự đoán của mô hình KNN Regression.

Module sẽ tính 4 độ đo:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² (R-squared)

Tất cả các metric phải được tự cài đặt bằng NumPy, không sử dụng các hàm metric có sẵn từ Scikit-learn.

## 2. File cần tạo

Tạo file:

src/metrics.py

## 3. Input

Các hàm đánh giá nhận:

- `y_true`: giá trị thực tế.
- `y_pred`: giá trị mô hình dự đoán.

Hai mảng phải có cùng số lượng phần tử.


## 4. Các metric cần cài đặt

### 4.1. MAE - Mean Absolute Error

Công thức:

MAE = (1/n) * Σ|y_true - y_pred|

MAE cho biết sai số tuyệt đối trung bình giữa giá trị thực tế và giá trị dự đoán.

Giá trị MAE càng nhỏ thì mô hình dự đoán càng tốt.

### 4.2. MSE - Mean Squared Error

Công thức:

MSE = (1/n) * Σ(y_true - y_pred)²

MSE bình phương sai số trước khi lấy trung bình.

Giá trị MSE càng nhỏ thì mô hình càng tốt.

### 4.3. RMSE - Root Mean Squared Error

Công thức:

RMSE = √MSE

RMSE đưa sai số về cùng đơn vị với biến mục tiêu `mag`.

Giá trị RMSE càng nhỏ thì mô hình càng tốt.

### 4.4. R² - R-squared

Công thức:

R² = 1 - SSE / SST

Trong đó:

SSE = Σ(y_true - y_pred)²

SST = Σ(y_true - mean(y_true))²

R² cho biết mô hình giải thích được bao nhiêu phần biến thiên của dữ liệu.

R² càng gần 1 thì mô hình càng tốt.

## 5. Các hàm cần tạo

Tạo 4 hàm:
mean_absolute_error(y_true, y_pred)
mean_squared_error(y_true, y_pred)
root_mean_squared_error(y_true, y_pred)
r2_score(y_true, y_pred)

Có thể sử dụng NumPy.

Không được sử dụng:

from sklearn.metrics import ...

Không được sử dụng bất kỳ mô hình KNN có sẵn nào.

## 6. Kiểm tra dữ liệu đầu vào

Mỗi hàm cần kiểm tra:

- `y_true` và `y_pred` có cùng số lượng phần tử hay không.
- Nếu không khớp thì báo lỗi phù hợp.

Đối với R²:

- Tính `SS_res`.
- Tính `SS_tot`.
- Nếu `SS_tot = 0` thì không thực hiện phép chia.
- Báo lỗi phù hợp để tránh chia cho 0.

## 7. Kiểm thử

Trong:

src/metrics.py

tạo phần kiểm thử khi chạy trực tiếp file.

Sử dụng dữ liệu giả định:

y_true = np.array([3.0, -0.5, 2.0, 7.0])
y_pred = np.array([2.5, 0.0, 2.0, 8.0])

In ra:

MAE:
MSE:
RMSE:
R²:

Kết quả dự kiến:

MAE: 0.5
MSE: 0.375
RMSE: 0.6123724356957945
R²: 0.9486081370449679

## 8. Tiêu chí hoàn thành

Task được xem là hoàn thành khi:

- `src/metrics.py` được tạo.
- Có đủ 4 metric.
- Công thức được cài đặt bằng NumPy.
- Không sử dụng Scikit-learn.
- Có kiểm tra kích thước `y_true` và `y_pred`.
- Có xử lý trường hợp `SS_tot = 0`.
- File chạy trực tiếp không xảy ra lỗi.
- Kết quả test hợp lý.

## 9. Không làm trong Task này

Không thực hiện:

- Visualization.
- Cross-validation.
- Hyperparameter tuning.
- Grid Search.
- Thay đổi thuật toán KNN.
- Thay đổi preprocessing.
- Thay đổi dataset.

Task này chỉ tập trung vào việc tự cài đặt các metric đánh giá.

## 10. Quy trình Vibe Coding

Thực hiện theo quy trình:

1. Đọc yêu cầu trong file này.
2. Generate code `src/metrics.py`.
3. Review code.
4. Chạy test.
5. Sửa lỗi nếu có.
6. Chạy lại test.
7. Chỉ commit sau khi code chạy thành công.

## 11. Prompt cho AI Coding

Sử dụng prompt sau để yêu cầu AI thực hiện Task 06:

Đọc file docs/06_evaluation.md.

Hãy thực hiện đúng Task 06 trong file đó.

Tạo src/metrics.py để tự cài đặt:
- MAE
- MSE
- RMSE
- R²

Chỉ sử dụng NumPy, không sử dụng sklearn.

Sau khi tạo code:
1. Kiểm tra lại công thức.
2. Kiểm tra input y_true và y_pred.
3. Xử lý trường hợp không thể tính R².
4. Chạy phần test trong metrics.py.
5. In kết quả để tôi kiểm tra.

Không làm thêm visualization hoặc các task khác.

## 12. Lệnh kiểm tra

Sau khi AI tạo code, chạy từ thư mục gốc project:

python src/metrics.py

Kết quả cần kiểm tra:

=== Kiểm tra metrics với dữ liệu giả định ===
y_true: [ 3.  -0.5  2.   7. ]
y_pred: [2.5 0.  2.  8. ]
MAE: 0.5
MSE: 0.375
RMSE: 0.6123724356957945
R²: 0.9486081370449679

## 13. Git
git status
git add .
git commit -m "feat: add evaluation metrics"
git push
