from src.data_preprocessing import load_data, preprocess_data
from src.anomaly_detection import detect_anomalies, get_anomaly_scores
from src.visualization import plot_anomalies

def main():
    # Load the transaction data
    filepath = 'data/transactions.csv'
    df = load_data(filepath)
    
    # Preprocess the data
    df_preprocessed = preprocess_data(df)

    # Detect anomalies
    df_with_anomalies = detect_anomalies(df_preprocessed)

    # Visualize anomalies
    plot_anomalies(df_with_anomalies)

    # Print out the anomalies
    anomalies = get_anomaly_scores(df_with_anomalies)
    print("Anomalies Detected:")
    print(anomalies)

if __name__ == "__main__":
    main()
