import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm
from mpl_toolkits.mplot3d import Axes3D



class Visualization():

    def __init__(self, x,y,z,t):
        self.X = x
        self.Y = y
        self.Z = z
        self.T = t

    def createObjectChart3D(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        img = ax.scatter(self.X, self.Y, self.Z)  # cmap=plt.hot()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def createSPHChart3D(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        img = ax.scatter(self.X, self.Y, self.Z, c=self.T, cmap=plt.hot())
        fig.colorbar(img)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axis('off')
        plt.show()

    def createIntersectionX(self, a):
        pomX = []
        pomY = []
        pomZ = []
        pomT = []

        minX = min(self.X)
        maxX = max(self.X)

        intesectionTab_x = np.linspace(minX, maxX, 11)

        for i in range(len(self.X)):
            if (self.X[i] > intesectionTab_x[a] and self.X[i] < intesectionTab_x[a+1]):
                pomX.append(self.X[i])
                pomY.append(self.Y[i])
                pomZ.append(self.Z[i])
                pomT.append(self.T[i])

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        img = ax.scatter(0, pomY, pomZ, c=pomT, cmap=plt.hot())
        fig.colorbar(img)
        plt.xlabel("x")
        plt.ylabel("y")
        #plt.axis('off')
        plt.show()



    def createIntersectionY(self, a):
        pomX = []
        pomY = []
        pomZ = []
        pomT = []

        minY = min(self.Y)
        maxY = max(self.Y)

        intesectionTab_y = np.linspace(minY, maxY, 11)

        for i in range(len(self.X)):
            if (self.Y[i] > intesectionTab_y[a] and self.Y[i] < intesectionTab_y[a+1]):
                pomX.append(self.X[i])
                pomY.append(self.Y[i])
                pomZ.append(self.Z[i])
                pomT.append(self.T[i])

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        img = ax.scatter(pomX, 0, pomZ, c=pomT, cmap=plt.hot())
        fig.colorbar(img)
        plt.xlabel("x")
        plt.ylabel("y")


        #ax.set_xlim([min(self.X), max(self.X)])
        #ax.set_ylim([min(self.Y) - 20*abs(max(self.Y) - min(self.Y)) , max(self.Y)])
        #print (max(self.Y))
        #print(min(self.Y))
        #ax.set_ylim([ymin, ymax])
        #plt.axis('off')
        plt.show()



    def createIntersectionZ(self, a):
        pomX = []
        pomY = []
        pomZ = []
        pomT = []

        minZ = min(self.Z)
        maxZ = max(self.Z)

        intesectionTab_z = np.linspace(minZ, maxZ, 11)

        for i in range(len(self.X)):
            if (self.Z[i] > intesectionTab_z[a] and self.Z[i] < intesectionTab_z[a + 1]):
                pomX.append(self.X[i])
                pomY.append(self.Y[i])
                pomZ.append(self.Z[i])
                pomT.append(self.T[i])

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        img = ax.scatter(pomX, pomY, 0, c=pomT, cmap=plt.hot())
        fig.colorbar(img)
        plt.xlabel("x")
        plt.ylabel("y")
        # plt.axis('off')
        plt.show()


    def showSubplots(self):
        plt.show()


'''
    rysowanie wykresu  temperatury 3D
'''
"""
fig = plt.figure()
ax = fig.gca(projection='3d')
img = ax.scatter(X, Y, Z, c=T, cmap=plt.hot())
fig.colorbar(img)
plt.xlabel("x")
plt.ylabel("y")
plt.axis('off')
plt.show()
"""


'''
    rysowanie wykresu ksztaltu elementu
'''
"""
fig = plt.figure()
ax = fig.gca(projection='3d')
img = ax.scatter(X, Y, Z) #cmap=plt.hot()
fig.colorbar(img)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

"""

'''
minX = min(X)
maxX = max(X)
intesectionTab_x = np.linspace(minX, maxX, 10)

pomX = []
pomY = []
pomZ = []
pomT = []
for i in range(len(X)):
    if(X[i] > intesectionTab_x[2] and X[i] < intesectionTab_x[3]):
        pomX.append(X[i])
        pomY.append(Y[i])
        pomZ.append(Z[i])
        pomT.append(T[i])


fig = plt.figure()
ax = fig.gca(projection='3d')
img = ax.scatter(pomX, pomY, pomZ) #cmap=plt.hot()
fig.colorbar(img)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
img = ax.scatter(0, pomY, pomZ, c=pomT, cmap=plt.hot())
fig.colorbar(img)
plt.xlabel("x")
plt.ylabel("y")
plt.axis('off')
plt.show()



fig = plt.figure()
ax = plt.axes(projection='3d')
img = ax.plot_surface(pomY, pomZ, pomT, cmap='viridis', edgecolor='none')
fig.colorbar(img)
plt.xlabel("x")
plt.ylabel("y")
plt.axis('off')
plt.show()

'''