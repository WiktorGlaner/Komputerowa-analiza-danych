import func

with open("data.csv", "r") as file:
    content = file.read()
    

lines = content.split("\n")

data = []
for l in lines:
    data.append(l.split(","))
del data[-1]

#1.1.1
print("\n Liczebności gatunków")
licz1=0
licz2=0
licz3=0

for ele in data:
    if ele[4]=="0":
        licz1+=1
    elif ele[4]=="1":
        licz2+=1
    elif ele[4]=="2":
        licz3+=1

print('setosa',licz1)
print('versicolor',licz2)
print('virginica',licz3)

#1.1.2
print("\n Udziały procentowe")
totalPop = licz1 + licz2 + licz3
up1 = licz1/totalPop * 100
up2 = licz2/totalPop * 100
up3 = licz3/totalPop * 100

print('setosa',up1,'%')
print('versicolor',up2,'%')
print('virginica',up3,'%')

#1.2.1.1
print("\n wartości ekstremalne: minimum, maksimum")
print("1. długość działki kielicha:\nmin:", func.min(data,0),"\nmax:",func.max(data,0))
print("2. szerokość działki kielicha:\nmin:", func.min(data,1),"\nmax:",func.max(data,1))
print("3. długość płatka:\nmin:", func.min(data,2),"\nmax:",func.max(data,2))
print("4. szerokość płatka:\nmin:", func.min(data,3),"\nmax:",func.max(data,3))

#1.2.1.2
print("\n miary tendencji centralnej: średnia arytmetyczna, mediana")
print("1. długość działki kielicha:\navg:", func.avg(func.sum(data,0),len(data)),"\nmed:",func.quartile(func.sortTab(data,0),2))
print("2. szerokość działki kielicha:\navg:", func.avg(func.sum(data,1),len(data)),"\nmed:",func.quartile(func.sortTab(data,1),2))
print("3. długość płatka:\navg:", func.avg(func.sum(data,2),len(data)),"\nmed:",func.quartile(func.sortTab(data,2),2))
print("4. szerokość płatka:\navg:", func.avg(func.sum(data,3),len(data)),"\nmed:",func.quartile(func.sortTab(data,3),2))

#1.2.1.3
print("\n miary położenia wyższych rzędów: dolny kwartyl (Q1), górny kwartyl (Q3)")
print("1. długość działki kielicha:\nQ1:", func.quartile(func.sortTab(data,0),1),"\nQ3:",func.quartile(func.sortTab(data,0),3))
print("2. szerokość działki kielicha:\nQ1:", func.quartile(func.sortTab(data,1),1),"\nQ3:",func.quartile(func.sortTab(data,1),3))
print("3. długość płatka:\nQ1:", func.quartile(func.sortTab(data,2),1),"\nQ3:",func.quartile(func.sortTab(data,2),3))
print("4. szerokość płatka:\nQ1:", func.quartile(func.sortTab(data,3),1),"\nQ3:",func.quartile(func.sortTab(data,3),3))

#1.2.2
print("\n miara zróżnicowania rozkładu: odchylenie standardowe (obliczone ze wzoru dla próby)")
print("1. długość działki kielicha:", func.stdProba(data,0))
print("2. szerokość działki kielicha:", func.stdProba(data,1))
print("3. długość płatka:", func.stdProba(data,2))
print("4. szerokość płatka:", func.stdProba(data,3))


#2.1
func.makeHistogramSimple(data,0,"Długość działki kielicha",35,4,8.5,0.5)
func.makeHistogramSimple(data,1,"Szerokość działki kielicha",55,2,4.6,0.25)
func.makeHistogramSimple(data,2,"Długość płatka",35,1,7.1,0.5)
func.makeHistogramSimple(data,3,"Szerokość płatka",40,0,2.6,0.25)

#2.2
func.makeBoxplot(data,0,"Długość działki kielicha",4,8)
func.makeBoxplot(data,1,"Szerokość działki kielicha",1,5)
func.makeBoxplot(data,2,"Długość płatka",0,7)
func.makeBoxplot(data,3,"Szerokość płatka",0,3)

#Uwaga
func.makeHistogramComplex(data,0,"Długość działki kielicha",30,4,8.5,0.5)
func.makeHistogramComplex(data,1,"Szerokość działki kielicha",25,2,4.6,0.25)
func.makeHistogramComplex(data,2,"Długość płatka",30,1,7.1,0.5)
func.makeHistogramComplex(data,3,"Szerokość płatka",35,0,2.6,0.25)