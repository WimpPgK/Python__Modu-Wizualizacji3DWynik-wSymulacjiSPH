from Visualization import Visualization
from FileOperators import FileOperators

class ProgramMenagement():

    def __init__(self):
        self.X = []
        self.Y = []
        self.Z = []
        self.T = []


    def startProgram(self):

        fileName = "results_particles_temperature00002.vel"
        f1 = FileOperators()
        f1.loadFromFile(fileName, self.X, self.Y, self.Z, self.T)
        self.createVisualization()


    def createVisualization(self):
        v1 = Visualization(self.X, self.Y, self.Z, self.T)
        #v1.createObjectChart3D()
        #v1.createSPHChart3D()

        #positionX, positionY, positionZ to miejsce w ktorym przekroj ma powstac <0;10>
        #positionX = 9
        #v1.createIntersectionX(positionX)

        positionY = 9
        v1.createIntersectionY(positionY)

        #positionZ = 9
        #v1.createIntersectionZ(positionZ)



