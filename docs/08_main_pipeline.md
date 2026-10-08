# Task 08 - Main Pipeline

## 1. Mục tiêu

Tạo file `src/main.py` để kết nối toàn bộ các module của dự án KNN Regression thành một quy trình hoàn chỉnh.

Sau Task này, người dùng chỉ cần chạy:

python src/main.py

để thực hiện toàn bộ quá trình:

Đọc dataset
    ↓
Preprocessing
    ↓
Train KNN Regression
    ↓
Predict
    ↓
Evaluation
    ↓
Visualization

## 2. File cần tạo

Tạo file:

src/main.py

## 3. Các module cần sử dụng

`main.py` phải sử dụng các module đã tạo trước đó:

src/data_loader.py
src/preprocessing.py
src/knn_regression.py
src/metrics.py
src/visualization.py

Không viết lại thuật toán KNN hoặc các metric trong `main.py`.

## 4. Quy trình xử lý

### Bước 1 - Load dataset

Đọc:

data/earthquake.csv

Sử dụng:

load_data()

### Bước 2 - Preprocessing

Sử dụng:

preprocess_data()

Nhận được:

X_train
X_test
y_train
y_test

Preprocessing đã bao gồm:

- Chọn 9 features.
- Chọn target `mag`.
- Loại bỏ dữ liệu thiếu cần thiết.
- Chia train/test theo tỷ lệ 80/20.
- Standardization.

Không thực hiện preprocessing lại trong `main.py`.

### Bước 3 - Tạo mô hình KNN

Sử dụng class:

KNNRegressor

Sử dụng:

k = 5

Không sử dụng:

sklearn.neighbors.KNeighborsRegressor

### Bước 4 - Train

Gọi:

knn.fit(X_train, y_train)


### Bước 5 - Prediction

Gọi:

y_pred = knn.predict(X_test)

Kiểm tra:

Số lượng prediction = số lượng mẫu test

### Bước 6 - Evaluation

Sử dụng các hàm trong:

src/metrics.py

Tính:

MAE
MSE
RMSE
R²

Không tự viết lại công thức metric trong `main.py`.

### Bước 7 - Visualization

Sử dụng:

plot_actual_vs_predicted(y_test, y_pred)


Hiển thị biểu đồ:

Actual vs Predicted

## 5. Kết quả cần in ra

Chương trình cần hiển thị các thông tin chính:

=== KNN Regression ===

Số lượng mẫu train: ...
Số lượng mẫu test: ...
Số lượng features: 9
K = 5

=== Evaluation ===
MAE: ...
MSE: ...
RMSE: ...
R²: ...

=== Prediction ===
5 prediction đầu tiên:
...

Các giá trị metric phải được tính từ:

y_test
y_pred

trên dataset earthquake.csv thật.

## 6. Kiểm tra prediction

Kiểm tra:

len(y_pred) == len(y_test)


Nếu không bằng nhau thì báo lỗi.

## 7. Đường dẫn dataset

Trong `main.py`, sử dụng:

data/earthquake.csv

Chương trình được thiết kế để chạy từ thư mục gốc của project:

python src/main.py

## 8. Thư viện

Không thêm thư viện Machine Learning mới.

Toàn bộ project chỉ sử dụng các thư viện đã có:

- NumPy
- Pandas
- Matplotlib

Không sử dụng:

sklearn

## 9. Không thay đổi các module cũ

Task này chỉ tạo:

src/main.py

Không sửa:

src/data_loader.py
src/preprocessing.py
src/knn_regression.py
src/metrics.py
src/visualization.py


trừ khi phát hiện lỗi import thực sự cần thiết để pipeline chạy.

Nếu phát hiện lỗi ở module cũ, phải báo rõ lỗi trước khi sửa.

## 10. Kiểm thử

Chạy:

python src/main.py

Kiểm tra:

- Dataset được đọc thành công.
- Preprocessing chạy thành công.
- KNN được train thành công.
- Prediction chạy thành công.
- Số lượng prediction bằng số lượng mẫu test.
- MAE được tính.
- MSE được tính.
- RMSE được tính.
- R² được tính.
- Biểu đồ Actual vs Predicted hiển thị.

## 11. Không làm trong Task này

Không thực hiện:

- Hyperparameter tuning.
- Grid Search.
- Cross-validation.
- Thử nhiều giá trị K.
- Thay đổi dataset.
- Thay đổi feature.
- Thay đổi thuật toán KNN.
- Sử dụng KNN từ sklearn.
- Thêm giao diện GUI.
- Thêm chức năng không cần thiết.

Task này chỉ tập trung vào việc kết nối các module thành một pipeline hoàn chỉnh.

## 12. Quy trình Vibe Coding

Thực hiện:

1. Đọc file `docs/08_main_pipeline.md`.
2. Generate `src/main.py`.
3. Review code.
4. Chạy chương trình.
5. Kiểm tra toàn bộ pipeline.
6. Sửa lỗi nếu có.
7. Chạy lại.
8. Chỉ commit sau khi pipeline chạy thành công.

## 13. Prompt cho AI Coding

Sử dụng prompt sau:

Đọc file docs/08_main_pipeline.md và thực hiện đúng Task 08.

Tạo file src/main.py để kết nối các module hiện có:

- data_loader.py
- preprocessing.py
- knn_regression.py
- metrics.py
- visualization.py

Pipeline phải thực hiện:

1. Load data/earthquake.csv.
2. Preprocessing.
3. Tạo KNNRegressor với k=5.
4. Fit bằng X_train và y_train.
5. Predict X_test.
6. Kiểm tra số lượng prediction bằng số lượng mẫu test.
7. Tính MAE, MSE, RMSE và R² bằng các hàm trong metrics.py.
8. In 5 prediction đầu tiên.
9. In các metric.
10. Hiển thị biểu đồ Actual vs Predicted bằng visualization.py.

Không viết lại thuật toán KNN hoặc metric trong main.py.

Không sử dụng sklearn.

Không thêm chức năng ngoài yêu cầu.

Không sửa các module cũ nếu không thực sự cần thiết. Nếu phát hiện lỗi import hoặc lỗi module cũ, hãy báo rõ trước khi sửa.

Sau khi tạo code:
1. Review code.
2. Chạy:
   python src/main.py
3. Kiểm tra toàn bộ pipeline.
4. Nếu có lỗi thì sửa và chạy lại.
5. Báo cho tôi kết quả chạy.
6. Chưa thực hiện git commit hoặc git push.

## 14. Tiêu chí hoàn thành

Task 08 hoàn thành khi:

- `src/main.py` được tạo.
- Có thể chạy bằng:

python src/main.py

- Dataset được load thành công.
- Preprocessing thành công.
- KNN Regression chạy thành công.
- Prediction thành công.
- Evaluation thành công.
- Có MAE.
- Có MSE.
- Có RMSE.
- Có R².
- Có 5 prediction đầu tiên.
- Có biểu đồ Actual vs Predicted.
- Không sử dụng sklearn.
- Không viết lại KNN hoặc metrics trong `main.py`.