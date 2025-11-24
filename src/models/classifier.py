import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
from pathlib import Path
from typing import Tuple, Dict, Optional
import json


class InstrumentClassifier:
    def __init__(self, n_estimators: int = 100, random_state: int = 42):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=random_state,
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            class_weight='balanced'
        )
        self.label_encoder = LabelEncoder()
        self.is_trained = False
        self.feature_importance = None
    
    def train(self, X: np.ndarray, y: np.ndarray, validation_split: float = 0.2) -> Dict:
        y_encoded = self.label_encoder.fit_transform(y)
        
        X_train, X_val, y_train, y_val = train_test_split(
            X, y_encoded, test_size=validation_split, random_state=42, stratify=y_encoded
        )
        
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        self.feature_importance = self.model.feature_importances_
        
        train_pred = self.model.predict(X_train)
        val_pred = self.model.predict(X_val)
        
        train_accuracy = accuracy_score(y_train, train_pred)
        val_accuracy = accuracy_score(y_val, val_pred)
        
        cv_scores = cross_val_score(self.model, X, y_encoded, cv=5)
        
        results = {
            'train_accuracy': float(train_accuracy),
            'validation_accuracy': float(val_accuracy),
            'cv_mean': float(np.mean(cv_scores)),
            'cv_std': float(np.std(cv_scores)),
            'confusion_matrix': confusion_matrix(y_val, val_pred).tolist(),
            'classification_report': classification_report(
                y_val, val_pred, target_names=self.label_encoder.classes_, output_dict=True
            )
        }
        
        return results
    
    def predict(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        if not self.is_trained:
            raise ValueError("Model has not been trained yet")
        
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)
        
        labels = self.label_encoder.inverse_transform(predictions)
        
        return labels, probabilities
    
    def predict_single(self, features: np.ndarray) -> Dict:
        if features.ndim == 1:
            features = features.reshape(1, -1)
        
        labels, probabilities = self.predict(features)
        
        result = {
            'predicted_instrument': labels[0],
            'confidence': float(np.max(probabilities[0])),
            'all_probabilities': {
                instrument: float(prob) 
                for instrument, prob in zip(self.label_encoder.classes_, probabilities[0])
            }
        }
        
        return result
    
    def save_model(self, model_path: str):
        model_data = {
            'model': self.model,
            'label_encoder': self.label_encoder,
            'feature_importance': self.feature_importance
        }
        joblib.dump(model_data, model_path)
    
    def load_model(self, model_path: str):
        model_data = joblib.load(model_path)
        self.model = model_data['model']
        self.label_encoder = model_data['label_encoder']
        self.feature_importance = model_data.get('feature_importance')
        self.is_trained = True
    
    def get_feature_importance(self, feature_names: list, top_n: int = 20) -> Dict:
        if self.feature_importance is None:
            raise ValueError("Model has not been trained yet")
        
        importance_dict = {
            name: float(importance) 
            for name, importance in zip(feature_names, self.feature_importance)
        }
        
        sorted_importance = sorted(
            importance_dict.items(), key=lambda x: x[1], reverse=True
        )
        
        return dict(sorted_importance[:top_n])
