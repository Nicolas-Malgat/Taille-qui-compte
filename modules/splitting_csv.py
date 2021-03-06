import os
from os import path, makedirs
import csv

def print_nb_row(file_path):
    print(len(open(file_path).readlines()))

def __test_folder(folder):
    if path.exists(folder) == False:
        try:
            makedirs(folder)
        except OSError:
            print(f"Creation of the directory {folder} failed")
            exit(1)
        else:
            print(f"Successfully created the directory {folder}")

def split(filehandler, delimiter=',', row_limit=10000, 
    output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    """
    filehandler
    delimiter=','
    row_limit=10000 
    output_name_template='output_%s.csv' 
    output_path='.'
    keep_headers=True
    
    https://gist.github.com/jrivero/1085501

    Splits a CSV file into multiple pieces.
    
    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file. 10,000 by default.
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files.
        `keep_headers`: Whether or not to print the headers in each output file.
    Example usage:
    
        >> from toolbox import csv_splitter;
        >> csv_splitter.split(open('/home/ben/input.csv', 'r'));
    
    """
    __test_folder(output_path)
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
         output_path,
         output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            print("created " + (output_name_template % current_piece) )
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
               output_path,
               output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)

if __name__ == "__main__":
    # print_nb_row("../datas/RAW/brief-12/train.csv")
    # >> 35563652

    split(
        open("../datas/RAW/brief-12/train.csv", 'r'),
        delimiter=';',
        row_limit=500000,
        output_name_template='Taxi_train_%s.csv',
        output_path="../datas/RAW/"
    )