import numpy as np
from sklearn.neighbors import KNeighborsClassifier

class AI_parsing():
    def __init__(self, date):
        self.temp_data = []
        self.rain_data = []
        self.claud_data = []
        self.date = date

    def loop_parsing(self):
        for i in range(int(len(self.date)-8)):
            l_temp = []
            l_rain = []
            l_claud = []
            for j in range(8):
                l_temp.append(int((self.date[i+j][2])))
                l_rain.append(int((self.date[i+j][1])))
                l_claud.append(int((self.date[i+j][3])))
            self.temp_data.insert(i,l_temp)
            self.rain_data.insert(i,l_rain)
            self.claud_data.insert(i,l_claud)

        temp_final = np.array(self.temp_data)
        rain_final = np.array(self.rain_data)
        claud_final = np.array(self.claud_data)

        temp_results = temp_final[:,-1]
        temp_desc = temp_final[:,0:-1]

        rain_results = rain_final[:,-1]
        rain_desc = rain_final[:,0:-1]

        claud_results = claud_final[:,-1]
        claud_desc = claud_final[:,0:-1]


        temp_KNN, rain_KNN, claud_KNN  = KNeighborsClassifier(n_neighbors=1,p=7) ,KNeighborsClassifier(n_neighbors=1,p=7),KNeighborsClassifier(n_neighbors=1,p=7)

        temp_KNN.fit(temp_desc, temp_results)
        rain_KNN.fit(rain_desc, rain_results)
        claud_KNN.fit(claud_desc, claud_results)
        return [temp_KNN, rain_KNN, claud_KNN]
