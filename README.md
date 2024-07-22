# 머신러닝 파이프라인 (~ing)
(24.07 ~) 머신러닝 모델 파이프라인 프로그램입니다.


## 머신러닝 프로세스

> **결측치 및 이상치 처리, 범주형 변수 전처리 기능은 포함되어 있지 않습니다.**
즉, 입력 데이터에는 결측치가 존재하지 않으며, 범주형 변수는 숫자형으로 인코딩 되어 있어야 합니다.

> 데이터는 train.py, test.py 또는 data.py

1. 데이터셋 생성
    - 데이터 로드
    - 분할(train-test-split)
2. (Optional) 데이터 전처리
    - 스케일링
    - 리샘플링
3. 모델링(Modeling)
    - 분류모델
    - 회귀모델
4. 성능평가(Evaluation)
    - 분류모델 : Accuracy, Precision, Recall, F1-score
    - 회귀모델 : MAE, MSE, RMSE, R2_score

## 파일 목록 및 설명

1. 실행 파일
    - main.py
    - demo.ipynb

2. 클래스 파일
    - Dataset.py

3. 머신러닝 모듈
    - loader.py
    - preprocessing.py
    - modeling.py
    - evaluation.py

## Setup
```
git clone 
cd 
<!-- pip install requirements.txt -->
```

## Tutorial
```
python main.py --
```