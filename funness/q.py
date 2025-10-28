import pandas as pd

# Automate Excel reports for clients
df = pd.read_excel("sales.xlsx")
summary = df.groupby("Region")["Revenue"].sum().reset_index()
summary.to_excel("summary_report.xlsx", index=False)

print("Report generated successfully!")
