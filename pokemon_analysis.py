import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokedex-project/Pokemon.csv")

print(df.head)

#Frecuency check
type_counts = df["Type 1"].value_counts()

#Visualization
plt.figure(figsize=(10,5))