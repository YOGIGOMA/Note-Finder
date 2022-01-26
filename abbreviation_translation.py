# 영문 약어를 국문으로 변환합니다.

import pandas as pd
import re

ab_df = pd.read_csv("data/abbreviation_dictionary.csv", encoding="utf-8", low_memory=False)

def abbreviation_translation(input_str):
    for i in range(len(ab_df)):
        input_str = re.sub(ab_df.loc[i]["#en"].strip(), ab_df.loc[i]["#ko"].strip(), input_str)

    return input_str



