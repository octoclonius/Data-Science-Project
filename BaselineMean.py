import numpy as np

class BaselineMean:
    def __init__(self):
        self.is_fitted = False
        self.mean = None
    
    def fit(self, _, y):
        self.mean = np.mean(y)
        self.is_fitted = True
        return self

    def predict(self, X):
        if self.is_fitted:
            return np.full(len(X), self.mean)
        else:
            raise Exception(
                f"This {self.__name__} estimator instance is not fitted yet. "
                f"Call 'fit' with appropriate arguments before using this estimator."
            )