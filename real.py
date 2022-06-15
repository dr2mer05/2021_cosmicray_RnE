import matplotlib
from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt
import logging

matplotlib.use("Agg")

NUM = 100000
RANGE = 250

dir_path = "C:/2021RnE/real_data/"
load_dir_path = dir_path + "raw_data/"
save_fdt_dir_path = dir_path + "fdt_data/"
save_hist_dir_path = dir_path + "hist_data/"
load_file_name = "raw_data_200809"
load_file_path = load_dir_path + load_file_name + ".xlsx"

load_wb = load_workbook(load_file_path, data_only=True)
load_ws = load_wb['Sheet1']

logger = logging.getLogger("fdt_data")
logger.setLevel(logging.DEBUG)
save_fdt_file_path = save_fdt_dir_path + "fdt_data_200809.log"
fh = logging.FileHandler(save_fdt_file_path)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

s = 1
e = NUM
listCh2 = []
get_cells = load_ws['C%d' % s:'C%d' % e]
for row in get_cells:
    for cell in row:
        listCh2.append(1024-cell.value)

listCh3 = []
get_cells = load_ws['D%d' % s:'D%d' % e]
for row in get_cells:
    for cell in row:
        listCh3.append(1024-cell.value)
listRe = []
for i in range(NUM):
    if listCh3[i] == 0:
        continue
    listRe.append(listCh2[i] / listCh3[i] * 100)

bins = np.arange(0, RANGE, 1)
hist, bins = np.histogram(listRe, bins)
hist_log = [0 for i in range(RANGE)]
for i in range(0, RANGE-1):
    hist_log[i] += hist[i]
logger.debug(hist_log)   

plt.hist(listRe, bins=range(0, RANGE, 1), density=True, alpha=1, histtype='stepfilled')
plt.axis('off')
save_hist_file_path = save_hist_dir_path + "hist_data_200809.png"
plt.savefig(save_hist_file_path)
plt.close()
