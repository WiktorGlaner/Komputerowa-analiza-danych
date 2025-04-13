import func

with open("data.csv", "r") as file:
    content = file.read()
    

lines = content.split("\n")

data = []
for l in lines:
    data.append(l.split(","))
del data[-1]

#ZADANIE 2

print("wyk. 1, r: ", func.wsp_kor_Pear(data, 0, 1),
      ", a: ",func.wsp_reglin_a(data, 0, 1),", b: ", func.wsp_reglin_b(data, 0, 1))

print("wyk. 2, r: ", func.wsp_kor_Pear(data, 0, 2),
      ", a: ",func.wsp_reglin_a(data, 0, 2),", b: ", func.wsp_reglin_b(data, 0, 2))

print("wyk. 3, r: ", func.wsp_kor_Pear(data, 0, 3),
      ", a: ",func.wsp_reglin_a(data, 0, 3),", b: ", func.wsp_reglin_b(data, 0, 3))

print("wyk. 4, r: ", func.wsp_kor_Pear(data, 1, 2),
      ", a: ",func.wsp_reglin_a(data, 1, 2),", b: ", func.wsp_reglin_b(data, 1, 2))

print("wyk. 5, r: ", func.wsp_kor_Pear(data, 1, 3),
      ", a: ",func.wsp_reglin_a(data, 1, 3),", b: ", func.wsp_reglin_b(data, 1, 3))

print("wyk. 6, r: ", func.wsp_kor_Pear(data, 2, 3),
      ", a: ",func.wsp_reglin_a(data, 2, 3),", b: ", func.wsp_reglin_b(data, 2, 3))

labels = ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]

func.make_scatter(data, 0, 1, labels[0], labels[1], 4, 8, 0.5, 2, 4.5, 0.5)
func.make_scatter(data, 0, 2, labels[0], labels[2], 4, 8, 0.5, 1, 8, 1)
func.make_scatter(data, 0, 3, labels[0], labels[3], 4, 8, 0.5, 0, 3, 0.5)
func.make_scatter(data, 1, 2, labels[1], labels[2], 2, 4.5, 0.5, 1, 7, 1)
func.make_scatter(data, 1, 3, labels[1], labels[3], 2, 4.5, 0.5, 0, 2.5, 0.5)
func.make_scatter(data, 2, 3, labels[2], labels[3], 1, 7, 1, 0, 2.5, 0.5)