import argparse
import data_loader
import data_preprocessing
import modeling
import evaluation

# 입력 데이터 파싱 메소드 
def parsing_argument():
    parser = argparse.ArgumentParser(
        # prog = '머신러닝 프로세스',
        description="데이터 로드, 전처리, 모델링 학습 및 평가",
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

    # (train) 데이터 파일경로
    # -> train-test-split 실행

    # test 데이터파일경로 (default=None)
    # -> None 일 경우, train-test-split 실행

    # train-test-split method (default: random / random or time)
    # test-size (default: 0.2)

    # 결과 저장 여부 (default = True)
    # 결과 저장 경로 설정 (default = './results_{날짜}')

    # test=None -> (train-test-split 여부)

    # scaling 여부 (default=True)
    # scaling method(default=Standard)

    # resampling 여부 (default=False)
    # resampling method(None일 경우 진행 X)


    # 입력 데이터 파싱 및 리턴
    args = parser.parse_args()
    return args

def main():
    args = parsing_argument()
    print(args)
    # print(f"Title : {args.title}")

    if args.test is None:
        data_preprocessing.train_test_split()

    return args

if __name__ == '__main__':
    main()