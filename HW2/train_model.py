# train_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def train_model(X_train, y_train, max_iter=200):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = LogisticRegression(max_iter=max_iter)
    model.fit(X_train_scaled, y_train)

    return model, scaler