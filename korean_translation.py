# -*- coding: utf-8 -*-
import re
import string  # string.punctuation 사용하기 위해 import
import pandas as pd


def translation(input_str):
    for i in range(len(dic_df)):
        input_str = re.sub(dic_df.loc[i]["#en"].strip(),
                           dic_df.loc[i]["#ko"].strip(), input_str)

    return input_str


# 사전에 정의한 제거문자열 패턴을 탐색하여 제거하는 함수
def replace_string_pattern(input_str, pattern_dict):
    for p, r in pattern_dict.items():
        input_str = re.sub(pattern=p, repl=r, string=input_str)

    return input_str


input = open("data/input.txt", mode="r", encoding="utf-8")
output = open("data/input_ko.txt", mode="w", encoding="utf-8")

input_list = input.readlines()  # 입력 텍스트파일의 데이터를 리스트 형태로 변환함
output_list = ["#ProcessedData\n"]

dic_df = pd.read_csv("data/en2ko_dictionary.csv",
                     encoding="utf-8", low_memory=False)

pattern_dict = {}

pattern_dict["(NIBP_평균+[^0-9]+[0-9. ]+)"] = "평균혈압 "  # NIBP_평균(mmHg) : 숫자
pattern_dict["(NIBP_이완기+[^0-9]+[0-9. ]+)"] = "이완기혈압 "  # NIBP_수축기(mmHg) : 숫자
pattern_dict["(NIBP_수축기+[^0-9]+[0-9. ]+)"] = "수축기혈압 "  # NIBP_이완기(mmHg) : 숫자
pattern_dict["(PR+[^0-9]+[0-9. ]+)"] = "맥박  "  # PR문자열 : 숫자
pattern_dict["(RR+[^0-9]+[0-9. ]+)"] = "호흡수 "  # RR문자열 : 숫자
pattern_dict["(BT+[^0-9]+[0-9. ]+)"] = "체온 "  # BT문자열 : 숫자
pattern_dict["(SpO+[^0-9]+[0-9. ]+)"] = "말초산소포화도 "  # SpO문자열 : 숫자
pattern_dict["(Device+[^0-9]+[a-zA-Z]+)"] = "기기 "  # Device : 영문자

pattern_dict["(FiO+[^0-9]+[0-9. ]+)"] = "흡입산소농도 "  # FiO₂(%) : 숫자
pattern_dict["(O₂ Flow(L/min)+[: ]+[0-9. ]+)"] = "산소유량 "  # O₂ Flow(L/min) : 숫자
pattern_dict["(pH+[▲▼: ]+[0-9. ]+pH+)"] = "수소이온농도 "  # pH : 숫자 pH
pattern_dict["(pCO2+[▲▼: ]+[0-9. ]+mmHg+)"] = "이산화탄소농도 "  # pCO2 : 숫자 mmHg
pattern_dict["(pO2+[▲▼: ]+[0-9. ]+mmHg+)"] = "산소농도 "  # pO2 : 숫자 mmHg
# EVM : E숫자V숫자M숫자
pattern_dict["(EVM+[: ]+E+[0-9]+V+[0-9]+M+[0-9]+)"] = "눈뜨기,언어,근력 "
pattern_dict[
    "(PS LR(R/L)+[: ]+[a-zA-Z0-9]+/+[a-zA-Z0-9]+)"
] = "동공크기 "  # PS LR(R/L) : 문자/문자
pattern_dict["(의식상태+[: ]+[^0-9]+)"] = "동공빛반사 "  # 의식상태 : 단어
# Pupil shape : 단어/단어
pattern_dict["(Pupil shape+[: ]+[^0-9]+/+[^0-9]+)"] = " "
# Hemoglobin, Blood 숫자
pattern_dict["(Hemoglobin, Blood+[▲▼: ]+[0-9. ]+)"] = "헤모글로빈 "
pattern_dict["(Albumin+[^0-9]+[0-9. ]+)"] = "알부민 "  # Albumin (g/㎗    ): 숫자
pattern_dict["(Location 1+[: ]+[^0-9]+)"] = "측정위치 "  # Location 1 : 단어
pattern_dict["(Comment+[: ]+[^0-9]+)"] = "코멘트 "  # Comment : 단어
pattern_dict[
    "(Potassium (K)+[▲▼: ]+[0-9. ]+mmol/ℓ+)"
] = "포타슘 "  # Potassium (K) : 숫자 mmol/ℓ
pattern_dict[
    "(ANC (Absolute Neutrophil Count)+)"
] = "절대호중구수 "  # ANC (Absolute Neutrophil Count)
pattern_dict["(APTT+[▲▼: ]+[0-9. ]+sec+)"] = "활성화부분트롬보플라스틴시간 "  # APTT : 실수 sec
pattern_dict["(Mg+[▲▼: ]+[0-9. ]+㎎/㎗+)"] = "마그네슘 "  # Mg : 숫자 ㎎/㎗
pattern_dict[
    "(Osmolality, Serum+[^0-9]+[0-9. ]+)"
] = "혈청삼투압농도 "  # Osmolality, Serum (mOsm/㎏ ):숫자
# Creatinine (㎎/㎗   ):숫자
pattern_dict["(Creatinine+[^0-9]+[0-9. ]+)"] = "크레아티닌 "

# pattern_dict[
#     '(([0-9]{4}-[0-9]{2}-[0-9]{2})+[ \[]+[a-zA-Z ]+[\] :]+Any PH)']  # 4자리숫자-2자리숫자-2자리숫자 [영문 | 공백] : Any PH
# pattern_dict[
#     '(([0-9]{4}-[0-9]{2}-[0-9]{2})+[ \[]+[a-zA-Z ]+[\] :]+Any mmHg)']  # 4자리숫자-2자리숫자-2자리숫자 [영문 | 공백] : Any mmHg


# 특수문자들 (따옴표, 쉼표, 마침표, 콤마 등)
remove_pattern_dict = {}
remove_pattern_dict["([^0-9a-zA-Zㄱ-ㅣ가-힣 \n])"] = ""
remove_pattern_dict["([0-9])"] = ""  # 숫자

try:
    """
    input.txt를 불러올 때는 행을 기준으로 데이터를 불러오지만, 처리는 단락을 기준으로 하기 때문에
    행이 비어있지 않고, 내용이 들어있을 때 (else문에서) note_str에 문자열을 이어붙히고
    행이 비어 있을 때 (if문에서) 이어붙혀진 note_str의 제거문자열을 제거하고, 동의어사전을 기반으로 번역작업 수행
    수행 후, output file에 write할 output_list에 넣어준다.
    """

    note_str = ""
    for idx in range(1, len(input_list)):  # 첫째줄을 제외하고 input.txt의 행을 기준으로 데이터를 처리
        print(f"{idx} of {len(input_list)}")

        if input_list[idx] == "\n":  # 행이 비어 있을 때
            # 빈 문자열을 가진 행을 만나거나 콤마(,)만 포함된 문자열을 가진 행이 있다면 이전까지의 문자열을 합쳐 하나의 입력데이터로 만든다.
            if note_str == "" or note_str == " " or note_str == "," or note_str == "\n":
                pass

            else:
                # 사전에 정의한 패턴을 탐색하여 치환
                note_str = replace_string_pattern(note_str, pattern_dict)

                # en2ko_dictionary 기반 번역 작업
                note_str = translation(note_str)

                # 특수문자 제거
                note_str = replace_string_pattern(
                    note_str, remove_pattern_dict)

                # 행의 시작이 공백이나 특수문자로 시작된다면 해당 문자를 모두 제거
                note_str = note_str.lstrip()  # 왼쪽의 공백 삭제하기
                note_str = note_str.lstrip(string.punctuation)  # 왼쪽의 구두점 삭제

                # 불필요한 문자열 제거 후
                if (
                    note_str == ""
                    or note_str == " "
                    or note_str == ","
                    or note_str == "\n"
                ):
                    # 만약 불필요한 문자열을 제거하였는데 남은게 없다면
                    pass

                else:
                    note_str += "\n\n"
                    output_list.append(note_str)
                    note_str = "\n"

        else:  # 행이 비어있지 않고, 내용이 들어있을 때
            note_str += input_list[idx][:-1]


except Exception as e:  # 입력 번역사전 텍스트파일을 처리하는 도중 혹은 입력 텍스트파일을 처리하는 도중에 문제가 생기는 경우
    print("Error가 발생했습니다.", e)
    print("문제가 발생한 위치 :", idx)  # 문제가 발생한 위치와 이유를 출력하고 처리를 중지


print("입력 텍스트파일에서 읽은 행의 개수", len(input_list))
print("입력 번역사전에서 읽어들인 용어의 개수", len(dic_df) - 1)
print("만들어진 입력데이터의 개수", len(output_list))

output.writelines(output_list)

output.close()
input.close()
