# src/knn_regression.py

import numpy as np


class KNNRegressor:
    def __init__(self, k=5):
        if k <= 0:
            raise ValueError("Tham số k phải lớn hơn 0.")

        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train: np.ndarray, y_train: np.ndarray):
        if X_train.shape[0] != y_train.shape[0]:
            raise ValueError(
                "Số lượng mẫu của X_train và y_train không khớp."
            )

        if self.k > X_train.shape[0]:
            raise ValueError(
                "Tham số k không được lớn hơn số lượng mẫu train."
            )

        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        if self.X_train is None or self.y_train is None:
            raise ValueError(
                "Phải gọi fit() trước khi predict()."
            )

        predictions = []

        for x in X_test:
            # Tính khoảng cách Euclidean
            distances = np.sqrt(
                np.sum((self.X_train - x) ** 2, axis=1)
            )

            # Lấy chỉ số của k điểm gần nhất
            neighbor_idx = np.argsort(distances)[:self.k]

            # Lấy giá trị target của k hàng xóm
            neighbor_values = self.y_train[neighbor_idx]

            # Dự đoán bằng trung bình của k hàng xóm
            prediction = neighbor_values.mean()

            predictions.append(prediction)

        return np.array(predictions)


if __name__ == "__main__":
    from data_loader import load_data
    from preprocessing import preprocess_data

    df = load_data("data/earthquake.csv")

    X_train, X_test, y_train, y_test = preprocess_data(df)

    knn = KNNRegressor(k=5)

    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    print("5 predictions đầu tiên:")
    print(y_pred[:5])

    print("Số lượng prediction:", len(y_pred))
    print("Số lượng mẫu test:", len(X_test))
    print(
        "Prediction có đúng số lượng mẫu test:",
        len(y_pred) == len(X_test)
    )