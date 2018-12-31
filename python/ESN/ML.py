import numpy as np

class ESN:
    @staticmethod
    def ESN(data,W,W_reservoir,a):
       return np.multiply(a,data) + \
    np.multiply((1-a),np.tanh(np.add(np.dot(W,data),np.dot(W_reservoir,data))))


    def __init__(self, W, W_reservoir,a):
        self.W = W
        self.W_reservoir = W_reservoir
        self.a = a

    def esn(self,x):
        self.x = x

        return np.multiply(self.a, self.x) + \
               np.multiply((1 - self.a), np.tanh(np.add(np.dot(self.W, self.x), np.dot(self.W_reservoir, self.x))))