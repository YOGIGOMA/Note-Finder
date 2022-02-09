# 검사, 측정 문자들의 앞뒤에 태그를 부착합니다.
# 이때, 태그가 붙은 문자들의 영어나 숫자는 추후에 제거되지 않아야 합니다.
import re

compiled_test_and_measurement = [re.compile("(NIBP_평균+\(mmHg\)+[ :]+[0-9]{2,3})"),
                                 re.compile("(NIBP_이완기+\(mmHg\)+[ :]+[0-9]{2,3})"),
                                 re.compile("(NIBP_수축기+\(mmHg\)+[ :]+[0-9]{2,3})"),
                                 re.compile("(PR\s*\(회\)+[ :]+[0-9]{2,3})"), re.compile("(RR\s*\(회\)+[ :]+[0-9]{2,3})"),
                                 re.compile("(BT\(℃\)+[ :]+[0-9.]{2,4})"), re.compile("(SpO₂\s*\(%\)[ :]+[0-9.]+)"),
                                 re.compile("(Device+\s*:\s*[a-zA-Z]+)"), re.compile(
        '(Event-1\s*:\s*[0-9가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]+\s*:\s*[0-9가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z,]+ [0-9가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z,]*)'),
                                 re.compile("(FiO₂\s*\(%\)[ :]+[0-9.]+)"),
                                 re.compile("(O₂\s*Flow(L\/min)\s*:\s*[0-9. ]+)"), re.compile("(pH+[▲▼: ]+[0-9. ]+pH)"),
                                 re.compile("(pCO2+[▲▼: ]+[0-9. ]+mmHg)"), re.compile("(pO2+[▲▼: ]+[0-9. ]+mmHg)"),
                                 re.compile("(EVM\s*:\sE[0-9]V[0-9]M[0-9])"),
                                 re.compile("(PS LR\s*(R/L)\s*:\s[a-zA-Z0-9]+\s*\/\s*[a-zA-Z0-9]+)"),
                                 re.compile("(의식상태\s*:\s[^0-9]+)"),
                                 re.compile("(Pupil shape\s*:\s[^0-9]+\s*\/\s*[^0-9]+)"),
                                 re.compile("(Hemoglobin,\s*Blood+[▲▼: ]+[0-9.]+)"),
                                 re.compile("(Albumin\s*\(g\/㎗\s*\)\s*:\s*[▲▼0-9.]+)"),
                                 re.compile("(Location\s*1\s*:\s*[^0-9]+)"), re.compile("(Comment\s*:\s*[^0-9]+)"),
                                 re.compile("(Potassium\s*\(K\)\s*:\s[▲▼0-9.]+\s*mmol\/ℓ)"),
                                 re.compile("(ANC\s*\(Absolute\s*Neutrophil\s*Count\))"),
                                 re.compile("(APTT\s*:\s[▲▼0-9.]+sec)"), re.compile("(Mg\s*:\s[▲▼0-9.]+㎎/㎗)"),
                                 re.compile("(Osmolality,\s*Serum\s*\(mOsm/㎏\s*\)\s*:\s*[0-9]+)"),
                                 re.compile("(Creatinine\s*\(㎎/㎗\s*\)\s*:\s*[0-9.]+)")]


def test_and_measurement_tagging(input_str):
    for obj in compiled_test_and_measurement:
        result = obj.finditer(input_str)
        for m in result:
            temp_str = m.group()
            input_str = input_str.replace(temp_str, "<검사측정>" + temp_str + "</검사측정/>")

    return lower_except_tag(input_str)


def lower_except_tag(input_str):
    if bool(re.search("</검사측정/>", input_str)):  # input_str에 tag가 포함되어 있는 경우
        return re.sub("(^|(?<=</검사측정/>)).*?($|(?=<검사측정>))", lambda m: m.group().lower(), input_str)

    else:  # input_str에 tag가 포함되어 있지 않은 경우
        # 모든 알파벳을 소문자로 만듬
        return input_str.lower()
