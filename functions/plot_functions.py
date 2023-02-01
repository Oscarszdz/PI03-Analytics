
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_box(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        # plt.subplots()
        sns.boxplot(x=dataframe[i], data=dataframe)
        plt.show()


def plot_count(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        # plt.subplots()
        sns.countplot(x=dataframe[i], data=dataframe)
        plt.show()


def plot_dist(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        # plt.subplots()
        sns.displot(x=dataframe[i], data=dataframe)
        plt.show()


def plot_hist(dataframe: pd.DataFrame):
    for i in dataframe.columns:
        # if dataframe[i].dtype != 'object':
        # plt.subplots()
        sns.histplot(x=dataframe[i], data=dataframe, kde=True)
        plt.show()
