# 영문 약어를 국문으로 변환합니다.

import pandas as pd
import re

ab_df = pd.read_csv("data/abbreviation_dictionary.csv", encoding="utf-8", low_memory=False)


def abbreviation_translation(input_str):
    input_str = " " + input_str  # 문장이 약어로 먼저 시작되는 경우를 위해
    for i in range(len(ab_df)):
        temp_str = ab_df.loc[i]["#en"].strip().lower()
        input_str = re.sub(f"\s{temp_str}(?=[^A-Za-z])", " " + ab_df.loc[i]["#ko"].strip(), input_str)

    return input_str



