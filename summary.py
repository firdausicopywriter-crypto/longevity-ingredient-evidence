import pandas as pd

files = {
    "Resveratrol": "resveratrol.csv",
    "NMN": "NMN.csv",
    "Spermidine": "spermidine.csv",
    "Fisetin": "fisetin.csv",
}

rows = []
for name, path in files.items():
    df = pd.read_csv(path)
    late = df[df["Phases"].str.contains("PHASE3|PHASE4", na=False)]
    rows.append({
        "Ingredient": name,
        "Trials": len(df),
        "% Completed": round((df["Study Status"] == "COMPLETED").mean() * 100, 1),
        "Late-stage (Ph3/4)": len(late),
        "Median enrollment (late)": late["Enrollment"].median(),
    })

summary = pd.DataFrame(rows)
print(summary)
summary.to_csv("summary.csv", index=False)