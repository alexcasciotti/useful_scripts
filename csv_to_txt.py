import csv


input_file_path = input("Enter csv file path: ")
export_file_path = input("Enter export file path: ")

with open(input_file_path) as csvfile:
    reader = csv.reader(csvfile)
    f = open(export_file_path, "w")
    for row in reader:
        f.write(f"{row}\n")
    f.close()
