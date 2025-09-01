import pandas as pd
import matplotlib.pyplot as plt
import os

# Create plots folder
os.makedirs("plots", exist_ok=True)

# Load CSV
df = pd.read_csv("data/final_decision_task.csv")
options = ["Option 1", "Option 2", "Option 3"]

# Boxplot using matplotlib
plt.figure(figsize=(6,4))
data_to_plot = [df[df['choice']==opt]['EEG_simulated'] for opt in options]
plt.boxplot(data_to_plot, labels=options)
plt.title("EEG Distribution per Choice")
plt.ylabel("EEG (simulated units)")
plt.tight_layout()
plt.savefig("plots/eeg_boxplot.png")
plt.show()
