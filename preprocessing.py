import argparse

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE


# 2. 데이터 전처리(Preprocessing)
#     - train-test-split
#     - scaling
#     - resampling

