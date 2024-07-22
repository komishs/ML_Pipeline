import os
import pandas as pd
import argparse

from sklearn.model_selection import train_test_split

from Dataset import Dataset

def load_csv(fpath):
    return pd.read_csv(fpath)

def load_excel(fpath):
    return pd.read_csv(fpath)

def load(fpath):
    ext = fpath.split('.')[-1]

    if not os.path.exists(fpath):
        raise Exception('파일이 존재하지 않습니다.')  
        
    if ext=='csv':
        return load_csv(fpath)
    elif ext in ['xls', 'xlsx']:
        return load_excel(fpath)
    else:
        raise Exception('파일 확장자가 잘못되었습니다. [가능한 확장자: .csv, .xls, .xlsx]')

def main(args):

    data = load(args.file)
    if args.test is None:
        X = data.drop(columns = args.label)
        y = data[args.label]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y
        )
    else:
        X_train = data.drop(columns = args.label)
        y_train = data[args.label]

        test = load(args.test)
        X_test = test.drop(columns = args.label)
        y_test = test[args.label]

    dataset = Dataset(
        X_train, X_test, y_train, y_test, 
    )

    return dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="데이터 로드 및 데이터셋 생성",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # 파일경로
    parser.add_argument(
        '-f', '--file', help='(학습) 데이터 파일 경로', required=True
    )
    parser.add_argument(
        '-t', '--test', help='테스트 파일 경로', default=None
    )

    # 분류 모델 - 레이블 컬럼명
    parser.add_argument(
        '-l', '--label', help='레이블명', default='label'
    )

    # 클래스 객체 저장 여부
    parser.add_argument(
        '-s', '--save', help='데이터셋 저장 여부', default=False
    )

    # 클래스 객체 저장 경로
    parser.add_argument(
        '-r', '--result', help='데이터셋 저장 경로', default='result/'
    )

    args = parser.parse_args()

    main(args)