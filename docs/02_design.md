# DESIGN - KNN Regression

## 1. Mục tiêu thiết kế

Thiết kế một chương trình KNN Regression đơn giản, dễ hiểu và phù hợp cho việc học tập, trình bày trong khoảng 5 phút.

Thuật toán KNN Regression phải được tự cài đặt, không sử dụng mô hình KNN có sẵn từ thư viện Machine Learning.

## 2. Project Structure

Cấu trúc dự kiến:

KNN_Regression/
│
├── data/
│   └── earthquake.csv
│
├── docs/
│   ├── 01_define.md
│   ├── 02_design.md
│   ├── 03_data_loading.md
│   ├── 04_preprocessing.md
│   ├── 05_knn_regression.md
│   ├── 06_evaluation.md
│   └── 07_visualization.md
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── knn_regression.py
│   ├── metrics.py
│   ├── visualization.py
│   └── main.py
│
├── README.md
└── requirements.txt

## 3. Data Flow

Luồng xử lý của chương trình:

earthquake.csv
      ↓
Load Dataset
      ↓
Select Features + Target
      ↓
Remove Missing Values
      ↓
Train / Test Split
      ↓
Feature Scaling
      ↓
KNN Regression
      ↓
Prediction
      ↓
Evaluation
      ↓
Visualization

## 4. Module Design

### 4.1. data_loader.py

Nhiệm vụ:

* Đọc file CSV.
* Kiểm tra dataset đã được đọc thành công.
* Trả về dữ liệu cho các module tiếp theo.

Không thực hiện thuật toán KNN trong module này.

### 4.2. preprocessing.py

Nhiệm vụ:

* Chọn 9 features:
latitude
longitude
depth
nst
gap
dmin
rms
horizontalError
depthError

* Chọn target: mag
* Loại bỏ các dòng chứa giá trị thiếu.
* Tách:
X = features
y = mag

* Chia dữ liệu thành tập train và test.
* Chuẩn hóa features.

Việc chuẩn hóa phải được thực hiện dựa trên tập train để tránh data leakage.


## 5. Train/Test Split

Dữ liệu được chia thành:

Training Set: 80%
Testing Set: 20%

Training Set được sử dụng để tìm các hàng xóm gần nhất.

Testing Set được sử dụng để đánh giá khả năng dự đoán của mô hình.

Việc chia dữ liệu phải có `random_state` cố định để kết quả có thể tái lập.

## 6. Feature Scaling

KNN dựa trên khoảng cách nên các feature cần được đưa về cùng thang đo.

Sử dụng Standardization:

z = (x - mean) / standard_deviation

Trong đó:

* `x`: giá trị ban đầu.
* `mean`: giá trị trung bình của feature trên tập train.
* `standard_deviation`: độ lệch chuẩn của feature trên tập train.
* `z`: giá trị sau chuẩn hóa.

Mean và standard deviation chỉ được tính từ tập train.

Sau đó sử dụng các giá trị này để chuẩn hóa cả train và test.

## 7. KNN Regression Design

### 7.1. Input

Một mẫu cần dự đoán:

x_test và X_train; y_train ;K

### 7.2. Euclidean Distance

Khoảng cách Euclidean giữa hai điểm:
distance =sqrt((x1 - y1)^2 +(x2 - y2)^2 +....(xn - yn)^2)

Trong Python có thể triển khai bằng vòng lặp.

Không sử dụng hàm KNN có sẵn.

### 7.3. Tìm K hàng xóm gần nhất

Đối với mỗi mẫu test:

1. Tính khoảng cách đến tất cả mẫu train.
2. Lưu khoảng cách cùng với giá trị `mag`.
3. Sắp xếp theo khoảng cách tăng dần.
4. Chọn `K` mẫu đầu tiên.

Ví dụ:
K = 3

Neighbor 1 → mag = 4.5
Neighbor 2 → mag = 4.2
Neighbor 3 → mag = 4.8

### 7.4. Prediction

KNN Regression dự đoán bằng trung bình giá trị target của K hàng xóm:

prediction = (mag1 + mag2 + ... + magK) / K
Ví dụ:
K = 3

mag1 = 4.5
mag2 = 4.2
mag3 = 4.8

prediction = (4.5 + 4.2 + 4.8) / 3 = 4.5

## 8. K Value

Ban đầu sử dụng:

K = 5

để làm mô hình chính và demo.

Có thể thử thêm:

K = 3
K = 7
K = 9

để minh họa ảnh hưởng của K.

Không cần thực hiện tìm kiếm K phức tạp vì bài trình bày chỉ khoảng 5 phút.

## 9. Evaluation Design

Các metric được sử dụng:

### MAE

Đo sai số tuyệt đối trung bình:

MAE = mean(|y_actual - y_predicted|)

MAE càng nhỏ càng tốt.

### MSE

Đo trung bình bình phương sai số:

MSE = mean((y_actual - y_predicted)^2)

MSE càng nhỏ càng tốt.

### RMSE

Căn bậc hai của MSE:

RMSE = sqrt(MSE)

RMSE càng nhỏ càng tốt.

### R²

Đánh giá mức độ mô hình giải thích sự biến thiên của target.

R² càng gần 1 thì mô hình càng phù hợp với dữ liệu.

## 10. Visualization Design

Tạo biểu đồ:

### Actual vs Predicted

* Trục X: giá trị `mag` thực tế.
* Trục Y: giá trị `mag` dự đoán.

Mục đích:

* Giúp người xem dễ dàng quan sát kết quả.
* So sánh giá trị thực tế và dự đoán.
* Hỗ trợ phần demo trong bài thuyết trình.

## 11. Main Program

`main.py` chịu trách nhiệm điều phối toàn bộ chương trình.

Luồng chính:

1. Load dataset
       ↓
2. Preprocess dataset
       ↓
3. Split train/test
       ↓
4. Scale features
       ↓
5. Create KNN Regression
       ↓
6. Train / store training data
       ↓
7. Predict test data
       ↓
8. Calculate metrics
       ↓
9. Display results
       ↓
10. Display visualization

## 12. Technology Constraints

Được sử dụng:
Python
Pandas
NumPy
Matplotlib

Không được sử dụng:

KNeighborsRegressor

Không sử dụng bất kỳ thư viện nào cung cấp trực tiếp thuật toán KNN Regression.

Các thành phần cốt lõi của KNN phải được tự cài đặt:
Euclidean Distance
Find K Neighbors
Prediction

Các metric đánh giá cũng nên được tự cài đặt để dễ giải thích thuật toán trong bài thuyết trình.

## 13. Vibe Coding Workflow

Mỗi module được phát triển thành một nhiệm vụ nhỏ.

Quy trình:
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
Git Commit

Không phát triển toàn bộ project trong một prompt duy nhất.

Mỗi nhiệm vụ phải có file `.md` tương ứng trong thư mục `docs/`.

Chỉ chuyển sang nhiệm vụ tiếp theo sau khi nhiệm vụ hiện tại đã chạy và kiểm tra thành công.

## 14. Development Order

Thứ tự phát triển:
01. Define
      ↓
02. Design
      ↓
03. Data Loading
      ↓
04. Preprocessing
      ↓
05. KNN Regression
      ↓
06. Evaluation
      ↓
07. Visualization
      ↓
08. Main Program

Mỗi bước phải được kiểm tra trước khi chuyển sang bước tiếp theo.

## 15. Git Strategy

Sau mỗi phần hoàn thành và kiểm tra thành công, tạo một commit riêng.

Ví dụ:

git add .
git commit -m "feat: add data loading"

Các commit tiếp theo:
feat: add preprocessing
feat: add train test split
feat: implement knn regression
feat: add evaluation metrics
feat: add visualization
feat: add main program