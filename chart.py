import pandas as pd
import matplotlib.pyplot as plt

s = pd.read_csv("summary.csv")
x = list(range(len(s)))

plt.figure(figsize=(8, 5))
plt.bar([i - 0.2 for i in x], s["Trials"], width=0.4, label="All registered trials")
plt.bar([i + 0.2 for i in x], s["Late-stage (Ph3/4)"], width=0.4, label="Phase 3/4 trials")
plt.xticks(x, s["Ingredient"])
plt.ylabel("Number of trials")
plt.title("Longevity ingredients: registered vs late-stage trials")
plt.legend()
plt.tight_layout()
plt.savefig("chart.png", dpi=200)