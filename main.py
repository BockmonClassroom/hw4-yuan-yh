import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the dataset
df = pd.read_csv("data/Iris.csv")

# Separate features and labels
df_features = df.drop(columns=["Species"])
df_labels = df["Species"]

# Normalizes all columns to have values between 0 and 1
normalized_df = pd.DataFrame(MinMaxScaler().fit_transform(df_features), columns=df_features.columns)
normalized_df["Species"] = df_labels
normalized_df.to_csv("data/iris_normalized.csv", index=False)

# Standardizes all columns to have a mean of 0 and standard deviation of 1
standardized_df = pd.DataFrame(StandardScaler().fit_transform(df_features), columns=df_features.columns)
standardized_df["Species"] = df_labels
standardized_df.to_csv("data/iris_standardized.csv", index=False)