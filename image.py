import matplotlib
import matplotlib.pyplot as plt
from openpyxl import load_workbook

matplotlib.use("Agg")
load_wb = load_workbook("C:/Users/dr2mer05/Desktop/sample_data.xlsx", data_only=True)
load_ws = load_wb['Sheet1']

for i in range(1, 10001):
    s = 102*(i-1)+8
    f = 102*i
    list1 = []
    get_cells = load_ws['C%d' % s:'C%d' % f]
    for row in get_cells:
        for cell in row:
            list1.append(cell.value)
    list2 = []
    get_cells = load_ws['D%d' % s:'D%d' % f]
    for row in get_cells:
        for cell in row:
            list2.append(cell.value)

    plt.subplot(2, 1, 1)
    plt.plot(list1)
    plt.title("ch1:x")
    plt.xlabel("x")
    plt.ylabel("ch1")

    plt.subplot(2, 1, 2)
    plt.plot(list2)
    plt.title("ch2:x")
    plt.xlabel("x")
    plt.ylabel("ch2")

    plt.tight_layout()
    plt.savefig('c:/Users/dr2mer05/Desktop/sample_data/sample_data%d.png' % i)
    plt.close()
