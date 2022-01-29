# 검사, 측정 문자들의 앞뒤에 태그를 부착합니다.
# 이때, 태그가 붙은 문자들의 영어나 숫자는 추후에 제거되지 않아야 합니다.
import re

compiled_test_and_measurement = []

compiled_test_and_measurement.append(re.compile("(NIBP_평균+\(mmHg\)+[ :]+[0-9]{2,3})"))  # "평균혈압" ex> NIBP_평균(mmHg) : 숫자
compiled_test_and_measurement.append(re.compile("(NIBP_이완기+\(mmHg\)+[ :]+[0-9]{2,3})"))  # "이완기혈압 " ex> NIBP_이완기(mmHg) : 숫자
compiled_test_and_measurement.append(re.compile("(NIBP_수축기+\(mmHg\)+[ :]+[0-9]{2,3})"))  # "수축기혈압 " ex> NIBP_수축기(mmHg) : 숫자
compiled_test_and_measurement.append(re.compile("(PR\s*\(회\)+[ :]+[0-9]{2,3})"))  # "맥박" ex> PR(회) : 숫자
compiled_test_and_measurement.append(re.compile("(RR\s*\(회\)+[ :]+[0-9]{2,3})"))  # "호흡수" ex> RR(회) : 숫자
compiled_test_and_measurement.append(re.compile("(BT\(℃\)+[ :]+[0-9.]{2,4})"))  # "체온" ex> BT(℃) : 숫자
compiled_test_and_measurement.append(re.compile("(SpO₂\s*\(%\)[ :]+[0-9.]+)"))  # "말초산소포화도" ex> SpO₂(%) : 숫자
compiled_test_and_measurement.append(re.compile("(Device+\s*:\s*[a-zA-Z]+)"))  # "기기 " ex> Device : 영문자
compiled_test_and_measurement.append(re.compile("(Event-1\s*:\s*[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+\s*:\s*[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+ [가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+)"))  # "사건" ex> Event-1: 단어: (단어)*n
compiled_test_and_measurement.append(re.compile("(FiO₂\s*\(%\)[ :]+[0-9.]+)"))  # "흡입산소농도 " ex> FiO₂(%) : 숫자
compiled_test_and_measurement.append(re.compile("(O₂\s*Flow(L\/min)\s*:\s*[0-9. ]+)"))  # "산소유량 " ex> O₂ Flow(L/min) : 숫자
compiled_test_and_measurement.append(re.compile("(pH+[▲▼: ]+[0-9. ]+pH)"))  # "수소이온농도" ex> pH : 숫자 pH
compiled_test_and_measurement.append(re.compile("(pCO2+[▲▼: ]+[0-9. ]+mmHg)"))  # "이산화탄소농도" ex> pCO2 : 숫자 mmHg
compiled_test_and_measurement.append(re.compile("(pO2+[▲▼: ]+[0-9. ]+mmHg)"))  # "산소농도" ex> pO2 : 숫자 mmHg
compiled_test_and_measurement.append(re.compile("(EVM\s*:\sE[0-9]V[0-9]M[0-9])"))  # "눈뜨기,언어,근력" ex> EVM : E숫자V숫자M숫자
compiled_test_and_measurement.append(re.compile("(PS LR\s*(R/L)\s*:\s[a-zA-Z0-9]+\s*\/\s*[a-zA-Z0-9]+)"))  # "동공크기" ex> PS LR(R/L) : 문자/문자
compiled_test_and_measurement.append(re.compile("(의식상태\s*:\s[^0-9]+)"))  # "동공빛반사" ex> 의식상태 : 단어
compiled_test_and_measurement.append(re.compile("(Pupil shape\s*:\s[^0-9]+\s*\/\s*[^0-9]+)"))  # " " ex> Pupil shape : 단어/단어
compiled_test_and_measurement.append(re.compile("(Hemoglobin,\s*Blood+[▲▼: ]+[0-9.]+)"))  # "헤모글로빈" ex> Hemoglobin, Blood 숫자
compiled_test_and_measurement.append(re.compile("(Albumin\s*\(g\/㎗\s*\)\s*:\s*[▲▼0-9.]+)"))  # "알부민" ex> Albumin (g/㎗    ): 숫자
compiled_test_and_measurement.append(re.compile("(Location\s*1\s*:\s*[^0-9]+)"))  # "측정위치" ex> Location 1 : 단어
compiled_test_and_measurement.append(re.compile("(Comment\s*:\s*[^0-9]+)"))  # "코멘트" ex> Comment : 단어
compiled_test_and_measurement.append(re.compile("(Potassium\s*\(K\)\s*:\s[▲▼0-9.]+\s*mmol\/ℓ)"))  # "포타슘" ex> Potassium (K) : 숫자 mmol/ℓ
compiled_test_and_measurement.append(re.compile("(ANC\s*\(Absolute\s*Neutrophil\s*Count\))"))  # "절대호중구수" ex> ANC (Absolute Neutrophil Count)
compiled_test_and_measurement.append(re.compile("(APTT\s*:\s[▲▼0-9.]+sec)"))  # "활성화부분트롬보플라스틴시간" ex> APTT : 실수 sec
compiled_test_and_measurement.append(re.compile("(Mg\s*:\s[▲▼0-9.]+㎎/㎗)"))  # "마그네슘" ex> Mg : 숫자 ㎎/㎗
compiled_test_and_measurement.append(re.compile("(Osmolality,\s*Serum\s*\(mOsm/㎏\s*\)\s*:\s*[0-9]+)"))  # "혈청삼투압농도" ex> Osmolality, Serum (mOsm/㎏ ):숫자
compiled_test_and_measurement.append(re.compile("(Creatinine\s*\(㎎/㎗\s*\)\s*:\s*[0-9.]+)"))  # "크레아티닌" ex> Creatinine (㎎/㎗   ):숫자


def test_and_measurement_tagging(input_str):
    for obj in compiled_test_and_measurement:
        result = obj.finditer(input_str)
        for m in result:
            temp_str = m.group()
            input_str = input_str.replace(temp_str, "<검사측정>" + temp_str + "</검사측정/>")
    return input_str
