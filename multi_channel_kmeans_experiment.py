"""
Script to demonstrate k-means improvements through use of multiple channels.

Use "multi_channel_kmeans.py" instead, this was just an initial test script.

This script can be deleted.

"""

import pandas as pd
import numpy as np
from pathlib import Path
import os

os.environ["OMP_NUM_THREADS"] = "1"  # to avoid warning about threading in sklearn

DEFAULT_CROP = "Winter_Barley"

DEFAULT_INPUTS = {
    "VH_amplitude_asc": f"{DEFAULT_CROP}_result/VH_amplitude_Ascending_monthly.xlsx",
    "VV_amplitude_asc": f"{DEFAULT_CROP}_result/VV_amplitude_Ascending_monthly.xlsx",
    "VH_amplitude_desc": f"{DEFAULT_CROP}_result/VH_amplitude_Descending_monthly.xlsx",
    "VV_amplitude_desc": f"{DEFAULT_CROP}_result/VV_amplitude_Descending_monthly.xlsx",
    "VH_coherence_asc": f"{DEFAULT_CROP}_result/VH_coherence_Ascending_monthly.xlsx",
    "VV_coherence_asc": f"{DEFAULT_CROP}_result/VV_coherence_Ascending_monthly.xlsx",
    "VH_coherence_desc": f"{DEFAULT_CROP}_result/VH_coherence_Descending_monthly.xlsx",
    "VV_coherence_desc": f"{DEFAULT_CROP}_result/VV_coherence_Descending_monthly.xlsx",
}


class Channel:
    def __init__(self, name: str, filepath: str | Path, description: str = ""):
        self.name = name
        if isinstance(filepath, str):
            filepath = Path(filepath)
        self.filepath = filepath
        self.description = description
        self.load_data()

    def load_data(self):
        if self.filepath.suffix == ".xlsx" or self.filepath.suffix == ".xls":
            raw_data = pd.read_excel(self.filepath)
        elif self.filepath.suffix == ".csv":
            raw_data = pd.read_csv(self.filepath)
        else:
            raise ValueError("{self.filepath} - Data must be in Excel or CSV format")

        self.columns = raw_data.columns
        date_column = self.find_date_column()
        self.dates: pd.Series[pd.Timestamp] = pd.to_datetime(raw_data[date_column])
        mean_key, std_key = self.get_stats_columns()

        self.means: pd.Series[float] = raw_data[mean_key]
        self.stds: pd.Series[float] = raw_data[std_key]

        print(f"Max mean: {self.means.max()} for {self.name}")

    def find_date_column(self) -> str:
        columns_lowercase = [column.lower() for column in self.columns]
        ACCEPTABLE_DATETIME_COLUMNS = ["date", "year_month"]

        date_column = None
        for column in columns_lowercase:
            if column in ACCEPTABLE_DATETIME_COLUMNS:
                date_column = column
                break

        if not date_column:
            raise ValueError(
                "Data must contain a datetime column, using one of these names:"
                f"{ACCEPTABLE_DATETIME_COLUMNS}"
            )

        return date_column

    def get_stats_columns(self) -> tuple[str, str]:
        mean_key = None
        std_key = None
        for column in self.columns:
            if "mean" == column.lower():
                mean_key = column
            if "mean_value" == column.lower():
                mean_key = column
            if "std" == column.lower():
                std_key = column
            if "std_dev_mean" == column.lower():
                std_key = column

        if not mean_key or not std_key:
            raise ValueError(
                "Data must contain columns for mean and standard deviation"
            )

        return mean_key, std_key

    def __repr__(self):
        return f"Channel(name={self.name}, filepath={self.filepath})"


if __name__ == "__main__":
    input_channels = {}
    for name, filepath in DEFAULT_INPUTS.items():
        input_channels[name] = Channel(name, filepath)

    [print(channel) for channel in input_channels.values()]

    # Plot each channel's data on same axis
    import matplotlib.pyplot as plt

    # create shared axis
    mean_fig, mean_ax = plt.subplots()

    # Initialize min and max values for y-axis
    y_min, y_max = float("inf"), float("-inf")

    for channel in input_channels.values():
        mean_ax.plot(channel.dates, channel.means, label=channel.name)
        # Update y-axis limits
        y_min = min(y_min, min(channel.means))
        y_max = max(y_max, max(channel.means))

    # Set y-axis limits
    mean_ax.set_ylim(y_min, y_max)
    mean_ax.legend()
    mean_ax.set_title("Mean values for each channel")

    # Plot each channel's data on same axis
    std_fig, std_ax = plt.subplots()

    # Initialize min and max values for y-axis
    y_min, y_max = float("inf"), float("-inf")

    for channel in input_channels.values():
        std_ax.plot(channel.dates, channel.stds, label=channel.name)
        # Update y-axis limits
        y_min = min(y_min, min(channel.stds))
        y_max = max(y_max, max(channel.stds))

    # Set y-axis limits
    std_ax.set_ylim(y_min, y_max)
    std_ax.legend()
    std_ax.set_title("Standard deviation values for each channel")

    # Add a circular variable to represent time of year
    # (e.g. sin and cos of month)
    # This will allow the clustering algorithm to take into account
    # the cyclical nature of the data
    first_channel_key = list(input_channels.keys())[0]
    months = input_channels[first_channel_key].dates

    time_of_year = np.linspace(0, 2 * np.pi, 12)
    sin_time = np.sin(time_of_year)
    cos_time = np.cos(time_of_year)

    # Plot sin and cos of time of year
    fig, ax = plt.subplots()
    ax.plot(sin_time, label="sin(time)")
    ax.plot(cos_time, label="cos(time)")
    ax.legend()
    ax.set_title("Sin and Cos of time of year")

    # Combine all of the channels into a single dataframe
    all_channels = pd.DataFrame()
    for channel in input_channels.values():
        all_channels[channel.name] = channel.means

    all_channels["sin_time"] = sin_time
    all_channels["cos_time"] = cos_time

    # get the principal components of the data
    from sklearn.decomposition import PCA

    pca = PCA(n_components=len(all_channels.columns))
    all_channels_pca = pca.fit_transform(all_channels)

    # plot the principal components against month
    pca_fig, pca_ax = plt.subplots()
    for i in range(all_channels_pca.shape[1]):
        pca_ax.plot(months, all_channels_pca[:, i], label=f"PC{i}")

    pca_ax.legend()
    pca_ax.set_title("Principal components of data")

    # Find the significant principal components
    explained_variance = pca.explained_variance_ratio_
    significant_components = np.where(explained_variance > 0.05)[0]

    # Plot the significant principal components against month
    significant_pca_fig, significant_pca_ax = plt.subplots()
    for i in significant_components:
        significant_pca_ax.plot(months, all_channels_pca[:, i], label=f"PC{i}")

    significant_pca_ax.legend()
    significant_pca_ax.set_title("Significant principal components of data")

    # normalise the data
    all_channels = (all_channels - all_channels.mean()) / all_channels.std()

    # Perform k-means clustering on the combined data
    from sklearn.cluster import KMeans

    NUM_CLUSTERS = 4
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=2).fit(all_channels)

    # Plot the clusters against month
    kmean_fig, kmean_ax = plt.subplots()
    kmean_ax.scatter(months, kmeans.labels_, label="Cluster", c=kmeans.labels_)
    # Legend for clusters
    kmean_ax.legend()
    # Plot the PC1 against month to show the clusters better
    kmean_ax.plot(
        months,
        (all_channels_pca[:, 0] + 1.0) * NUM_CLUSTERS / 2.0,
        label=f"(PC1 + 1) * {NUM_CLUSTERS} / 2",
        color="k",
    )

    # Legend
    kmean_ax.legend()
    kmean_ax.set_title("K-means clusters")

    # Now instead of normalising the data, we will use the significant PCA components
    significant_components_data = all_channels_pca[:, significant_components]

    # Perform k-means clustering on the significant PCA components
    kmeans_pca = KMeans(n_clusters=NUM_CLUSTERS, random_state=2).fit(
        significant_components_data
    )
    kmean_fig2, kmean_ax2 = plt.subplots()
    kmean_ax2.scatter(months, kmeans_pca.labels_, label="Cluster", c=kmeans_pca.labels_)
    kmean_ax2.legend()  # Legend for clusters
    # Plot the significant PCA components against month to show the clusters better
    for i in significant_components:
        kmean_ax2.plot(months, all_channels_pca[:, i], label=f"PC{i}")

    # Legend
    kmean_ax2.legend()
    kmean_ax2.set_title("K-means clusters using significant PCA components")

    plt.show()
