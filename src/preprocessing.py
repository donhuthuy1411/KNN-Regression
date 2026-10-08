# src/preprocessing.py

import numpy as np
import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """
    Thực hiện tiền xử lý dữ liệu cho KNN Regression:
    1. Xóa các dòng có giá trị thiếu.
    2. Tạo X (features) và y (target).
    3. Chia dữ liệu thành train/test theo tỷ lệ 80/20.
    4. Chuẩn hóa dữ liệu bằng thống kê của tập train.
    
    Trả về:
        X_train, X_test, y_train, y_test
    """

    # Các feature cần dùng
    features = [
        "latitude", "longitude", "depth", "nst", "gap", "dmin",
        "rms", "horizontalError", "depthError"
    ]
    target = "mag"

    # Xóa các dòng có giá trị thiếu
    df_clean = df.dropna()

    # Tạo X và y
    X = df_clean[features].values
    y = df_clean[target].values

    # Chia dữ liệu train/test (80/20) bằng numpy
    np.random.seed(42)
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)

    train_size = int(0.8 * X.shape[0])
    train_idx, test_idx = indices[:train_size], indices[train_size:]

    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # Chuẩn hóa dữ liệu (Standardization)
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)

    # Tránh chia cho 0 nếu std = 0
    std[std == 0] = 1

    X_train = (X_train - mean) / std
    X_test = (X_test - mean) / std

    return X_train, X_test, y_train, y_test


# Nếu chạy trực tiếp file này, kiểm tra với dataset thật
if __name__ == "__main__":
    from data_loader import load_data

    df = load_data("data/earthquake.csv")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("=== Kiểm tra kết quả preprocessing ===")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

    print("\nSố lượng giá trị thiếu trong X_train:", np.isnan(X_train).sum())
    print("Số lượng giá trị thiếu trong X_test:", np.isnan(X_test).sum())
    print("Mean (X_train):", X_train.mean(axis=0))
    print("Std (X_train):", X_train.std(axis=0))
