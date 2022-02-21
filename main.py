# -*- coding: utf-8 -*-

"""
1. 단어 정규화 (word_normalization.py)
2. 검사_측정 (test_and_measurement_normalization)
3. 약물명 (drug_name_translation)
4. En2Ko (en2ko_translation)
5. 약어 사전 (abbreviation_translation)
6. 토큰화 (tokenization)
"""

import re
# import string  # string.punctuation 사용하기 위해 import

from word_normalization import word_normalization
from test_and_measurement_normalization import test_and_measurement_tagging
from drug_name_translation import drug_name_translation
from en2ko_translation import en2ko_translation, print_dic_length
from abbreviation_translation import abbreviation_translation
from tokenization import get_nouns, get_freq
from gensim.models import Word2Vec

# input_txt = open("data/input.txt", mode="r", encoding="utf-8")
# output_txt = open("data/input_ko.txt", mode="w", encoding="utf-8")

input_txt = open("data/input_ko.txt", mode="r", encoding="utf-8")
output_txt = open("data/input_ko_tokened.txt", mode="w", encoding="utf-8")

# input_txt = open("data/input_ko_tokened.txt", mode="r", encoding="utf-8")
# output_txt = open("data/input_ko_vectored.txt", mode="w", encoding="utf-8")


input_list = input_txt.readlines()  # 입력 텍스트파일의 데이터를 리스트 형태로 변환함
output_list = ["#ProcessedData\n"]

# 특수문자들 (따옴표, 쉼표, 마침표, 콤마 등)
remove_pattern_dict = {"([^0-9a-zA-Zㄱ-ㅣ가-힣 \n])": "", "([0-9])": ""}


# 사전에 정의한 제거문자열 패턴을 탐색하여 제거하는 함수
def replace_string_pattern(input_str, pattern_dict):
    for p, r in pattern_dict.items():
        input_str = re.sub(pattern=p, repl=r, string=input_str)

    return input_str


try:
    """
    input.txt를 불러올 때는 행을 기준으로 데이터를 불러오지만, 처리는 단락을 기준으로 하기 때문에
    행이 비어있지 않고, 내용이 들어있을 때 (else문에서) note_str에 문자열을 이어붙히고
    행이 비어 있을 때 (if문에서) 이어붙혀진 note_str의 제거문자열을 제거하고, 동의어사전을 기반으로 번역작업 수행
    수행 후, output file에 write할 output_list에 넣어준다.
    """

    note_str = ""
    docs = []
    tokenized_data = []
    for idx in range(1, len(input_list)):  # 첫째줄을 제외하고 input.text 행을 기준으로 데이터를 처리
        print(f"{idx} of {len(input_list)}")

        if input_list[idx] == "\n":  # 행이 비어 있을 때
            # 빈 문자열을 가진 행을 만나거나 콤마(,)만 포함된 문자열을 가진 행이 있다면 이전까지의 문자열을 합쳐 하나의 입력데이터로 만든다.
            if note_str == "" or note_str == " " or note_str == "," or note_str == "\n":
                pass

            else:
                note_str = note_str.replace("\\n", " ")

                note_str = word_normalization(note_str)  # 단어 정규화 (word_normalization.py)
                note_str = test_and_measurement_tagging(note_str)  # 검사_측정 (test_and_measurement_normalization)
                note_str = drug_name_translation(note_str)  # 약물명 (drug_name_translation)
                note_str = en2ko_translation(note_str)  # En2Ko (en2ko_translation)
                note_str = abbreviation_translation(note_str)  # 약어 사전 (abbreviation_translation)
                note_str, tokened_list = get_nouns(note_str)

                docs.append(note_str)
                tokenized_data.append(tokened_list)
                # 특수문자 제거
                # note_str = replace_string_pattern(note_str, remove_pattern_dict)

                # 행의 시작이 공백이나 특수문자로 시작된다면 해당 문자를 모두 제거
                # note_str = note_str.lstrip()  # 왼쪽의 공백 삭제하기
                # note_str = note_str.lstrip(string.punctuation)  # 왼쪽의 구두점 삭제

                # 불필요한 문자열 제거 후
                if note_str == "" or note_str == " " or note_str == "," or note_str == "\n":
                    # 만약 불필요한 문자열을 제거하였는데 남은게 없다면
                    pass

                else:
                    note_str += "\n\n"
                    output_list.append(note_str)
                    note_str = "\n"

        else:  # 행이 비어있지 않고, 내용이 들어있을 때
            note_str += input_list[idx][:-1]

    # dtm을 구하는 코드
    get_freq(docs)

    # Word2Vec 모델을 학습시켜 저장하는 코드
    model = Word2Vec(sentences=tokenized_data, vector_size=100, window=5, min_count=5, workers=4, sg=0)
    model.wv.save_word2vec_format("kr_w2v")


except Exception as e:  # 입력 번역사전 텍스트파일을 처리하는 도중 혹은 입력 텍스트파일을 처리하는 도중에 문제가 생기는 경우
    print("Error가 발생했습니다. : ", e)
    print("문제가 발생한 위치 :", idx)  # 문제가 발생한 위치와 이유를 출력하고 처리를 중지

print("입력 텍스트파일에서 읽은 행의 개수", len(input_list))
print_dic_length()
print("만들어진 입력데이터의 개수", len(output_list))

output_txt.writelines(output_list)

output_txt.close()
input_txt.close()
