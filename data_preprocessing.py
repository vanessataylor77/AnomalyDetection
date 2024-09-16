import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    # Load the dataset from CSV
    return pd.read_csv(filepath)

def preprocess_data(df):
    # Drop any missing or null values
    df_cleaned = df.dropna()

    # Standardize numeric features
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df_cleaned.select_dtypes(include=['float64', 'int64'])),
                             columns=df_cleaned.select_dtypes(include=['float64', 'int64']).columns)

    # Return the preprocessed data
    return df_scaled
