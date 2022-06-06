import matplotlib
import matplotlib.pyplot as plt
from openpyxl import load_workbook

read_dir_path = ''
read_file_name =''
read_file_type = 'xlsx'

save_dir_path=''
save_file_name=''
save_file_type='png'

read_file_path = '{}/{}.{}'.format(dir_path, file_name, file_type)

matplotlib.use("Agg")
load_wb = load_workbook(read_file_path, data_only=True)
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
    save_file_path = '{}/{}%d.{}'.format(save_dir_path, save_file_name, i, save_file_type)
    plt.savefig(save_file_path)
    plt.close()
