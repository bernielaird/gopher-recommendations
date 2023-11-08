import csv

def classList():
    with open('SPR2023_raw_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        classes = []
        line_count = 0
        for row in csv_reader:
            if([row[4], row[5]] not in classes):
               classes.append([row[4], row[5]])
            line_count+=1
        classes.pop(0)
    return classes



















































































        

#writeToFile([1, 1, 0, 10, 8, 8, 8, 4, 8, 8, 0, 8, 9, 9, 8, 6, 8, 4, 10, 6])