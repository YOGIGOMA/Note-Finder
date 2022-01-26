# 단어들을 정규화하여 처리합니다.

import re

normalization_pattern = {}

normalization_pattern["\d{4}(-|\.|\s){1,2}\d{1,2}(-|\.|\s){1,2}\d{1,2}(\s|\.)"] = "날짜" # 2022.1.25. 2022/01/25
normalization_pattern["\d{1,2}/\d{1,2}/\d{4}"] = "날짜" # 1/12/2022
normalization_pattern["\d{1,2}:\d{1,2}"] = "시간" # 01:14
normalization_pattern["\d{1,2}:\d{1,2}"] = "시간" # 01:14


def word_normalization(input_str):
    for p, r in normalization_pattern.items():
        input_str = re.sub(pattern=p, repl=r, string=input_str)

    return input_str

