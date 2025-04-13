import numpy as np
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt

#Ładowanie danych
with open("data.csv", "r") as file:
    content = file.read()
    
lines = content.split("\n") 

data = []
for l in lines:
    data.append(l.split(","))
del data[-1] #usunięcie pustego wiersza na końcu
data = [[float(element) for element in row] for row in data] 
data = np.array(data)

X = data[:,:4] #tylko cechy bez gatunku

#Zbieranie danych
wcssValues = [] #suma kwadratów odległości punktów od centroidów
iterValues = [] #liczba iteracji
kValues = range(2,11) #liczba klastrów

for k in kValues:
    kmeans = KMeans(n_clusters=k) 
    kmeans.fit(X) 
    iterations = kmeans.n_iter_ #liczba iteracji
    clusters = kmeans.labels_ #przypisanie do klastrów
    wcss = kmeans.inertia_ #suma kwadratów odległości punktów od centroidów
    centroids = kmeans.cluster_centers_ #współrzędne centroidów
    wcssValues.append(wcss)
    iterValues.append(iterations)
    print(f"k={k}, liczba iteracji={iterations}, WCSS={wcss}")
    
    #wykresy dla wszystkich par cech dla warości k=3
    if(k == 3):
        featureLabels = ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]
        
        featurePairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)] #wszystkie pary cech

        fig, axs = plt.subplots(2, 3, figsize=(15, 10)) #6 wykresów 2x3, figsize to rozmiar figury w calach
        
        for i, (x, y) in enumerate(featurePairs):
            axs[i//3, i%3].scatter(X[:, x], X[:, y], c=clusters) #i//3 to numer wiersza, i%3 to numer kolumny
            axs[i//3, i%3].scatter(centroids[:, x], centroids[:, y], c=np.unique(clusters) , marker="X", s=100, edgecolor="red") #oznaczenie centroidow na wykresach po wspolrzednych x oraz y
            axs[i//3, i%3].set_xlabel(featureLabels[x] + " (cm)")
            axs[i//3, i%3].set_ylabel(featureLabels[y] + " (cm)")
        plt.show()

# Wykres liczby iteracji od k
plt.plot(kValues, iterValues)
plt.scatter(kValues, iterValues)
plt.xlabel('Wartość liczby k')
plt.ylabel('Liczba iteracji')
plt.title('Zależność liczby iteracji od liczby k')
plt.show()

# Wykres wartości WCSS od k
plt.plot(kValues, wcssValues)
plt.scatter(kValues, wcssValues)
plt.xlabel('Wartość liczby k')
plt.ylabel('Wartość WCSS')
plt.title('Zależność Wartości WCSS od liczby k')
plt.show()