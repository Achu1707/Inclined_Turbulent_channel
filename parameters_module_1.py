import os
import math
import csv
import xlwt
from xlrd import open_workbook
import logging

def precision(value, p=5):
    return round(value, p)

def rename(fname):
    fname = fname.split(" ")
    return "_".join(fname)

# Get input file
os.system('dir /b *Filtered_by_ALL*.dat > dat_files_list.txt')

with open("dat_files_list.txt", "rt", encoding="utf8") as f:
    for dat_filename_read in f:
        dat_filename_read = dat_filename_read.strip()
        dat_filename_read = rename(dat_filename_read)
        print("Processing file: %s" % dat_filename_read)
        
        try:
            # Convert DAT to XLS
            with open(dat_filename_read, 'rt') as f_in:
                reader = csv.reader(f_in, delimiter=",")
                wbk = xlwt.Workbook()
                sheet = wbk.add_sheet("Sheet 1")

                for rowi, row in enumerate(reader):
                    for coli, value in enumerate(row):
                        try:
                            sheet.write(rowi, coli, float(value))
                        except:
                            sheet.write(rowi, coli, value)

                wbk.save(dat_filename_read + '.xls')
                print("Conversion to %s.xls done" % dat_filename_read)

            # Process the XLS file
            book = open_workbook(dat_filename_read + '.xls')
            first_sheet = book.sheet_by_index(0)
            total_rows = first_sheet.nrows - 3
            
            # Initialize variables
            inst_velocity_U = 0
            inst_velocity_V = 0
            inst_velocity_W = 0
            
            U_prime_sum_of_square = 0
            V_prime_sum_of_square = 0
            W_prime_sum_of_square = 0

            # First pass: calculate mean velocities
            for i in range(3, first_sheet.nrows):
                row = first_sheet.row_slice(i)
                inst_velocity_U += row[1].value
                inst_velocity_V += row[2].value
                inst_velocity_W += row[3].value

            average_velocity_U = inst_velocity_U / total_rows
            average_velocity_V = inst_velocity_V / total_rows
            average_velocity_W = inst_velocity_W / total_rows

            # Second pass: calculate variances
            for i in range(3, first_sheet.nrows):
                row = first_sheet.row_slice(i)
                
                U_prime = row[1].value - average_velocity_U
                U_prime_sum_of_square += U_prime * U_prime
                
                V_prime = row[2].value - average_velocity_V
                V_prime_sum_of_square += V_prime * V_prime
                
                W_prime = row[3].value - average_velocity_W
                W_prime_sum_of_square += W_prime * W_prime

            U_variance = U_prime_sum_of_square / total_rows
            V_variance = V_prime_sum_of_square / total_rows
            W_variance = W_prime_sum_of_square / total_rows

            U_stdev = math.sqrt(U_variance)
            V_stdev = math.sqrt(V_variance)
            W_stdev = math.sqrt(W_variance)

            # Print results
            print("\nResults for file: %s" % dat_filename_read)
            print("Mean U velocity: %0.10f" % average_velocity_U)
            print("Mean V velocity: %0.10f" % average_velocity_V)
            print("Mean W velocity: %0.10f" % average_velocity_W)
            print("U variance: %0.10f" % U_variance)
            print("V variance: %0.10f" % V_variance)
            print("W variance: %0.10f" % W_variance)
            print("U standard deviation: %0.10f" % U_stdev)
            print("V standard deviation: %0.10f" % V_stdev)
            print("W standard deviation: %0.10f" % W_stdev)
            print("----------------------------------------")

            # Write results to CSV
            with open("Velocity_Statistics.csv", "a") as fo:
                fo.write("\n" + dat_filename_read + ","
                         + str(precision(average_velocity_U)) + ","
                         + str(precision(average_velocity_V)) + ","
                         + str(precision(average_velocity_W)) + ","
                         + str(precision(U_variance)) + ","
                         + str(precision(V_variance)) + ","
                         + str(precision(W_variance)) + ","
                         + str(precision(U_stdev)) + ","
                         + str(precision(V_stdev)) + ","
                         + str(precision(W_stdev)))
            
        except Exception as e:
            current = os.getcwd()
            dstDir = os.getcwd() + "\Logs"
            os.chdir(dstDir)
            logger = logging.getLogger(dat_filename_read)
            logger.setLevel(logging.INFO)
            fh = logging.FileHandler(dat_filename_read + ".txt")
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            logger.exception(e)
            fh.close()
            os.chdir(current)

print("\nProcessing complete. Results saved to Velocity_Statistics.csv")

