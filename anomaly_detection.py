from sklearn.ensemble import IsolationForest

def detect_anomalies(df, contamination=0.01):
    # Initialize the Isolation Forest model
    iso_forest = IsolationForest(contamination=contamination, random_state=42)
    
    # Fit the model and predict anomalies (-1 for anomaly, 1 for normal)
    df['anomaly'] = iso_forest.fit_predict(df)
    
    # Return the dataframe with anomaly labels
    return df

def get_anomaly_scores(df):
    # Extract anomaly scores
    return df.loc[df['anomaly'] == -1]
