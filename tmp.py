import numpy as np
import pandas as pd


def export_random_data():
    """
    Export random data to a CSV file.
    """
    # Generate random data
    data = {
        "feature1": np.random.rand(10000),
        "feature2": np.random.rand(10000),
        "feature3": np.random.rand(10000),
        "feature4": np.random.rand(10000),
        "feature5": np.random.rand(10000),
        "feature6": np.random.rand(10000),
        "label": np.random.choice(["A", "B", "C"], 10000),
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv("data.csv", index=False)


if __name__ == "__main__":
    export_random_data()
    print("Random data exported to 'data.csv'")
