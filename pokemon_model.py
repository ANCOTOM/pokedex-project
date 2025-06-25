#Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('pokedex-project/Pokemon.csv')

#General csv info
#print(df.head()) #Show the first 5 rows
#print(df.info()) #Show dataframe info
#print(df.isnull().sum()) #Show null values

#Show actual columns
#print(df.columns)

#Delete non useful or numeric columns 
df = df.drop(columns=['#', 'Name', 'Type 1', 'Type 2'])

#Convert Legendary into an int variable to predict 
df["Legendary"] = df["Legendary"].astype(int)

X = df.drop(columns=["Legendary"])#Everything except the legendaries / predictor values 
y = df["Legendary"] #Only the legendarys column 

#Shape verification
print("X shape", X.shape)
print("y distribution:\n", y.value_counts())

#Funcion train test split de scikit learn 

#dividir x and y in training(80%) y test(20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )

print("Training:", X_train.shape,)
print("Test:", X_test.shape, y_test.shape)

#model creation
model = RandomForestClassifier(n_estimators=100, random_state=42)

#model training
model.fit(X_train, y_train)

#model check
print("Model trained succesfully")
print(model)

#predictions
y_pred = model.predict(X_test)

#General model Precition
print("Accuracy:", accuracy_score(y_test, y_pred))

#Detailed report: precition, recall and F! for each class
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Confusion matrix
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))