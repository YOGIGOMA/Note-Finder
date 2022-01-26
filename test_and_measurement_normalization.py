# 검사, 측정 문자들의 앞뒤에 태그를 부착합니다.
# 이때, 태그가 붙은 문자들의 영어나 숫자는 추후에 제거되지 않아야 합니다.
import re

test_and_measurement_pattern = {}

test_and_measurement_pattern["(NIBP_평균+\(mmHg\)+[ :]+[0-9]{2,3})"] = "평균혈압"  # NIBP_평균(mmHg) : 숫자
test_and_measurement_pattern["(NIBP_이완기+\(mmHg\)+[ :]+[0-9]{2,3})"] = "이완기혈압 "  # NIBP_이완기(mmHg) : 숫자
test_and_measurement_pattern["(NIBP_수축기+\(mmHg\)+[ :]+[0-9]{2,3})"] = "수축기혈압 "  # NIBP_수축기(mmHg) : 숫자
test_and_measurement_pattern["(PR\s*\(회\)+[ :]+[0-9]{2,3})"] = "맥박"  # PR(회) : 숫자
test_and_measurement_pattern["(RR\s*\(회\)+[ :]+[0-9]{2,3})"] = "호흡수"  # RR(회) : 숫자
test_and_measurement_pattern["(BT\(℃\)+[ :]+[0-9.]{2,4})"] = "체온"  # BT(℃) : 숫자
test_and_measurement_pattern["(SpO₂\s*\(%\)[ :]+[0-9.]+)"] = "말초산소포화도"  # SpO₂(%) : 숫자
test_and_measurement_pattern["(Device+\s*:\s*[a-zA-Z]+)"] = "기기 "  # Device : 영문자
test_and_measurement_pattern["(Event-1\s*:\s*[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+\s*:\s*[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+ [가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+)"] = "사건"  # Event-1: 단어: (단어)*n
test_and_measurement_pattern["(FiO₂\s*\(%\)[ :]+[0-9.]+)"] = "흡입산소농도 "  # FiO₂(%) : 숫자
test_and_measurement_pattern["(O₂\s*Flow(L\/min)\s*:\s*[0-9. ]+)"] = "산소유량 "  # O₂ Flow(L/min) : 숫자
test_and_measurement_pattern["(pH+[▲▼: ]+[0-9. ]+pH)"] = "수소이온농도"  # pH : 숫자 pH
test_and_measurement_pattern["(pCO2+[▲▼: ]+[0-9. ]+mmHg)"] = "이산화탄소농도"  # pCO2 : 숫자 mmHg
test_and_measurement_pattern["(pO2+[▲▼: ]+[0-9. ]+mmHg)"] = "산소농도"  # pO2 : 숫자 mmHg
test_and_measurement_pattern["(EVM\s*:\sE[0-9]V[0-9]M[0-9])"] = "눈뜨기,언어,근력"# EVM : E숫자V숫자M숫자
test_and_measurement_pattern["(PS LR\s*(R/L)\s*:\s[a-zA-Z0-9]+\s*\/\s*[a-zA-Z0-9]+)"] = "동공크기"  # PS LR(R/L) : 문자/문자
test_and_measurement_pattern["(의식상태\s*:\s[^0-9]+)"] = "동공빛반사"  # 의식상태 : 단어
test_and_measurement_pattern["(Pupil shape\s*:\s[^0-9]+\s*\/\s*[^0-9]+)"] = " " # Pupil shape : 단어/단어
test_and_measurement_pattern["(Hemoglobin,\s*Blood+[▲▼: ]+[0-9.]+)"] = "헤모글로빈" # Hemoglobin, Blood 숫자
test_and_measurement_pattern["(Albumin\s*\(g\/㎗\s*\)\s*:\s*[▲▼0-9.]+)"] = "알부민"  # Albumin (g/㎗    ): 숫자
test_and_measurement_pattern["(Location\s*1\s*:\s*[^0-9]+)"] = "측정위치"  # Location 1 : 단어
test_and_measurement_pattern["(Comment\s*:\s*[^0-9]+)"] = "코멘트"  # Comment : 단어
test_and_measurement_pattern["(Potassium\s*\(K\)\s*:\s[▲▼0-9.]+\s*mmol\/ℓ)"] = "포타슘"  # Potassium (K) : 숫자 mmol/ℓ

test_and_measurement_pattern["(ANC\s*\(Absolute\s*Neutrophil\s*Count\))"] = "절대호중구수"  # ANC (Absolute Neutrophil Count)
test_and_measurement_pattern["(APTT\s*:\s[▲▼0-9.]+sec)"] = "활성화부분트롬보플라스틴시간"  # APTT : 실수 sec
test_and_measurement_pattern["(Mg\s*:\s[▲▼0-9.]+㎎/㎗)"] = "마그네슘"  # Mg : 숫자 ㎎/㎗
test_and_measurement_pattern["(Osmolality,\s*Serum\s*\(mOsm/㎏\s*\)\s*:\s*[0-9]+)"] = "혈청삼투압농도"  # Osmolality, Serum (mOsm/㎏ ):숫자
test_and_measurement_pattern["(Creatinine\s*\(㎎/㎗\s*\)\s*:\s*[0-9.]+)"] = "크레아티닌" # C reatinine (㎎/㎗   ):숫자

# test_and_measurement_pattern['(([0-9]{4}-[0-9]{2}-[0-9]{2})+[ \[]+[a-zA-Z ]+[\] :]+Any PH)']  # 4자리숫자-2자리숫자-2자리숫자 [영문 | 공백] : Any PH
# test_and_measurement_pattern['(([0-9]{4}-[0-9]{2}-[0-9]{2})+[ \[]+[a-zA-Z ]+[\] :]+Any mmHg)']  # 4자리숫자-2자리숫자-2자리숫자 [영문 | 공백] : Any mmHg

def test_and_measurement_tagging(input_str):
    for key in test_and_measurement_pattern.keys():
        input_str = re.sub(pattern=key, repl="<검사측정>"+input_str+"</검사측정/>", string=input_str)

    return input_str