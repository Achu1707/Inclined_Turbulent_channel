import os
import datetime

def main():
    start_time = datetime.datetime.now()
    
    # Read input files and prepare dat_files_list.txt for parameters_module
    with open("input_files.txt", 'r') as f:
        input_files = f.readlines()
    
    # Write input files to dat_files_list.txt (required by parameters_module)
    with open("dat_files_list.txt", 'w') as f:
        for line in input_files:
            f.write(line.strip() + '\n')  # Format for parameters_module
    
    # Trigger parameters_module calculations
    import parameters_module_1
    
    print(f"Execution time: {datetime.datetime.now() - start_time}")

if __name__ == "__main__":
    main()
