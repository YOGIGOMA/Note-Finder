# 단어들을 정규화하여 처리합니다.

import re

normalization_pattern = {}

normalization_pattern["\d{4}(-|\.|\s){1,2}\d{1,2}(-|\.|\s){1,2}\d{1,2}(\s|\.)"] = "날짜"  # 2022.1.25. 2022/01/25
normalization_pattern["\d{1,2}/\d{1,2}/\d{4}"] = "날짜"  # 1/12/2022
normalization_pattern["\d{1,2}:\d{1,2}"] = "시간"  # 01:14
normalization_pattern["[0-2]?[0-9][apAP][Mm]"] = "시간"  # 2am, 12pm
normalization_pattern["[apAP][Mm][0-2]?[0-9]"] = "시간"  # am2, pm11

normalization_pattern["p(ro)?f?.\s?[가-힣]{3}"] = "의사이름"  # prof.홍길동, pf. 홍길동, pro. 홍길동
normalization_pattern["[Dd]r.\s?[가-힣]{3}"] = "의사이름"  # dr.홍길동, Dr. 홍길동
normalization_pattern["[Rr][1-3].?\s?[가-힣]{3}"] = "의사이름"  # R1 홍길동 또는 r1 홍길동, R2 홍길동, r3 홍길동
normalization_pattern["당직의사?\s?[가-힣]{3}"] = "의사이름"  # 당직의 홍길동, 당직의사 홍길동
normalization_pattern["주치의\s?[가-힣]{3}"] = "의사이름"  # 주치의 홍길동

normalization_pattern["[0-9]+(hr|HR)"] = "시간"  # 24hr
normalization_pattern["/(hr|HR)"] = "시간당"  # /hr


def word_normalization(input_str):
    for p, r in normalization_pattern.items():
        input_str = re.sub(pattern=p, repl=r, string=input_str)

    return input_str
