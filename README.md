
#Cognitive Decision Simulation

Repository Name: cognitive_decision_simulation

Description:
Python-based simulation of a cognitive neuroscience decision-making task. This project generates synthetic EEG data influenced by stress and reward, simulates participant choices and reaction times, and produces visualizations including scatter plots and boxplots. All data and plots are saved for further analysis.

Folder Structure:
cognitive_decision_simulation/
│
├─ code/
│   ├─ main.py                 ← Main file to run the full simulation
│   ├─ generate_data.py        ← Generates CSV data
│   ├─ scatter_plot.py         ← Generates and saves scatter plot
│   └─ boxplot.py              ← Generates and saves boxplot
│
├─ data/                       ← Stores CSV files
│   └─ final_decision_task.csv
│
└─ plots/                      ← Stores plot images
    ├─ eeg_scatter.png
    └─ eeg_boxplot.png

Requirements:
•	Python 3.x
•	pandas
•	matplotlib
You can install required packages using:
pip install pandas matplotlib

How to Run:
Run the main simulation:
python main.py
After running, you will find:
•	CSV data in data/final_decision_task.csv
•	Scatter plot in plots/eeg_scatter.png
•	Boxplot in plots/eeg_boxplot.png

Project Details:
•	generate_data.py: Creates simulated trials with randomized stress levels, choices, reaction times, and EEG signals influenced by stress and reward.
•	scatter_plot.py: Creates scatter plot of EEG vs trial number, marker size = RT, color = reward.
•	boxplot.py: Creates boxplot of EEG distribution per choice.
•	main.py: Runs the full simulation and calls all other scripts automatically.

Purpose:
This repository is designed for cognitive neuroscience research simulations. It allows for:
•	Testing decision-making tasks virtually
•	Generating synthetic EEG and behavioral datasets
•	Visualizing results with customizable plots
•	Easy integration into further experiments or analysis

