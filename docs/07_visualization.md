# Task 07 - Visualization

## 1. Mục tiêu

Tạo module trực quan hóa kết quả dự đoán của mô hình KNN Regression.

Biểu đồ chính:

- Actual vs Predicted

Biểu đồ giúp so sánh:

- Giá trị thực tế của `mag`.
- Giá trị `mag` do mô hình KNN dự đoán.

Mục đích của biểu đồ là giúp người xem dễ dàng quan sát mức độ chính xác của mô hình.

## 2. File cần tạo

Tạo file:

src/visualization.py

## 3. Input

Hàm visualization nhận:

- `y_true`: giá trị thực tế.
- `y_pred`: giá trị dự đoán.

Hai mảng phải có cùng số lượng phần tử.


## 4. Biểu đồ Actual vs Predicted

Sử dụng Matplotlib để tạo biểu đồ scatter.

Thiết lập:

- Trục X: `Actual Magnitude`
- Trục Y: `Predicted Magnitude`
- Mỗi điểm biểu diễn một mẫu dữ liệu.
- Thêm đường tham chiếu `y = x`.

Ý nghĩa:

- Nếu điểm nằm gần đường `y = x`, dự đoán gần với giá trị thực tế.
- Nếu điểm nằm xa đường `y = x`, sai số dự đoán lớn hơn.


## 5. Thư viện được phép sử dụng

Sử dụng:

import matplotlib.pyplot as plt
import numpy as np

Không sử dụng:

- Seaborn.
- Scikit-learn.
- Các thư viện Machine Learning khác.

## 6. Hàm cần tạo

Tạo hàm:

plot_actual_vs_predicted(y_true, y_pred)


Hàm phải thực hiện:

1. Chuyển dữ liệu đầu vào thành NumPy array nếu cần.
2. Kiểm tra `y_true` và `y_pred` có cùng kích thước.
3. Tạo scatter plot.
4. Vẽ đường tham chiếu `y = x`.
5. Đặt tiêu đề.
6. Đặt tên trục X.
7. Đặt tên trục Y.
8. Hiển thị biểu đồ.

## 7. Xử lý dữ liệu đầu vào

Nếu: len(y_true) != len(y_pred) thì báo lỗi phù hợp.

Không được âm thầm bỏ bớt dữ liệu.

## 8. Đường tham chiếu y = x

Đường tham chiếu phải đi qua các điểm:

(x, x)

Đường này dùng để biểu diễn trường hợp:

Actual = Predicted

Các điểm dữ liệu càng gần đường này thì dự đoán càng gần giá trị thực tế.

## 9. Kiểm thử
Trong:

src/visualization.py

tạo phần kiểm thử khi chạy trực tiếp file.

Sử dụng dữ liệu giả định:

y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.2, 1.8, 3.1, 3.9, 5.2])

Sau đó gọi:

plot_actual_vs_predicted(y_true, y_pred)

Chạy file:

python src/visualization.py

Kiểm tra biểu đồ có hiển thị đúng hay không.


## 10. Tiêu chí hoàn thành

Task được xem là hoàn thành khi:

- `src/visualization.py` được tạo.
- Có hàm `plot_actual_vs_predicted()`.
- Biểu đồ có trục X là `Actual Magnitude`.
- Biểu đồ có trục Y là `Predicted Magnitude`.
- Có các điểm dữ liệu.
- Có đường tham chiếu `y = x`.
- Có tiêu đề biểu đồ.
- Có kiểm tra kích thước dữ liệu.
- Chạy file không xảy ra lỗi.
- Biểu đồ hiển thị đúng.

## 11. Không làm trong Task này

Không thực hiện:

- KNN Regression.
- Evaluation metrics.
- Cross-validation.
- Hyperparameter tuning.
- Grid Search.
- Thay đổi preprocessing.
- Thay đổi dataset.
- Thay đổi thuật toán KNN.

Task này chỉ tập trung vào visualization.

## 12. Quy trình Vibe Coding

Thực hiện theo quy trình:

1. Đọc yêu cầu trong file này.
2. Generate code `src/visualization.py`.
3. Review code.
4. Chạy test bằng dữ liệu giả định.
5. Kiểm tra biểu đồ.
6. Sửa lỗi nếu có.
7. Chạy lại test.
8. Chỉ commit sau khi code chạy thành công.

## 13. Prompt cho AI Coding

Sử dụng prompt sau để yêu cầu AI thực hiện Task 07:

Đọc file docs/07_visualization.md.

Hãy thực hiện đúng Task 07 trong file đó.

Tạo src/visualization.py theo đúng yêu cầu.

Sau khi tạo:
1. Review lại code.
2. Kiểm tra hàm plot_actual_vs_predicted().
3. Kiểm tra y_true và y_pred có cùng kích thước.
4. Chạy file bằng dữ liệu giả định.
5. Kiểm tra biểu đồ Actual vs Predicted có hiển thị đúng.
6. Nếu có lỗi thì sửa và chạy lại.
7. Không làm thêm task khác.

Chỉ sử dụng matplotlib và numpy.

## 14. Lệnh kiểm tra

Sau khi AI tạo code, chạy từ thư mục gốc project:

python src/visualization.py

Nếu đúng, một cửa sổ biểu đồ sẽ xuất hiện.

Kiểm tra:

- Có các điểm dữ liệu.
- Trục X là Actual Magnitude.
- Trục Y là Predicted Magnitude.
- Có đường `y = x`.
- Không có lỗi Python.

## 15. Git

git status
git add .
git commit -m "feat: add visualization"
git push
