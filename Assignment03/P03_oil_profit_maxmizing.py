import time    
import utils

##################### CODE HERE FOR USER-DEFINED FUNCTION #####################   
def max_crossing_subarray(prices_diff, low, mid, high):
    # 왼쪽 배열과 오른쪽 배열을 중간을 기준으로 연속합의 최대 지점 구하기
    left_sum = float('-inf')
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += prices_diff[i]
        if total > left_sum:
            left_sum = total
            max_left = i
    
    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += prices_diff[j]
        if total > right_sum:
            right_sum = total
            max_right = j
    
    return max_left, max_right, left_sum + right_sum

def max_subarray(prices_diff, low, high):
    # 최소 단위(원소 1개)까지 쪼개지면 본인 인덱스, 인덱스에 해당하는 값(가격차이) 반환
    if low == high:
        return low, high, prices_diff[low]
    
    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray(prices_diff, low, mid)
    right_low, right_high, right_sum = max_subarray(prices_diff, mid + 1, high)
    cross_low, cross_high, cross_sum = max_crossing_subarray(prices_diff, low, mid, high)
    
    # 왼쪽 배열, 오른쪽 배열, 크로스 배열 우선순위
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def find_max_profit(prices):
    n = len(prices)
    if n < 2:
        return 0  # 가격이 하루치 밖에 없으면 0 반환

    # 1일 간격으로 가격 변화 배열 생성
    prices_diff = [prices[i] - prices[i - 1] for i in range(1, n)]
    
    # 최대 이익을 갖는 날짜 인덱스와 이익 서칭
    buy_day, sell_day, max_profit = max_subarray(prices_diff, 0, len(prices_diff) - 1)
    
    # 1일 간격 가격차이로 최대 이익을 구했기 때문에 반환받은 인덱스를 날짜 개념으로 +1, +2
    buy_day += 1
    sell_day += 2
    
    return buy_day + sell_day + max_profit

###############################################################################


def solution(test_case):  
    
    start_time = time.time()
    
    ##################### CODE HERE #####################    
    
    prices = list(map(int, test_case.split()))
    
    result = find_max_profit(prices)
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
    
