import pandas as pd
import matplotlib.pyplot as plt
import os

# Create plots folder
os.makedirs("plots", exist_ok=True)

# Load CSV
df = pd.read_csv("data/final_decision_task.csv")
options = ["Option 1", "Option 2", "Option 3"]

# Scatter Plot
plt.figure(figsize=(8,4))
for option in options:
    subset = df[df['choice']==option]
    colors = subset['reward'].apply(lambda x: (0, 0, min(1, max(0, (x+5)/15))))
    plt.scatter(subset['trial'], subset['EEG_simulated'], s=subset['RT_sec']*100, 
                c=list(colors), label=option, alpha=0.7)

plt.title("Simulated EEG per Choice (Marker size = RT, Color = Reward)")
plt.xlabel("Trial")
plt.ylabel("EEG (simulated units)")
plt.xticks(df['trial'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/eeg_scatter.png")
plt.show()
