# -*- coding: utf-8 -*-
import re
import string  # string.punctuation 사용하기 위해 import
import pandas as pd


def translation(input_str):
    for i in range(len(dic_df)):
        input_str = re.sub(dic_df.loc[i]["#en"],
                           dic_df.loc[i]["#ko"], input_str)
    return input_str


def remove_string_pattern(input_str):  # 사전에 정의한 제거문자열 패턴을 탐색하여 제거하는 함수
    pattern_list = []

    pattern_list.append('(NIBP_+[^0-9]+[0-9. ]+)')  # NIBP_문자열 : 숫자
    pattern_list.append('(PR+[^0-9]+[0-9. ]+)')  # PR문자열 : 숫자
    pattern_list.append('(RR+[^0-9]+[0-9. ]+)')  # RR문자열 : 숫자
    pattern_list.append('(BT+[^0-9]+[0-9. ]+)')  # BT문자열 : 숫자
    pattern_list.append('(SpO+[^0-9]+[0-9. ]+)')  # SpO문자열 : 숫자
    pattern_list.append('(Device+[^0-9]+[a-zA-Z]+)')  # Device : 영문자
    pattern_list.append(
        '(([0-9]{4}-[0-9]{2}-[0-9]{2})+[ \[]+[a-zA-Z ]+[\] :]+Any PH)')  # 4자리숫자-2자리숫자-2자리숫자 [영문 | 공백] : Any PH
    pattern_list.append(
        '(([0-9]{4}-[0-9]{2}-[0-9]{2})+[ \[]+[a-zA-Z ]+[\] :]+Any mmHg)')  # 4자리숫자-2자리숫자-2자리숫자 [영문 | 공백] : Any mmHg
    # 특수문자들 (따옴표, 쉼표, 마침표, 콤마 등)
    pattern_list.append('([^0-9a-zA-Zㄱ-ㅣ가-힣 \n])')
    pattern_list.append('([0-9])')  # 숫자

    repl = ''

    for p in pattern_list:
        input_str = re.sub(pattern=p, repl=repl, string=input_str)

    return input_str


input = open("data/input.txt", mode="r", encoding="utf-8")
output = open("data/input_ko.txt", mode="w", encoding="utf-8")

input_list = input.readlines()  # 입력 텍스트파일의 데이터를 리스트 형태로 변환함
output_list = ["#ProcessedData\n"]

dic_df = pd.read_csv('data/en2ko_dictionary.csv',
                     encoding="utf-8", low_memory=False)


try:
    '''
    input.txt를 불러올 때는 행을 기준으로 데이터를 불러오지만, 처리는 단락을 기준으로 하기 때문에
    행이 비어있지 않고, 내용이 들어있을 때 (else문에서) note_str에 문자열을 이어붙히고 
    행이 비어 있을 때 (if문에서) 이어붙혀진 note_str의 제거문자열을 제거하고, 동의어사전을 기반으로 번역작업 수행
    수행 후, output file에 write할 output_list에 넣어준다.
    '''

    note_str = ""
    for idx in range(1, len(input_list)):  # 첫째줄을 제외하고 input.txt의 행을 기준으로 데이터를 처리
        if input_list[idx] == "\n":  # 행이 비어 있을 때
            # 빈 문자열을 가진 행을 만나거나 콤마(,)만 포함된 문자열을 가진 행이 있다면 이전까지의 문자열을 합쳐 하나의 입력데이터로 만든다.
            if (note_str == "" or note_str == " " or note_str == "," or note_str == "\n"):
                pass

            else:
                note_str = remove_string_pattern(
                    note_str)  # 사전에 정의한 제거문자열 패턴을 탐색하여 제거

                note_str = translation(note_str)

                # 행의 시작이 공백이나 특수문자로 시작된다면 해당 문자를 모두 제거
                note_str = note_str.lstrip()  # 왼쪽의 공백 삭제하기
                note_str = note_str.lstrip(
                    string.punctuation)  # 왼쪽의 구두점 삭제

                # 불필요한 문자열 제거 후
                if (note_str == "" or note_str == " " or note_str == "," or note_str == "\n"):
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
print("입력 번역사전에서 읽어들인 용어의 개수", len(dic_df)-1)
print("만들어진 입력데이터의 개수", len(output_list))

output.writelines(output_list)

output.close()
input.close()
