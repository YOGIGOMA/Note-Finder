# Word Finder in Clinic Note.

## Change Log
날짜의 역순으로 변경이력을 기록하세요.

### 2022-01-29
- `test_and_measurement_normalization.py`를 수정하였습니다.
  - 사전에 정규 표현식 패턴을 컴파일하여 `compiled_test_and_measurement` 리스트에 저장 
  - `test_and_measurement_tagging` 함수 내에 문자열 치환하는 과정에서의 오류 수정

### 2022-01-27
- 영문2한글의 작업순서가 변경됨에 따라 note_str의 처리 순서를 수정하였습니다.
  - `abbreviation_translation` (약어 번역 작업)의 순서를 맨 마지막으로 변경

### 2022-01-26
- 프로그램을 함수화하였습니다.
  - `word_normalization.py`는 단어들을 정규화하여 처리합니다.
  - `test_and_measurement_normalization.py`는 검사, 측정 문자들의 앞뒤에 태그를 부착해주는 파일입니다.
  - `drug_name_translation.py`는 `drug_name_dictionary.csv`을 기반으로 translation 하는 합니다.
  - `abbreviation_translation.py`는 `abbreviation_dictionart.csv`을 기반으로 translation 합니다.
  - `en2ko_translation.py`는 `en2ko_dictionary`를 기반으로 영문을 국문으로 변환합니다.

- 기존의 `korean_translation.py`의 파일명을 `main.py`로 바꾸고, 부분수정하였습니다.

### 2022-01-20
- `translation` 함수 기능 향상
  - 2021-01-11에 commit한 단어 앞뒤에 `ㅤ`(띄어쓰기)를 포함하는 코드 삭제
  - 번역사전에서  `#en`과 `#ko`에 공백이 들어가있는 경우 (단어 중간 제외), 발생하는 오류를 막기 위해 `#en`과 `#ko`에 `strip()` 처리

### 2022-01-11
- 업데이트된 단어 정규화에 대응하기 위해 replace_string_pattern 전면 수정 (공유 드라이브 '영문2한글' 파일 참고)
- 업데이트된 번역사전에 대응하기 위해 코드 수정
  - `translation` 함수에서 기존의 `eng`를 `한국어`로 바꾸는 코드를
  - 단어 앞뒤에 `ㅤ`(띄어쓰기)를 포함하여 `ㅤengㅤ`를 `ㅤ한국어ㅤ`로 바꾸도록 수정

### 2022-01-05
- 데이터를 구별할 수 있도록 데이터 사이에 빈 줄 삽입
- 원본 데이터가 모두 삭제되는 경우에 생기는 빈 줄 삭제
- 불필요한 문자열을 제거 한 후에 왼쪽의 공백과 구두점을 삭제하도록 순서 변경

### 2021-12-31
- 모든 특수문자를 제거하도록 수정
- 변경된 형식의 번역사전에 대응하도록 수정
- 데이터 처리 방식을 한 줄에서 한 단락씩 하도록 수정

### 2021-12-28
- 'en2ko_dictionary.csv'를 열 때 발생하는 `UnicodeDecodeError` 수정

### 2021-12-26
- 번역사전 기반 번역처리 함수 구현

### 2021-12-25
- 파일입출력, 제거문자열 패턴 등 전반적인 기능 구현
