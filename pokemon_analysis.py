#!!!!! This is a prototype, everything might receive changes later on to scale it 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokedex-project/Pokemon.csv")

#Data Cleaning
"""""
Dropped this because I went for another strategy, selecting only 1 for each poke in the pokedex using their numbers

exclude = ["Mega ", " Forme", " Mode"]
filter = ~df["Name"].str.contains("|".join(exclude), na=False)
df_filtered = df[filter]
"""
df_unique = df.drop_duplicates(subset="#", keep="first")

stats =  ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

print(df.head)

#Frecuency check
type1_counts = df["Type 1"].value_counts()
type2_counts = df["Type 2"].value_counts()

#Visualization
plt.figure(figsize=(10,5))

#Common 1rst type plt
sns.barplot(x=type1_counts.index, y=type1_counts.values, palette="viridis")

plt.title("Most Common Pokemon Types (Type 1)")
plt.ylabel("Qty")
plt.xlabel("Type")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Common 2nd type
plt.figure(figsize=(10,5))

sns.barplot(x=type2_counts.index, y=type2_counts.values, palette="dark")

plt.title("Most Common Pokemon Types (Type 2)")
plt.ylabel("Qty")
plt.xlabel("Type")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Stats ckeck (No graph, might add later)

while True:
    print("Select The Stat's Top 5 You Want To Check")
    for i, stat in enumerate(stats):
        print(f"{i+1}. {stat}")
    print("0. Quit")
    
    try:
        choice = int(input("\n Type your Selection"))
        if choice == 0:
            print("Stat Check Done")
            break
        elif 1 <= choice <= len(stats):
            selected_stat = stats[choice-1]
            print(f"\nTop 5 Pokemon With More {selected_stat}:")
            print(df[["Name", selected_stat]].sort_values(by=selected_stat, ascending=False).head())
        else:
            print("Incorrect Option")
    except ValueError:
        print("Please, select a number")

#Generation Amount of Pokemon

plt.figure(figsize=(10,5))
sns.countplot(x="Generation", data=df_unique, palette="muted")

plt.title("Amount of Pokemon by Generation")
plt.xlabel("Generation")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

"""""
#Just Checking the df_unique cleaning

gen = 1
count = df_unique[df_unique["Generation"] == gen].shape[0]
print(f"Amount of Pokemon in Gen {gen}: {count}")
"""

#How Different are legendaries
plt.figure(figsize=(10, 5))

sns.boxplot(x="Legendary", y="Attack", data= df)

plt.title("Atk Distribution If It's Legendary")
plt.xlabel("Legendary(True) or Not(False)")
plt.ylabel("Attack")
plt.tight_layout()
plt.show()

#Stats Correlation
plt.figure(figsize=(10, 5))
sns.heatmap(df[stats].corr(),annot=True, cmap="coolwarm")
plt.tight_layout()
plt.show()