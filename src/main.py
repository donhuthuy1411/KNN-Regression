# src/main.py

from data_loader import load_data
from preprocessing import preprocess_data
from knn_regression import KNNRegressor
from metrics import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error,
    r2_score
)
from visualization import plot_actual_vs_predicted


def main():
    print("=== KNN Regression Pipeline ===")

    # Bước 1 - Load dataset
    data_path = "data/earthquake.csv"
    df = load_data(data_path)

    # Bước 2 - Preprocessing
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print(f"Số lượng mẫu train: {X_train.shape[0]}")
    print(f"Số lượng mẫu test: {X_test.shape[0]}")
    print(f"Số lượng features: {X_train.shape[1]}")
    print("K = 5")

    # Bước 3 - Tạo mô hình KNN
    knn = KNNRegressor(k=5)

    # Bước 4 - Train
    knn.fit(X_train, y_train)

    # Bước 5 - Prediction
    y_pred = knn.predict(X_test)

    # Kiểm tra số lượng prediction
    if len(y_pred) != len(y_test):
        raise ValueError(
            "Số lượng prediction không khớp với số lượng mẫu test."
        )

    print("\n=== Prediction ===")
    print("5 prediction đầu tiên:")
    print(y_pred[:5])

    # Bước 6 - Evaluation
    print("\n=== Evaluation ===")
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("RMSE:", root_mean_squared_error(y_test, y_pred))
    print("R²:", r2_score(y_test, y_pred))

    # Bước 7 - Visualization
    plot_actual_vs_predicted(y_test, y_pred)


if __name__ == "__main__":
    main()