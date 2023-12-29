import warnings
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

warnings.filterwarnings('ignore')

df = pd.read_csv(r"C:\Users\hithardha\Desktop\projects\ml_project\Fraud_Transaction\PS_20174392719_1491204439457_log.csv")

df = df.drop(columns=['step', 'isFlaggedFraud', 'nameOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest'], axis=1)
df['type'] = df['type'].map({'PAYMENT': 1, 'TRANSFER': 4, 'CASH_OUT': 2, 'DEBIT': 5, 'CASH_IN': 3})

X = df.drop("isFraud", axis=1)
y = df['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

import pickle
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

