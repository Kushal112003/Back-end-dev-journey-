from sklearn.linear_model import LogisticRegression
import joblib

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # 0 = fail, 1 = pass

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')

print("Model trained and saved as model.pkl")
