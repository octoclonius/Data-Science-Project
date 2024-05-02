import numpy as np

class BaselineRandom:
    def __init__(self, *, random_state=None):
        self.is_fitted = False
        self.low = None
        self.high = None
        self.rng = np.random.default_rng(random_state)
    
    def fit(self, _, y):
        self.low = min(y)
        self.high = max(y)
        self.is_fitted = True
        return self

    def predict(self, X):
        if self.is_fitted:
            return np.array(self.rng.uniform(self.low, self.high, len(X))).ravel()
        else:
            raise Exception(
                f"This {self.__name__} estimator instance is not fitted yet. "
                f"Call 'fit' with appropriate arguments before using this estimator."
            )