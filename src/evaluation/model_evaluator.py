import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.preprocessing import label_binarize
from typing import Dict, List
import json


class ModelEvaluator:
    def __init__(self):
        self.evaluation_results = {}
    
    def evaluate_predictions(self, y_true: np.ndarray, y_pred: np.ndarray, 
                           class_names: List[str]) -> Dict:
        cm = confusion_matrix(y_true, y_pred)
        report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)
        
        self.evaluation_results = {
            'confusion_matrix': cm.tolist(),
            'classification_report': report,
            'accuracy': float(report['accuracy']),
            'class_names': class_names
        }
        
        return self.evaluation_results
    
    def plot_confusion_matrix(self, cm: np.ndarray, class_names: List[str], 
                            save_path: str = None):
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=class_names, yticklabels=class_names)
        plt.title('Confusion Matrix - Instrument Classification')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return plt
    
    def plot_feature_importance(self, importance_dict: Dict, 
                               save_path: str = None, top_n: int = 20):
        sorted_features = sorted(importance_dict.items(), 
                               key=lambda x: x[1], reverse=True)[:top_n]
        features, importance = zip(*sorted_features)
        
        plt.figure(figsize=(12, 8))
        plt.barh(range(len(features)), importance)
        plt.yticks(range(len(features)), features)
        plt.xlabel('Importance')
        plt.title(f'Top {top_n} Most Important Features')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return plt
    
    def generate_evaluation_report(self, save_path: str = None) -> str:
        if not self.evaluation_results:
            return "No evaluation results available"
        
        report_lines = [
            "=" * 60,
            "ISAN MUSICAL INSTRUMENTS CLASSIFICATION EVALUATION REPORT",
            "=" * 60,
            "",
            f"Overall Accuracy: {self.evaluation_results['accuracy']:.4f}",
            "",
            "Per-Class Performance:",
            "-" * 60
        ]
        
        for class_name in self.evaluation_results['class_names']:
            if class_name in self.evaluation_results['classification_report']:
                metrics = self.evaluation_results['classification_report'][class_name]
                report_lines.append(f"\n{class_name}:")
                report_lines.append(f"  Precision: {metrics['precision']:.4f}")
                report_lines.append(f"  Recall: {metrics['recall']:.4f}")
                report_lines.append(f"  F1-Score: {metrics['f1-score']:.4f}")
                report_lines.append(f"  Support: {int(metrics['support'])}")
        
        report_text = "\n".join(report_lines)
        
        if save_path:
            with open(save_path, 'w') as f:
                f.write(report_text)
        
        return report_text
    
    def save_results(self, save_path: str):
        with open(save_path, 'w') as f:
            json.dump(self.evaluation_results, f, indent=2)
