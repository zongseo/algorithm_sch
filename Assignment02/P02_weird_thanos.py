import time    
import utils

##################### CODE HERE FOR USER-DEFINED FUNCTION #####################   
def insertion_sort(n, arr):
    # 인덱스 0은 이미 정렬된 것으로 간주
    for i in range(1, n):
        key = arr[i]  # 현재 삽입될 숫자인 i번째 요소를 key로 설정
        
        # 현재 정렬된 배열은 i-1까지이므로 i-1부터 역순으로 조사
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 요소를 오른쪽으로 이동
            j -= 1
        
        arr[j + 1] = key  # key 값을 알맞은 위치에 삽입

###############################################################################

def solution(test_case):        
    
    start_time = time.time()
    
    ##################### CODE HERE #####################    

    numbers = [int(char) for char in test_case.strip()]
    length = len(numbers)
    insertion_sort(length, numbers)
    
    half_length = length // 2

    # 절반 만큼 삭제 (앞에서부터)
    result = numbers[half_length:]
    result = ''.join(map(str, result))


    #####################################################

    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.8f} seconds".format(elapsed_time))

    return result


###################### DO NOT TOUCH BELOW ######################
if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description = 'Argument parser')
    parser.add_argument('--input', '-i', default = './input', help = 'Input file path')
    parser.add_argument('--output', '-o', default = './output', help = 'Output file path')
    args = parser.parse_args()

    INPUT_PATH = args.input
    OUTPUT_PATH = args.output

    utils.output_checker(args.output)    
    test_cases = utils.read_input(args.input)

    for test_case in test_cases:
        result = solution(test_case)
        utils.write_ouput(OUTPUT_PATH, result)
    
    utils.compare_files(OUTPUT_PATH)
    
