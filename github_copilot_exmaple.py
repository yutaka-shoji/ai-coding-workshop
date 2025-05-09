import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_iris_scatter(df: pd.DataFrame, feature1: str, feature2: str) -> None:
    """
    Plot scatter of the iris dataset.
    """
    ...  # TODO: Implement this function


def main():
    # load iris dataset
    df = sns.load_dataset("iris")

    # scatter plot
    plot_iris_scatter(df, "petal_length", "petal_width")


if __name__ == "__main__":
    main()
