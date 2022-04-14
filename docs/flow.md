# Process of Fall Detection in Clinic Note

## Phase 1. Pre-Preprocessing

### 1. 데이터 전처리

#### 1) 개행 문자 제거

#### 2) 단어 정규화

#### 3) 검사 측정 구문 제거

#### 4) 대문자를 소문자로 변환

#### 5) 약물명 번역

#### 6) En2Ko 번역

#### 7) 약어 번역

#### 8) 불용어 삭제

#### 9) 남은 영어, 숫자, 특수문자 삭제

### 2. 단어 토큰화

#### 1) 동사, 명사, 부사의 형태소 분석을 통해 토큰화

#### 2) (필요 시) Term Frequency 추출

---

## Phase 2. (필요 시) Word2Vec 모델 학습

---

## Phase 3. Text Classification

### 1. 데이터 준비

#### 1) 모델 학습 전 오버샘플링

#### 2) train, val, test 데이터 분할 (train_test_split)

### 2. FastText를 통한 Text Classification

#### 1) fasttext 라이브러리 설치 및 불러오기

#### 2) FastText 학습을 위한 .txt 파일 생성

#### 3) FastText 모델 학습 및 추론

#### 4) 성능 평가
