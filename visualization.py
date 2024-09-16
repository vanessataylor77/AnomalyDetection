import matplotlib.pyplot as plt

def plot_anomalies(df):
    # Visualize anomalies
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, df['transaction_amount'], c=df['anomaly'], cmap='coolwarm', label='Anomalies')
    plt.title('Anomalies in Financial Transactions')
    plt.xlabel('Transaction Index')
    plt.ylabel('Transaction Amount')
    plt.legend()
    plt.show()
