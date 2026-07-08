"""
=========================================================
CLASSIFIC-AI Base Machine Learning Model
=========================================================

Every Machine Learning model

- Logistic Regression
- SVM
- KNN
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost

will inherit from this class.

This class provides common functionality such as:

1. Train-Test Split
2. Model Training Interface
3. Prediction Interface
4. Evaluation Interface

=========================================================
"""

from abc import ABC, abstractmethod

from sklearn.model_selection import train_test_split


class BaseModel(ABC):
    """
    Parent class for all supervised learning models.
    """

    def __init__(self):
        """
        Initialize model.
        """
        self.model = None

    def split_data(
        self,
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=None
    ):
        """
        Automatically split dataset into train and test sets.
        """

        return train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
            stratify=stratify
        )

    @abstractmethod
    def train(self, X_train, y_train):
        """
        Train the Machine Learning model.
        """
        pass

    @abstractmethod
    def predict(self, X_test):
        """
        Predict using trained model.
        """
        pass

    @abstractmethod
    def evaluate(self, X_test, y_test):
        """
        Evaluate trained model.
        """
        pass