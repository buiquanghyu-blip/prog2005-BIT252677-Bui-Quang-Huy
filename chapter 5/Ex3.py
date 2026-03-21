import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes = [30, 25, 15, 20, 10]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Tỷ lệ doanh số các sản phẩm")

plt.show()
