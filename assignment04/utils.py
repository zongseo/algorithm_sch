import os
import subprocess
import sys
# from natsort import natsorted

def install_natsort():
    try:
        import natsort
        # from natsort import natsorted
    except ImportError:
        print("natsort package is not installed. Install start....")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "natsort"])
        print("natsort package install completed successfully.")
        import natsort
        # from natsort import natsorted

def read_input(input_directory):
    install_natsort()
    from natsort import natsorted
    
    test_cases = []
    
    filenames = [f for f in os.listdir(input_directory) if f.endswith('.txt')]
    sorted_filenames = natsorted(filenames)

    for filename in sorted_filenames:
        file_path = os.path.join(input_directory, filename)
        with open(file_path, 'r') as file:
            inputs = file.read()
            test_cases.append(inputs)

    # print(test_cases)
    return test_cases

def output_checker(output_directory):
    output_file = os.path.join(output_directory, 'output.txt')
    if os.path.exists(output_file):
        os.remove(output_file)

def write_ouput(output_directory, contents):
    output_file = os.path.join(output_directory, 'output.txt')
    result = f'{contents}\n'
    with open(output_file, 'a') as file:
        file.write(result)
        
def compare_files(output_directory):
    output_file = os.path.join(output_directory, 'output.txt')
    answer_file = os.path.join(output_directory, 'answer.txt')

    with open(output_file, 'r') as f1, open(answer_file, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1.strip() != line2.strip():
                print("Failed")
                return 
            
        # Check if one file has more lines than the other
        if len(f1.readlines()) != len(f2.readlines()):
            print("Failed")
            return 
    
    print("Success!")