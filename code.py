import matplotlib.pyplot as plt

t, Va, Vb, Vc, Ia, Ib, Ic = [], [], [], [], [], [], []
for line in open(r'C:\Codes\Project\Trapezoidal rule\309.ADF', 'r'):
    values = [float(s) for s in line.split()]
    t.append(values[0])
    Va.append(values[1])
    Vb.append(values[2])
    Vc.append(values[3])
    Ia.append(values[4])
    Ib.append(values[5])
    Ic.append(values[6])

Va_R = []
R = 0
rv = int(len(Va) - 2000)

a = 0
b = 2000
for i in range(rv):
    R = sum(Va[a:b])
    Va_R.append(R)
    a += 1
    b += 1

Ia_R = []
a = 0
b = 2000
for i in range(rv):
    first = sum(Ia[a:b])
    Ia_R.append(first)
    a += 1
    b += 1


plt.xlabel("Time (t)")
plt.ylabel("Voltage (Va)")
plt.plot(t, Va)
plt.title('Voltage Vs Time')
plt.show()

plt.ylabel("Resultant")
plt.plot(Va_R)
plt.title("Resultant of Va")  # First Plot
plt.show()

plt.xlabel("Time (t)")
plt.ylabel("Current (Ia)")
plt.plot(t, Ia)
plt.title("Time VS Current Graph")
plt.show()

plt.ylabel("Resultant")
plt.title("Resultant of Ia")
plt.plot(Ia_R)  # Second Plot
plt.show()
