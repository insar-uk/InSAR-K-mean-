"""
multi_channel_kmeans.py

Script to demonstrate k-means improvements through use of multiple channels.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

os.environ["OMP_NUM_THREADS"] = "1"  # to avoid warning about threading in sklearn


## USER SETTINGS ##
# --------------------------------------------------------------------------- #

# Set to True to show all plot windows at the end of the script, rather than one by one
SHOW_PLOTS_AT_END = True

# Specify which directory the crop data is stored in
DEFAULT_CROP_DIRECTORY = "Winter_Barley_result"

# Specify the files we want to load in terms of the channel name and the file path
DEFAULT_INPUTS = {
    "VH_amplitude_asc": f"{DEFAULT_CROP_DIRECTORY}/VH_amplitude_Ascending_monthly.xlsx",
    "VV_amplitude_asc": f"{DEFAULT_CROP_DIRECTORY}/VV_amplitude_Ascending_monthly.xlsx",
    "VH_amplitude_desc": f"{DEFAULT_CROP_DIRECTORY}/VH_amplitude_Descending_monthly.xlsx",
    "VV_amplitude_desc": f"{DEFAULT_CROP_DIRECTORY}/VV_amplitude_Descending_monthly.xlsx",
    "VH_coherence_asc": f"{DEFAULT_CROP_DIRECTORY}/VH_coherence_Ascending_monthly.xlsx",
    "VV_coherence_asc": f"{DEFAULT_CROP_DIRECTORY}/VV_coherence_Ascending_monthly.xlsx",
    "VH_coherence_desc": f"{DEFAULT_CROP_DIRECTORY}/VH_coherence_Descending_monthly.xlsx",
    "VV_coherence_desc": f"{DEFAULT_CROP_DIRECTORY}/VV_coherence_Descending_monthly.xlsx",
}

# These are the names of the datetime column in your data
ACCEPTABLE_DATETIME_COLUMNS = ["date", "year_month"]

# Number of clusters to use in k-means
NUM_CLUSTERS = 4

# --------------------------------------------------------------------------- #


class Channel:
    """
    Helper class for loading and formatting your excel or csv files
    """
    def __init__(self, name: str, filepath: str | Path, description: str = ""):
        self.name = name
        self.filepath = Path(filepath) if isinstance(filepath, str) else filepath
        self.description = description
        self.load_data()

    def load_data(self):
        raw_data = self._read_data()
        self.columns = raw_data.columns
        date_column = self._find_date_column()
        self.dates: pd.Series[pd.Timestamp] = pd.to_datetime(raw_data[date_column])
        mean_key, std_key = self._get_stats_columns()

        self.means: pd.Series[float] = raw_data[mean_key]
        self.stds: pd.Series[float] = raw_data[std_key]

    def _read_data(self) -> pd.DataFrame:
        if self.filepath.suffix in [".xlsx", ".xls"]:
            return pd.read_excel(self.filepath)
        elif self.filepath.suffix == ".csv":
            return pd.read_csv(self.filepath)
        else:
            raise ValueError(f"{self.filepath} - Data must be in Excel or CSV format")

    def _find_date_column(self) -> str:
        columns_lowercase = [column.lower() for column in self.columns]
        for column in columns_lowercase:
            if column in ACCEPTABLE_DATETIME_COLUMNS:
                return column
        raise ValueError(
            f"Data must contain a datetime column, using one of these names: {ACCEPTABLE_DATETIME_COLUMNS}"
        )

    def _get_stats_columns(self) -> tuple[str, str]:
        mean_key = next(
            (col for col in self.columns if col.lower() in ["mean", "mean_value"]), None
        )
        std_key = next(
            (col for col in self.columns if col.lower() in ["std", "std_dev_mean"]),
            None,
        )
        if not mean_key or not std_key:
            raise ValueError(
                "Data must contain columns for mean and standard deviation"
            )
        return mean_key, std_key

    def __repr__(self):
        return f"Channel(name={self.name}, filepath={self.filepath})"


def plot_data(channels, attribute, title):
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)  # type: ignore
    y_min, y_max = float("inf"), float("-inf")
    for channel in channels.values():
        data = getattr(channel, attribute)
        ax.plot(channel.dates, data, label=channel.name)
        y_min, y_max = min(y_min, min(data)), max(y_max, max(data))
    ax.set_ylim(y_min, y_max)
    ax.legend()
    ax.set_title(title)
    if not SHOW_PLOTS_AT_END:
        plt.show()


def plot_normalised_data(normalised_data, title="normalised data"):
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)  # type: ignore
    for channel in normalised_data.columns:
        ax.plot(normalised_data.index, normalised_data[channel], label=channel)
    ax.legend()
    ax.set_title("normalised data")
    if not SHOW_PLOTS_AT_END:
        plt.show()


def plot_time_of_year(title="Sin and Cos of time of year"):
    time_of_year = np.linspace(0, 2 * np.pi, 12)
    sin_time, cos_time = np.sin(time_of_year), np.cos(time_of_year)
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)  # type: ignore
    ax.plot(sin_time, label="sin(time)")
    ax.plot(cos_time, label="cos(time)")
    ax.legend()
    ax.set_title("Sin and Cos of time of year")
    if not SHOW_PLOTS_AT_END:
        plt.show()
    return sin_time, cos_time


def combine_channels(channels, sin_time, cos_time):
    all_channels = pd.DataFrame(
        {channel.name: channel.means for channel in channels.values()}
    )
    all_channels["sin_time"], all_channels["cos_time"] = sin_time, cos_time
    return all_channels


def perform_pca(data):
    pca = PCA(n_components=data.shape[1])
    pca_data = pca.fit_transform(data)
    return pca, pca_data


def plot_pca(pca_data, months, title):
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)  # type: ignore
    for i in range(pca_data.shape[1]):
        ax.plot(months, pca_data[:, i], label=f"PC{i}")
    ax.legend()
    ax.set_title(title)
    if not SHOW_PLOTS_AT_END:
        plt.show()


def plot_significant_pca(
    pca_data,
    months,
    significant_components,
    title="Significant principal components of data",
):
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)  # type: ignore
    for i in significant_components:
        ax.plot(months, pca_data[:, i], label=f"PC{i}")
    ax.legend()
    ax.set_title("Significant principal components of data")
    if not SHOW_PLOTS_AT_END:
        plt.show()


def perform_kmeans(data, months, title):
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=2).fit(data)
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)  # type: ignore
    ax.scatter(months, kmeans.labels_, label="Cluster", c=kmeans.labels_)
    ax.legend()
    ax.set_title(title)

    if not SHOW_PLOTS_AT_END:
        plt.show()
    return kmeans


def main():
    input_channels = {
        name: Channel(name, filepath) for name, filepath in DEFAULT_INPUTS.items()
    }
    plot_data(input_channels, "means", "Mean values for each channel")
    plot_data(input_channels, "stds", "Standard deviation values for each channel")

    sin_time, cos_time = plot_time_of_year()
    all_channels = combine_channels(input_channels, sin_time, cos_time)

    normalised_data = (all_channels - all_channels.mean()) / all_channels.std()

    plot_normalised_data(normalised_data)

    pca, all_channels_pca = perform_pca(all_channels)
    plot_pca(
        all_channels_pca,
        input_channels[list(input_channels.keys())[0]].dates,
        "Principal components of data",
    )

    explained_variance = pca.explained_variance_ratio_
    significant_components = np.where(explained_variance > 0.05)[0]
    plot_significant_pca(
        all_channels_pca,
        input_channels[list(input_channels.keys())[0]].dates,
        significant_components,
    )

    perform_kmeans(
        all_channels,
        input_channels[list(input_channels.keys())[0]].dates,
        "K-means clusters using raw data",
    )

    perform_kmeans(
        normalised_data,
        input_channels[list(input_channels.keys())[0]].dates,
        "K-means clusters using normalised data",
    )

    significant_components_data = all_channels_pca[:, significant_components]
    perform_kmeans(
        significant_components_data,
        input_channels[list(input_channels.keys())[0]].dates,
        "K-means clusters using significant PCA components",
    )

    if SHOW_PLOTS_AT_END:
        plt.show()


if __name__ == "__main__":
    main()
