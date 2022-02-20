# 단어들을 정규화하여 처리합니다.

import re

normalization_pattern = {}

normalization_pattern["\d{4}(-|\.|\s){1,2}\d{1,2}(-|\.|\s){1,2}\d{1,2}(\s|\.)"] = "날짜"  # 2022.1.25. 2022/01/25
normalization_pattern["\d{1,2}/\d{1,2}/\d{4}"] = "날짜"  # 1/12/2022
normalization_pattern["\d{1,2}:\d{1,2}"] = "시간"  # 01:14
normalization_pattern["[0-2]?[0-9][apAP][Mm]"] = "시간"  # 2am, 12pm
normalization_pattern["[apAP][Mm][0-2]?[0-9]"] = "시간"  # am2, pm11
normalization_pattern["(?<=[0-9])(HR|hr)"] = "시간"  # 24hr
normalization_pattern["/(hr|HR)"] = "시간당"  # /hr

normalization_pattern["prof?.?\s?[가-힣]+"] = "의사이름"  # prof.ooo, pro.ooo
normalization_pattern["pf.?\s?[가-힣]+"] = "의사이름"  # pf.ooo
normalization_pattern["[Dd]r.?\s?[가-힣]+"] = "의사이름"  # dr.ooo, Dr. ooo
normalization_pattern["[Rr][1-4].?\s?[가-힣]+"] = "의사이름"  # R1 ooo 또는 r1 OOO, R2 ooo 또는 r2 OOO, R3 ooo 또는 r3 OOO, R4OOO
normalization_pattern["주치의.?\s?[가-힣]+"] = "의사이름"  # 주치의 홍길동, 주치의 OO
normalization_pattern["당직의사?.?\s?[가-힣]+"] = "의사이름"  # 당직의 OOO, 당직의사 OOO, 당직의 OO
normalization_pattern["인턴.?\s?[가-힣]+"] = "의사이름"  # 인턴 OOO, 인턴 OO
normalization_pattern["의사?.?\s?[가-힣]+"] = "의사이름"  # 의사OOO, 의사OO, 의사 OOO, 의사 OO, 의사.OOO
normalization_pattern["d.?i.?\s?[가-힣]+"] = "의사이름"  # d.i.OOO, di.OOO
normalization_pattern["pf.?\s?\([가-힣]+\)"] = "의사이름"  # pf.(OOO)
normalization_pattern["D1.?\s?[가-힣]+"] = "의사이름"  # D1 OOO
normalization_pattern["[가-힣]+\s?교수님"] = "의사이름"  # OOO 교수님
normalization_pattern["전담간호사?.?\s?[가-힣]+"] = "간호사이름"  # 전담간호사 OOO, 전담간호사OOO


def word_normalization(input_str):
    for p, r in normalization_pattern.items():
        input_str = re.sub(pattern=p, repl=r, string=input_str)

    return input_str
