import numpy as np

class Neural_Network(object):
    def __init__(self):
        #Define HyperParameters
        self.hiddenLayerSize = 3
        self.inputLayerSize =2
        self.outputLayerSize=1

        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)

    def forward(self,X):
        #Propogate inputs throug network
        self.z2 = np.dot(X,self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2,self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat #Estimate
        

    def sigmoid(self,z):
        #Apply sigmoid activation function
        return 1/(1+np.exp(-z))
        

nn = Neural_Network()

X = [[3,5],[5,1],[10,2]]
Xnorm = X/np.amax(X,axis=0)
yhat = nn.forward(Xnorm)

print(yhat)