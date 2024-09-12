import time    
import utils

def solution(test_case):
    start_time = time.time()
    
    ##################### CODE HERE #####################
    # Check! 
    # print(test_case)
    lines = test_case.strip().split('\n')
    rows, cols = map(int, lines[0].split(' '))
    matrix = lines[1:]

    gen_row = []
    gen_col = []

    for row in matrix:   # test case의 행과 해당 행의 문자열 반환
        gen_row.append([1] if 'O' in row else[])  # 행의 문자열 속 O존재 여부 확인
    
    for i in range(cols):
        gen_col.append([1] if any('O' in row[i] for row in matrix) else [])

        #  비어있는 공간은 false로 반환되기에 not r을 통해 True로 반환하여 빈 공간 개수 찾기
    empty_rows = sum(1 for r in gen_row if not r)
    empty_cols = sum(1 for c in gen_col if not c)

    result = max(empty_rows, empty_cols)
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

    utils.output_checker(args.output)    
    test_cases = utils.read_input(args.input)

    for test_case in test_cases:
        result = solution(test_case) # solution function call here.
        utils.write_ouput(args.output, result)
    
    utils.compare_files(args.output)  
