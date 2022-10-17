import matplotlib.pyplot as plt

x = ['barcode01.py', 'qrcode01.py', 'testando.py', 'testando01.py']
y = [0,42,39,49]

#plt.plot(x, y, "r--")
plt.barh(x, y, align='center', alpha=0.5)

plt.title("Bar chart", fontdict={'family': 'monospace', 'color' : 'red','weight': 'bold','size': 16},loc='center')


plt.xlabel('Funcionalidade')
plt.ylabel('Códigos Testados')

plt.show()