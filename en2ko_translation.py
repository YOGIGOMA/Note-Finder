# en2ko_dictionary를 기반으로 영문을 국문으로 변환합니다.

import pandas as pd
import re

dic_df = pd.read_csv("data/en2ko_dictionary.csv", encoding="utf-8", low_memory=False)

def en2ko_translation(input_str):
    for i in range(len(dic_df)):
        input_str = re.sub(dic_df.loc[i]["#en"].strip(), dic_df.loc[i]["#ko"].strip(), input_str)

    return input_str

def print_dic_length():
    print("입력 번역사전에서 읽어들인 용어의 개수", len(dic_df) - 1)



