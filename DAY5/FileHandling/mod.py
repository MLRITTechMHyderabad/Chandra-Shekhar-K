import csv

with open("demo.csv",'r') as file:
    reader= csv.Reader(file)
    for i in reader:
        print(i)