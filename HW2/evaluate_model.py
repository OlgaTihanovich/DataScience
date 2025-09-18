# evaluate_model.py
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate_model(model, scaler, X_test, y_test):
 
    # Масштабируем тестовые данные
    X_test_scaled = scaler.transform(X_test)
    
    # Предсказания
    y_pred = model.predict(X_test_scaled)
    
    # Метрики
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)
    
    print(f"Точность модели: {accuracy:.2f}")
    print("Матрица истинности:")
    print(cm)
    print("Классификационный отчет:")
    print(cr)
    
    # Можно вернуть результаты для дальнейшего анализа
    return accuracy, cm, cr