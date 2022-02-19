# -*- coding: utf-8 -*-

# !pip install konlpy
# JPype 설치 필수
# 방법 : https://wikidocs.net/22488의 "5. 윈도우에서 KoNLPy 에러가 발생하는 경우"를 참고

from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Hannanum
# from konlpy.tag import Okt
import pandas as pd
import re

hannanum = Hannanum()
# okt = Okt()


def get_nouns(input_str):
    if bool(re.search("</검사측정/>", input_str)):  # input_str에 tag가 포함되어 있는 경우
        input_str = re.sub("(^|(?<=<검사측정>)).*?($|(?=</검사측정/>))", "검사측정", input_str)
        input_str = input_str.replace("<검사측정>", "")
        input_str = input_str.replace("</검사측정/>", "")

    tokened_list = hannanum.nouns(input_str)
    output_str = ", ".join(tokened_list)
    # output_str = " ".join(okt.nouns(input_str))

    return " " + output_str + " ", tokened_list


def get_freq(corpus):
    vector = CountVectorizer()

    nd_array = vector.fit_transform(corpus).toarray()
    vocab_dict = vector.vocabulary_

    sorted_list = sorted(vocab_dict.items(), key=lambda x: x[1])

    vocab_list = []
    for t in sorted_list:
        vocab_list.append(t[0])

    tf_ = pd.DataFrame(nd_array, columns=vocab_list)
    # tf_.to_csv("data/dtm.csv", mode='w', encoding='utf-8')  # , encoding='euc-kr'

    tf_ = tf_.transpose()

    tf_['freq'] = tf_.sum(axis=1)
    tf_ = tf_[['freq']]
    freq_df = tf_.sort_values('freq', ascending=False)
    freq_df.to_csv("data/freq.csv", mode='w', encoding='utf-8')  # , encoding='euc-kr'
    print("Saved freq.csv!\n")
