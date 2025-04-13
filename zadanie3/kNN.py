import numpy as np

#Ładowanie danych
with open("data_test.csv", "r") as file:
    content = file.read()
    
lines = content.split("\n")

dataTest = []
for l in lines:
    dataTest.append(l.split(","))
del dataTest[-1]
dataTest = [[float(element) for element in row] for row in dataTest]


with open("data_train.csv", "r") as file:
    content = file.read()
    
lines = content.split("\n")

dataTrain = []
for l in lines:
    dataTrain.append(l.split(","))
del dataTrain[-1]
dataTrain = [[float(element) for element in row] for row in dataTrain]

#data[wiersz][kolumna]
#Algorytm kNN
def max_val(tab, index): #max wartosc z tablicy dla danej cechy
    res = float(tab[0][index])
    for elem in tab:
        if(float(elem[index]) > res):
            res = float(elem[index])
        
    return res

def min_val(tab, index): #min wartosc z tablicy dla danej cechy
    res = float(tab[0][index])
    for elem in tab:
        if(float(elem[index]) < res):
            res = float(elem[index])
        
    return res

def generate_norm_data(tab): 
    normData = []
    for i in range(0,4):
        normData.append([min_val(tab,i), max_val(tab,i)]) 
    return normData #tablica z wartościami min i max dla każdej cechy

def normalize_vector(vector, normData, if2Dim=False, c1=0, c2=0): 
    
    if(if2Dim):
        return np.array([find_normalized_value(vector[0], normData[c1][0], normData[c1][1]), #zwraca wektor znormalizowany
                        find_normalized_value(vector[1], normData[c2][0], normData[c2][1])]) 
    else:
        return np.array([find_normalized_value(vector[0], normData[0][0], normData[0][1]),
                        find_normalized_value(vector[1], normData[1][0], normData[1][1]),
                        find_normalized_value(vector[2], normData[2][0], normData[2][1]),
                        find_normalized_value(vector[3], normData[3][0], normData[3][1])])
        
def find_normalized_value(value, min, max): #normalizacja wartości
    return (value-min)/(max - min) #zwraca wartość z przedziału <0,1>

def euclidean_distance_2dim(x, y, c1, c2, normData):
    vector1 = normalize_vector(np.array([x[c1], x[c2]]), normData, True, c1, c2) #normalizacja wektora z danymi testowymi
    vector2 = normalize_vector(np.array([y[c1], y[c2]]), normData, True, c1, c2) 
    return np.linalg.norm(vector1 - vector2) #obliczenie odległości euklidesowej

def euclidean_distance_4dim(x, y, normData):
    vector1 = normalize_vector(np.array([x[0], x[1], x[2], x[3]]), normData)
    vector2 = normalize_vector(np.array([y[0], y[1], y[2], y[3]]), normData) 
    
    return np.linalg.norm(vector1 - vector2)

def kNN_algorithm(data, k, if2Dim=False, c1=0, c2=0):
    normData = generate_norm_data(dataTrain) #tablica z wartościami min i max dla każdej cechy
    distance = []
    for row in dataTrain:
        if(if2Dim):
            distance.append([euclidean_distance_2dim(row, data, c1, c2, normData), row[4]]) #dodanie odległości i klasy do tablicy
        else:
            distance.append([euclidean_distance_4dim(row, data, normData), row[4]])
    distance.sort(key=lambda x: x[0]) #sortowanie tablicy po odległościach
    
    neighbors = distance[:k] #wybranie k najbliższych sąsiadów
    classes = [neighbor[1] for neighbor in neighbors] #wybranie klas sąsiadów
    return max(set(classes), key=classes.count) #zwrócenie klasy, która występuje najczęściej // key=classes.count - funkcja zwracająca ilość wystąpień elementu w tablicy wywołana dla każdego elementu tablicy

def make_error_matrix(k, if2Dim = False, c1 = 0, c2 = 0): #tworzenie macierzy błędu
    matrix = [[0,0,0],[0,0,0],[0,0,0]] #macierz błędu 3x3
    for data in dataTest:
        result = kNN_algorithm(data, k, if2Dim, c1, c2) 
        matrix[int(data[4])][int(result)] += 1 #zwiększenie wartości w macierzy błędu
    return matrix

#Użycie algorytmu
print("Dla wszystkich cech dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i) == data[4]): #sprawdzenie czy klasa obliczona przez algorytm jest równa klasie z danych testowych
            x += 1 
    percent = (x/len(dataTest))*100 #obliczenie procentowej zgodności
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 7
matrix = make_error_matrix(7) #tworzenie macierzy błędu dla najlepszego k (równego 7)
print(matrix[0]) 
print(matrix[1])
print(matrix[2]) 


print("Dla długości kielicha i szerokości kielicha dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i, True, 0, 1) == data[4]):
            x += 1
    percent = (x/len(dataTest))*100
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 5
matrix = make_error_matrix(5, True, 0, 1)
print(matrix[0])
print(matrix[1])
print(matrix[2])

print("Dla długości kielicha i długości płatka dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i, True, 0, 2) == data[4]):
            x += 1
    percent = (x/len(dataTest))*100
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 8
matrix = make_error_matrix(8, True, 0, 2)
print(matrix[0])
print(matrix[1])
print(matrix[2])

print("Dla długości kielicha i szerokości płatka dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i, True, 0, 3) == data[4]):
            x += 1
    percent = (x/len(dataTest))*100
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 5
matrix = make_error_matrix(5, True, 0, 3)
print(matrix[0])
print(matrix[1])
print(matrix[2])

print("Dla szerokości kielicha i długości płatka dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i, True, 1, 2) == data[4]):
            x += 1
    percent = (x/len(dataTest))*100
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 5
matrix = make_error_matrix(5, True, 1, 2)
print(matrix[0])
print(matrix[1])
print(matrix[2])

print("Dla szerokości kielicha i szerokości płatka dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i, True, 1, 3) == data[4]):
            x += 1
    percent = (x/len(dataTest))*100
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 3
matrix = make_error_matrix(3, True, 1, 3)
print(matrix[0])
print(matrix[1])
print(matrix[2])

print("Dla długości płatka i szerokości płatka dla k=<0,15>")
for i in range(1,16):
    x = 0
    for data in dataTest:
        if(kNN_algorithm(data,i, True, 2, 3) == data[4]):
            x += 1
    percent = (x/len(dataTest))*100
    print (f"k={i}, Zgodnosc: {percent}")

#najlepsze k dla tego testu: 1
matrix = make_error_matrix(1, True, 2, 3)
print(matrix[0])
print(matrix[1])
print(matrix[2])


   