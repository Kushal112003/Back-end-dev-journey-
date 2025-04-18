from sklearn.linear_model import LogisticRegression
import joblib

# 1. Sample data
# X = hours studied, y = pass or fail
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # 0 = fail, 1 = pass

# 2. Create and train model
model = LogisticRegression()
model.fit(X, y)

# 3. Save the trained model
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")
