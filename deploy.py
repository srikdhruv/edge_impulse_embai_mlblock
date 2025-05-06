import torch
import torch.nn as nn
import numpy as np
import onnxruntime as ort
import sys
import os

class EdgeImpulseModel:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), 'model', 'deepcnn_edgeimpulse.onnx')
        self.session = ort.InferenceSession(model_path)
    
    def predict(self, X):
        # X is raw audio: shape (1, 16000)
        X = np.expand_dims(X, axis=1).astype(np.float32)  # → (1, 1, 16000)
        out = self.session.run(None, {"input": X})[0]
        return out
