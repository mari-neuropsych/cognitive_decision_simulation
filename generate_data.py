import random
import pandas as pd
import os

# Create data folder
os.makedirs("data", exist_ok=True)

# Experiment parameters
n_trials = 20
options = ["Option 1", "Option 2", "Option 3"]
rewards = [10, 0, -5]

# Store responses
responses = []
for trial in range(n_trials):
    stress_level = round(random.uniform(0.5, 1.5), 3)
    choice = random.randint(0, 2)
    rt = round(random.uniform(0.5, 3.0), 3)
    eeg_simulated = round(random.uniform(0.5, 2.5) * stress_level + rewards[choice]*0.1, 3)
    
    responses.append({
        'trial': trial+1,
        'choice': options[choice],
        'reward': rewards[choice],
        'RT_sec': rt,
        'EEG_simulated': eeg_simulated,
        'stress_level': stress_level
    })

df = pd.DataFrame(responses)
csv_path = "data/final_decision_task.csv"
df.to_csv(csv_path, index=False)
print(f"CSV saved as '{csv_path}'")
