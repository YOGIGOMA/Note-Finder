# !pip install openpyxl

import pandas as pd
import os

INPUT_FILE_NAME = "data/Train_원본엑셀.xlsx"
TEMP_FILE_NAME = "data/temp.txt"
OUPUT_FILE_NAME = "data/input.txt"

df = pd.read_excel(INPUT_FILE_NAME,
                   sheet_name=0)

with open(TEMP_FILE_NAME, 'w') as outfile:
    df.to_string(outfile, index=False)

# 임시로 TEMP_FILE을 만든 후, 삭제
f_temp = open(TEMP_FILE_NAME, 'r')
lines = f_temp.readlines()
f_temp.close()
os.remove(TEMP_FILE_NAME)

f = open(OUPUT_FILE_NAME, 'w')
for line in lines:
    line = line.strip(" ")
    line = line.replace("_x000D_\\n", " ")
    line = line.replace("_x000D_", " ")
    line = line + "\n\n"
    f.write(line)
f.close()
