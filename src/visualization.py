# src/visualization.py

import numpy as np
import matplotlib.pyplot as plt

def plot_actual_vs_predicted(y_true, y_pred):
    """
    Vẽ biểu đồ scatter Actual vs Predicted cho giá trị magnitude.
    
    Tham số:
        y_true (array-like): Giá trị thực tế.
        y_pred (array-like): Giá trị dự đoán.
    """
    # Chuyển dữ liệu thành NumPy array
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Kiểm tra kích thước dữ liệu
    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("y_true và y_pred phải có cùng số lượng phần tử.")

    # Tạo scatter plot
    plt.scatter(y_true, y_pred, color="blue", alpha=0.6, label="Dữ liệu")

    # Vẽ đường tham chiếu y = x
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], color="red", linestyle="--", label="y = x")

    # Thiết lập tiêu đề và tên trục
    plt.title("Actual vs Predicted Magnitude (KNN Regression)")
    plt.xlabel("Actual Magnitude")
    plt.ylabel("Predicted Magnitude")
    plt.legend()

    # Hiển thị biểu đồ
    plt.show()


# Kiểm thử khi chạy trực tiếp file
if __name__ == "__main__":
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.2, 1.8, 3.1, 3.9, 5.2])

    print("=== Kiểm thử Visualization ===")
    print("y_true:", y_true)
    print("y_pred:", y_pred)

    plot_actual_vs_predicted(y_true, y_pred)
