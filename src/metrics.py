# src/metrics.py

import numpy as np


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Mean Absolute Error
    MAE = mean(|y_true - y_pred|)
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("y_true và y_pred phải có cùng kích thước.")

    return np.mean(np.abs(y_true - y_pred))


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Mean Squared Error
    MSE = mean((y_true - y_pred)^2)
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("y_true và y_pred phải có cùng kích thước.")

    return np.mean((y_true - y_pred) ** 2)


def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Root Mean Squared Error
    RMSE = sqrt(MSE)
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    R-squared
    R² = 1 - (SS_res / SS_tot)
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("y_true và y_pred phải có cùng kích thước.")

    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)

    if ss_tot == 0:
        raise ValueError("Không thể tính R² khi y_true không có độ biến thiên.")

    return 1 - (ss_res / ss_tot)


if __name__ == "__main__":
    y_true = np.array([3.0, -0.5, 2.0, 7.0])
    y_pred = np.array([2.5, 0.0, 2.0, 8.0])

    print("=== Kiểm tra metrics với dữ liệu giả định ===")
    print("y_true:", y_true)
    print("y_pred:", y_pred)
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("RMSE:", root_mean_squared_error(y_true, y_pred))
    print("R²:", r2_score(y_true, y_pred))