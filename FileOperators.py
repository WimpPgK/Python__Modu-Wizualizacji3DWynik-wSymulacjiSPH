class FileOperators():

    def loadFromFile(self, fileName, X,Y,Z,T):
        # print("Wpisz nazwe pliku:")
        # sciezka = input()
        #sciezka = "results_particles_temperature00002.vel"
        plik = open("./data/" + fileName, "r")
        dane = plik.read()
        dane = dane.strip()  # usuwa entery
        dane = dane.split()  # usuwa spacje

        i = 0
        while i < (len(dane) - 4):
            X.append(float(dane[i + 1]))
            Y.append(float(dane[i + 2]))
            Z.append(float(dane[i + 3]))
            T.append(float(dane[i + 4]))
            i += 5
        plik.close()
