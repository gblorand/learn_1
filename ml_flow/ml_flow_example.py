import mlflow
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate random data
X, y = np.random.rand(100, 5), np.random.randint(2, size=100)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start a new MLflow run
with mlflow.start_run():
    # Log parameters
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("num_epochs", 100)

    # Create and train a model
    model = LogisticRegression(max_iter=100, random_state=42)
    for epoch in range(1, 101):
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Log metrics
        mlflow.log_metrics({"accuracy": accuracy}, step=epoch)

    # Save the trained model
    model_path = "trained_model"
    mlflow.sklearn.save_model(model, model_path)

    # Log the saved model as an artifact
    mlflow.log_artifacts(model_path)
