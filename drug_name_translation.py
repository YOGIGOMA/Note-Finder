# 영문 약물이름을 국문 성분명으로 변환합니다.

import pandas as pd
import re

drug_df = pd.read_csv("data/drug_name_dictionary.csv", encoding="utf-8", low_memory=False)


def drug_name_translation(input_str):
    for i in range(len(drug_df)):
        input_str = re.sub(drug_df.loc[i]["#en"].strip().lower(), drug_df.loc[i]["#ko"].strip(), input_str)

    return input_str