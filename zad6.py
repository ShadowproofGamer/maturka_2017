plik = open("dane.txt")
dane = plik.read().split()
dane2 = []
dane2rev = []
for i in range(200):
    temp = []
    for j in range(0+i*320, 320+i*320, 1):
        temp.append(int(dane[j]))
    dane2.append(temp)
for i in range(200):
    temp = []
    for j in range(0+i, 200*320, 320):
        temp.append(int(dane[j]))
    dane2rev.append(temp)
max_jasnosc = 0
max_ciemnosc = 255
for i in dane:
    if int(i)>max_jasnosc:
        max_jasnosc=int(i)
    if int(i)<max_ciemnosc:
        max_ciemnosc=int(i)
print("maksymalna jasnosc: ", max_jasnosc, " maksymalna ciemnosc: ", max_ciemnosc)
liczba_wierszy =0
for i in dane2:
    for j in range(320):
        if i[j] != i[319-j]:
            liczba_wierszy += 1
            break
print("liczba wierszy: ", liczba_wierszy)
dane_int = []
for i in range(len(dane)):
    dane_int.append(int(dane[i]))

liczba_kontr = 0
tab = []
for i in range(1, 318):
    if abs(dane_int[i] - dane_int[i-1]) > 128 or abs(dane_int[i] - dane_int[i+1]) > 128 or abs(dane_int[i] - dane_int[i+320]) > 128:
        liczba_kontr+=1
for i in range(len(dane_int)-319, len(dane_int)-2):
    if abs(dane_int[i] - dane_int[i-1]) > 128 or abs(dane_int[i] - dane_int[i+1]) > 128 or abs(dane_int[i] - dane_int[i-320]) > 128:
        liczba_kontr+=1
for i in range(320, len(dane_int)-640, 320):
    if abs(dane_int[i] - dane_int[i-320]) > 128 or abs(dane_int[i] - dane_int[i+1]) > 128 or abs(dane_int[i] - dane_int[i+320]) > 128:
        liczba_kontr+=1
for i in range(639, len(dane_int)-321, 320):
    if abs(dane_int[i] - dane_int[i-1]) > 128 or abs(dane_int[i] - dane_int[i-320]) > 128 or abs(dane_int[i] - dane_int[i+320]) > 128:
        liczba_kontr+=1

if abs(dane_int[0] - dane_int[1])>128 or abs(dane_int[0] - dane_int[320])>128:
    liczba_kontr+=1
if abs(dane_int[319] - dane_int[318])>128 or abs(dane_int[319] - dane_int[639])>128:
    liczba_kontr+=1
if abs(dane_int[len(dane_int)-320] - dane_int[len(dane_int)-319])>128 or abs(dane_int[len(dane_int)-320] - dane_int[len(dane_int)-640])>128:
    liczba_kontr+=1
if abs(dane_int[len(dane_int)-1] - dane_int[len(dane_int)-2])>128 or abs(dane_int[len(dane_int)-1] - dane_int[len(dane_int)-321])>128:
    liczba_kontr+=1
for i in range(1,199):
    for j in range(1,319):
        if abs(dane_int[i*320 +j] - dane_int[i*320 +j-1])>128:
            liczba_kontr+=1
        elif abs(dane_int[i*320 +j] - dane_int[i*320 +j+1])>128:
            liczba_kontr+=1
        elif abs(dane_int[i*320 +j] - dane_int[i*320 +j-320])>128:
            liczba_kontr+=1
        elif abs(dane_int[i*320 +j] - dane_int[i*320 +j+320])>128:
            liczba_kontr+=1

'''
for i in range(len(dane2)):
    for j in range(len(dane2[i])):

        if j == 0 and abs(dane2[i][j+1]-dane2[i][j]) > 128:
            liczba_kontr += 1
            tab.append(j + i * 320)
        if j == 319 and abs(dane2[i][j-1]-dane2[i][j]) > 128:
            liczba_kontr += 1
            tab.append(j + i * 320)
        if (j!=0) and (j!=319) and (abs(dane2[i][j+1]-dane2[i][j]) > 128 or abs(dane2[i][j-1]-dane2[i][j]) > 128):
            liczba_kontr += 1
            tab.append(j + i * 320)
for i in range(len(dane2rev)):
    for j in range(len(dane2rev[i])):

        if (j == 0) and (abs(dane2rev[i][j+1]-dane2rev[i][j]) > 128):
            if tab.count(i + j * 320) == 0:
                #print("i: ", i, "j: ", j, "wartosc: ", abs(dane2rev[i][j + 1] - dane2rev[i][j]))
                tab.append(i + j * 320)
                liczba_kontr += 1
        if (j == 199) and (abs(dane2rev[i][j-1]-dane2rev[i][j]) > 128):
            if tab.count(i + j * 320) == 0:
                #print("i: ", i, "j: ", j, "wartosc: ", abs(dane2rev[i][j + 1] - dane2rev[i][j]))
                tab.append(i + j * 320)
                liczba_kontr += 1
        if (j!=0) and (j!=199) and abs(dane2rev[i][j+1]-dane2rev[i][j]) > 128:
            if tab.count(i + j * 320) == 0:
                #print("i: ", i, "j: ", j, "wartosc: ", abs(dane2rev[i][j + 1] - dane2rev[i][j]))
                tab.append(i + j * 320)
                liczba_kontr += 1
        if (j!=0) and (j!=199) and abs(dane2rev[i][j - 1] - dane2rev[i][j]) > 128:
            if tab.count(i + j * 320) == 0:
                #print("i: ", i, "j: ", j, "wartosc: ", abs(dane2rev[i][j -1] - dane2rev[i][j]))
                tab.append(i + j * 320)
                liczba_kontr += 1

'''

print("kontrast: ", liczba_kontr)
#print(tab)
'''
for i in tab:
    print(i, " : ", dane[i])
'''

#print(len(tab))
long = 0

for i in dane2rev:
    temp = 1
    num = i[0]
    for j in range(1, len(i)):
        if i[j] == num:
            temp+=1
        else:
            if temp>long:
                long=temp
            num=i[j]
            temp=1
print("dlugosc linii: ", long)
