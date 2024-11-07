import time    
import utils

def LCS(x, y):
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)]
    b = [[0 for _ in range(n)] for _ in range(m)]
    
    # LCS 길이 및 방향 배열 채우기
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1  # 대각선 방향
            else:
                if c[i][j-1] > c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 2  # 왼쪽 방향
                else:
                    c[i][j] = c[i-1][j]
                    b[i][j] = 3  # 위쪽 방향

    # LCS 길이 저장
    lcs_length = c[m-1][n-1]

    # LCS 문자열 추출
    sa = []
    i, j = m - 1, n - 1
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 대각선으로 이동 (LCS에 포함되는 문자)
            sa.append(x[i])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 왼쪽으로 이동
            j -= 1
        else:  # 위쪽으로 이동
            i -= 1

    # 역순으로 쌓였으므로 뒤집어주기
    sa.reverse()

    return lcs_length, ''.join(sa)
    
def solution(test_case):
    # time check
    start_time = time.time()
    
    ##################### CODE HERE #####################  
    data = test_case.split()
    y, x = data[0], data[1]
    x, y = list(x), list(y)
    
    lcs_length, lcs = LCS(x, y)
    #####################################################

    # end time
    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.8f} seconds".format(elapsed_time))

    result = f"{lcs} {lcs_length}"

    return result

###################### DO NOT TOUCH BELOW ######################
if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description = 'Argument parser')
    parser.add_argument('--input', '-i', default = './input', help = 'Input file path')
    parser.add_argument('--output', '-o', default = './output', help = 'Output file path')
    args = parser.parse_args()

    utils.output_checker(args.output)    
    test_cases = utils.read_input(args.input)

    for test_case in test_cases:
        result = solution(test_case)
        utils.write_ouput(args.output, result)
    
    utils.compare_files(args.output)
    
