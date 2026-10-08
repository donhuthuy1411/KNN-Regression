# src/data_loader.py

import os
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Hàm đọc dữ liệu từ file CSV và trả về DataFrame.
    Đồng thời kiểm tra thông tin cơ bản của dataset.
    
    Tham số:
        file_path (str): Đường dẫn đến file CSV.
    
    Trả về:
        pd.DataFrame: DataFrame chứa dữ liệu đọc được.
    """
    # Kiểm tra file có tồn tại hay không
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Không tìm thấy file: {file_path}")
    
    # Đọc dữ liệu bằng pandas
    df = pd.read_csv(file_path)
    
    # Kiểm tra dữ liệu cơ bản
    print("=== Thông tin dataset ===")
    print(f"Shape (dòng, cột): {df.shape}")
    print("\nTên các cột:")
    print(df.columns.tolist())
    print("\nKiểu dữ liệu của các cột:")
    print(df.dtypes)
    print("\nSố lượng giá trị thiếu ở mỗi cột:")
    print(df.isnull().sum())
    
    return df

# Nếu chạy trực tiếp file này, kiểm tra với dataset thật
if __name__ == "__main__":
    data_path = "data/earthquake.csv"
    df = load_data(data_path)
