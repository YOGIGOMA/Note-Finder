# Process of Fall Detection in Clinic Note

**Flow Chart** 확인하려면 [**클릭**](https://oneonlee.github.io/Note-Finder/docs/etc/flow.html)

## Phase 1. Pre-Preprocessing

### 0. 라이브러리 설치 및 파일 불러오기

- 라이브러리 설치 및 불러오기
- 파일 불러오기 (data, dictionary 등)
  - dictionary 중복 여부 확인
  - 원본 데이터 알아보기
    - 결측값 여부 확인
    - 낙상 데이터와 비낙상 데이터의 개수, 비율 확인

### 1. 데이터 전처리

- 1. 개행 문자 제거
- 2. 단어 정규화
- 3. 검사 측정 구문 제거
- 4. 대문자를 소문자로 변환
- 5. 약물명 번역
- 6. En2Ko 번역
- 7. 약어 번역
- 8. 동의어 처리
- 9. 단어 통합 처리
- 10. 불용어 삭제
- 11. 남은 영어, 숫자, 특수문자 삭제

### 2. 단어 토큰화

- 동사, 명사, 부사의 형태소 분석을 통해 토큰화
- Term Frequency 추출

---

## Phase 2. (필요 시) Word2Vec 모델 학습

---

## Phase 3. FastText를 통한 Text Classification

- 모델 학습 전 imblearn 라이브러리를 활용한 오버샘플링
- sklearn 라이브러리를 활용한 train, val, test 데이터 분할 (train_test_split)

<!-- ### A. LSTM으로 낙상 데이터 이진 분류하기 -->


- 1. fasttext 라이브러리 설치 및 불러오기
- 2. FastText 학습을 위한 .txt 파일 생성
- 3. FastText 모델 학습 및 추론

### 2022. 04. 11. 분석 결과

**[결론 먼저 확인하고 싶으면 클릭](#결론)**

| Data Info.                | label 0 (Non-Fall) | label 1 (Fall) | Total           |
| ------------------------- | ------------------ | -------------- | --------------- |
| Original Data             | 9838 (52.638%)     | 8852 (47.362%) | 18690           |
| Resampled Data            | 9838 (50%)         | 9838 (50%)     | 19676 (100%)    |
| Resampled Training Data   | 5901 (50.013%)     | 5901 (49.987%) | 11805 (59.997%) |
| Resampled Validation Data | 1002 (50.863%)     | 968 (49.137%)  | 1970 (10.012%)  |
| Resampled Testing Data    | 2935 (49.712%)     | 2969 (50.288%) | 5904 (30.006%)  |

2022년 04월 11일 분석에서는 Original Data를 오버샘플링 기법으로 데이터를 늘려 Resampled Data를 생성하였다. 또한, 그 Resampled Data를 60:10:30의 비율로 각각 Traing Data, Validation Data, Testing Data로 구성하였다.

위 표는 앞서 설명한 5가지 종류의 데이터들에 대한 label의 비율과 데이터의 비율을 나타낸 표이다.

Original Data에서 비낙상:낙상의 비율이 52:47이었지만, 오버샘플링을 한 데이터들은 비율이 50:50으로 고정된 것을 확인할 수 있다. 비율이 52:47에서 50:50으로 맞춰준 이 과정이 효과가 없고 비효율적으로 느껴질 수 있지만, 추후 Original Data의 비율이 imbalance 할 때의 상황을 대비한 것이다.

<br>

| UsedData       | Raw Data                    | Processed Data          | Tokenized Data              |
| -------------- | --------------------------- | ----------------------- | --------------------------- |
| Precision      | [**0.99383562** 0.98894102] | [0.99147049 0.99024554] | [0.99046646 **0.99123694**] |
| Recall         | [0.98875639 **0.99393735**] | [0.99011925 0.99157966] | [**0.9911414** 0.99056922]  |
| F1 score       | [**0.9912895 0.99143289**]  | [0.99079441 0.99091215] | [0.99080381 0.99090296]     |
| Accuracy Score | **0.9913617886178862**      | 0.9908536585365854      | 0.9908536585365854          |

위 표는 데이터의 분석 정도(깊이)에 따른 성능을 확인할 수 있는 표이다.

Raw Data는 말그대로 원본 데이터를 의미하며, 아무런 전처리과정을 거치지 않은 데이터이다. <br>
Processed Data는 Raw Data에서 [전처리 단계](#1-데이터-전처리)를 거친 데이터를 의미한다. <br>
Tokenized Data는 Processed Data를 [토큰화](#2-단어-토큰화)시킨 데이터이다. 즉, 전처리와 토큰화 과정이 모두 거쳐진 데이터이다.

위 표의 Precision과 Recall, F1 Score의 값이 대괄호(`[ ]`)로 둘러쌓여진 것을 볼 수 있는데 이는 순서대로 Label 0(비낙상)에 대한 값과 Label 1(낙상)에 대한 값이다.

Raw Data, Processed Data, Tokenized Data 모두 (Accuracy Score 기준) 0.99이상의 성능을 보여주었다. 아무것도 처리하지 않은 data인 Raw Data의 F1 Score가 가장 높았을 뿐만 아니라 거의 모든 평가 지표에서 작지만 우세한 것을 확인할 수 있다.

#### 결론

> 1. label 비율이 53:47이었던 원본 데이터를 50:50으로 오버샘플링 하였음.

> 2. 오버샘플링한 데이터를 60:10:30의 비율의 Traing Data, Validation Data, Testing Data로 구성하였음.

> 3. Raw Data, Processed Data, Tokenized Data 중 근사한 차이지만 가장 성능이 우세한 것은 Raw Data임.


### 2022. 04. 27. 분석 결과
Training Data는 6000개 data에 KOPS data를 낙상 label과 비낙상 label이 10:90의 비율을 갖도록 구성하였다.

| Data Info.                | label 0 (Non-Fall) | label 1 (Fall) | Total |
| ------------------------- | ------------------ | -------------- | ----- |
| Training Data             | 5832 (90%)         | 648 (10%)      | 6480  |
| Testing Data              | 4006 (97%)         | 120 (3%)       | 4126  |


| TrainingData →<br> TestingData ↓ | Raw Data                                                                                                                                                                 | Processed Data                                                                                                                                                               | Tokenized Data                                                                                                                                                              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Raw Data                         | Precision: [0.9935227 0.8392857]<br> Recall: [0.9955067 0.7833333]<br> F1 score: [0.9945137 0.8103448]<br> Support: [4006  120]<br> Accuracy score: 0.9893359185         | Precision: [0.99525   0.8015873]<br> Recall: [0.9937594 **0.8416667**]<br> F1 score: [0.9945041 0.8211382]<br> Support: [4006  120]<br> Accuracy score: 0.9893359186         | Precision: [0.9829798 0.7083333]<br> Recall: [0.9947579 0.425     ]<br> F1 score: [0.9888338 0.53125   ]<br> Support: [4006  120]<br> Accuracy score: 0.9781871062          |
| Processed Data                   | Precision: [**0.9962217** 0.6730769]<br> Recall: [0.987269 0.875    ]<br> F1 score: [0.9917252 0.7608696]<br> Support: [4006  120]<br> Accuracy score: 0.9840038778      | Precision: [0.9942701 **0.8660714**]<br> Recall: [0.9962556 0.8083333]<br> F1 score: [**0.9952619** **0.836207** ]<br> Support: [4006  120]<br> Accuracy score: **0.9907901115** | Precision: [*0.9811089* 0.86      ]<br> Recall: [**0.9982526** *0.3583333*]<br> F1 score: [0.9896065 *0.5058824*]<br> Support: [4006  120]<br> Accuracy score: 0.9796412991 |
| Tokenized Data                   | Precision: [0.9913021 *0.3963134*]<br> Recall: [*0.9672991* 0.7166667]<br> F1 score: [*0.9791535* 0.5103858]<br> Support: [4006  120]<br> Accuracy score: *0.9600096946* | Precision: [0.9907754 0.7217391]<br> Recall: [0.9920120 0.6916667]<br> F1 score: [0.9913933 0.7063830]<br> Support: [4006  120]<br> Accuracy score: 0.9832767814<br>         | Precision: [0.9950075 0.8333333]<br> Recall: [0.9950075 0.8333333]<br> F1 score: [0.9950075 0.8333333]<br> Support: [4006  120]<br> Accuracy score: 0.9903053805        |

#### 결론
> 1. Training Data의 비율을 10:90으로 구성하였음
> 2. Testing Data는 Real World Data의 비율과 유사하게 3:97로 구성하였음
> 3. Training Data와 Testing Data 모두 Processed Data로 구성하였을 때가 가장 좋은 성능을 보임


### 2022. 05. 22. 분석 결과
<!-- | TrainingData →<br> TestingData ↓ | Raw Data                                                                                                                                                                 | Processed Data                                                                                                                                                               | Tokenized Data                                                                                                                                                              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Raw Data                         | Precision: [0.98865329 0.83472803]<br>Recall: [0.99436519 0.7137746 ]<br>F1 score: [0.99150101 0.76952748]<br>Accuracy score: 0.9836065573770492                         | Precision: [0.99434198 0.49690722]<br>Recall: [0.96519258 0.86225403]<br>F1 score: [0.97955047 0.63047744]<br>Accuracy score: 0.9612456272721037                             | Precision: [0.98681948 0.10245802]<br>Recall: [0.73694722 0.75313059]<br>F1 score: [0.84377297 0.18037704]<br>Accuracy score: 0.7375677344125111                            |
| Processed Data                   | Precision: [0.99000357 0.72996516]<br>Recall: [0.98894437 0.74955277]<br>F1 score: [0.98947368 0.7396293 ]<br>Accuracy score: 0.9797654160093285                         | Precision: [0.98888496 0.88546256]<br>Recall: [0.99629101 0.71914132]<br>F1 score: [0.99257417 0.79368213]<br>Accuracy score: 0.9856643116811853                             | Precision: [0.98172179 0.16898506]<br>Recall: [0.88495007 0.58676208]<br>F1 score: [0.93082752 0.2624    ]<br>Accuracy score: 0.8735167021057686                            |
| Tokenized Data                   | Precision: [0.97478933 0.5899705 ]<br>Recall: [0.99008559 0.35778175]<br>F1 score: [0.98237792 0.4454343 ]<br>Accuracy score: 0.9658412785513409                         | Precision: [0.97185154 0.80628272]<br>Recall: [0.99736091 0.27549195]<br>F1 score: [0.984441   0.41066667]<br>Accuracy score: 0.9696824199190617                             | Precision: [0.99209964 0.84688091]<br>Recall: [0.99422254 0.80143113]<br>F1 score: [0.99315996 0.82352941]<br>Accuracy score: 0.986830372453529                             |
 -->
 
| TrainingData →<br>  TestData ↓ | Raw Data                                                                                                                | Processed Data                                                                                                          | Tokenized Data                                                                                                              |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Raw Data                       | Precision        : 0.8347<br> Recall           : 0.7138<br> F1 score         : 0.7695<br> Accuracy score   : 0.9836     | Precision        : 0.7601<br> Recall           : 0.7370 <br>F1 score         : 0.7484<br> Accuracy score   : 0.9810     | Precision        : 0.6708<br> Recall           : 0.2916<br> F1 score         : 0.4065<br> Accuracy score   : 0.9674         |
| Processed Data                 | Precision        : 0.4005<br> **Recall           : 0.8640**<br> F1 score         : 0.5473<br> Accuracy score   : 0.9452 | **Precision        : 0.8822**<br> Recall           : 0.6834<br> F1 score         : 0.7702<br> Accuracy score   : 0.9844 | Precision        : 0.7711<br> Recall           : 0.2290<br> F1 score         : 0.3531<br> Accuracy score   : 0.9678         |
| Tokenized Data                 | Precision        : 0.0953<br> Recall           : 0.7567<br> F1 score         : 0.1693<br> Accuracy score   : 0.7152     | Precision        : 0.1578<br> Recall           : 0.5170<br> F1 score         : 0.2418<br> Accuracy score   : 0.8757     | Precision        : 0.8318<br> Recall           : 0.7871<br> **F1 score         : 0.8088**<br> **Accuracy score   : 0.9857** | 
 
<!-- Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
사용한 훈련 데이터 종류 : note
사용한 평가 데이터 종류 : note
Precision        : 0.8347
Recall           : 0.7138
F1 score         : 0.7695
Accuracy score   : 0.9836
[[13941    79]
 [  160   399]]

사용한 훈련 데이터 종류 : note
사용한 평가 데이터 종류 : #ProcessedData
Precision        : 0.4005
Recall           : 0.8640
F1 score         : 0.5473
Accuracy score   : 0.9452
[[13297   723]
 [   76   483]]

사용한 훈련 데이터 종류 : note
사용한 평가 데이터 종류 : #TokenizedData
Precision        : 0.0953
Recall           : 0.7567
F1 score         : 0.1693
Accuracy score   : 0.7152
[[10004  4016]
 [  136   423]]

Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
사용한 훈련 데이터 종류 : #ProcessedData
사용한 평가 데이터 종류 : note
Precision        : 0.7601
Recall           : 0.7370
F1 score         : 0.7484
Accuracy score   : 0.9810
[[13890   130]
 [  147   412]]

사용한 훈련 데이터 종류 : #ProcessedData
사용한 평가 데이터 종류 : #ProcessedData
Precision        : 0.8822
Recall           : 0.6834
F1 score         : 0.7702
Accuracy score   : 0.9844
[[13969    51]
 [  177   382]]

사용한 훈련 데이터 종류 : #ProcessedData
사용한 평가 데이터 종류 : #TokenizedData
Precision        : 0.1578
Recall           : 0.5170
F1 score         : 0.2418
Accuracy score   : 0.8757
[[12478  1542]
 [  270   289]]

Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
사용한 훈련 데이터 종류 : #TokenizedData
사용한 평가 데이터 종류 : note
Precision        : 0.6708
Recall           : 0.2916
F1 score         : 0.4065
Accuracy score   : 0.9674
[[13940    80]
 [  396   163]]

사용한 훈련 데이터 종류 : #TokenizedData
사용한 평가 데이터 종류 : #ProcessedData
Precision        : 0.7711
Recall           : 0.2290
F1 score         : 0.3531
Accuracy score   : 0.9678
[[13982    38]
 [  431   128]]

사용한 훈련 데이터 종류 : #TokenizedData
사용한 평가 데이터 종류 : #TokenizedData
Precision        : 0.8318
Recall           : 0.7871
F1 score         : 0.8088
Accuracy score   : 0.9857
[[13931    89]
 [  119   440]]
 -->

### 2022. 06. 20. 결과

| TrainingData →<br>  TestData ↓ | Raw Data                                                                                                                | Processed Data                                                                                                          | Tokenized Data                                                                                                              |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Raw Data                       | Precision        : 0.6885<br> Recall           : 0.2258<br> F1 score         : 0.3401<br> Accuracy score   : 0.9642 | Precision        : 0.8497<br> Recall           : 0.2330<br> F1 score         : 0.3657<br> Accuracy score   : 0.9670 | Precision        : 0.8259<br> Recall           : 0.7993<br> F1 score         : 0.8124<br> Accuracy score   : 0.9849 |
| Processed Data                 | Precision        : 0.6885<br> Recall           : 0.2258<br> F1 score         : 0.3401<br> Accuracy score   : 0.9642 | Precision        : 0.8497<br> Recall           : 0.2330<br> F1 score         : 0.3657<br> Accuracy score   : 0.9670 | Precision        : 0.8259<br> Recall           : 0.7993<br> F1 score         : 0.8124<br> Accuracy score   : 0.9849 |
| Tokenized Data                 | Precision        : 0.6885<br> Recall           : 0.2258<br> F1 score         : 0.3401<br> Accuracy score   : 0.9642 | Precision        : 0.8497<br> Recall           : 0.2330<br> F1 score         : 0.3657<br> Accuracy score   : 0.9670 | Precision        : 0.8259<br> Recall           : 0.7993<br> F1 score         : 0.8124<br> Accuracy score   : 0.9849 |
