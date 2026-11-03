import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_excel(r"C:/Users/Bhabuk/Downloads/Final Plot and Results-Research/Result_Data/1.Calibation_Result_Data.xlsx")


obs=df["Observed Discharge"]
hbv=df["HBV Simulated"]
hec=df["HEC-HMS Simulated"]

HBV_NSE =  1 - sum((obs - hbv)**2) / sum((obs - obs.mean())**2)
HEC_HMS_NSE =  1 - sum((obs - hec)**2) / sum((obs - obs.mean())**2)

print("NSE of HBV is:",HBV_NSE)
print("NSE of HEC-HMS is:",HEC_HMS_NSE)


plt.figure(figsize=(12,6))
plt.plot(df["Date"],df["Observed Discharge"], label="Observed Discharge")
plt.plot(df["Date"],df["HBV Simulated"], label="HBV Simulated")
plt.plot(df["Date"],df["HEC-HMS Simulated"], label="HEC-HMS Simulated")

plt.xlabel("Date")
plt.ylabel("Discharge")
plt.title("Hydrograph")
plt.legend()
plt.grid()

plt.show()
