import csv
def makeBetterCSV():
    with open('SPR2023_raw_data.csv', mode ='r') as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter = ',')
        with open('SPR2023_beter_data.csv', mode = 'w', newline='') as csv_file2:
            csv_writer = csv.writer(csv_file2, delimiter = ',')
            classes = []
            next(csv_reader)
            for row in csv_reader:
                if ([row[4], row[5], row[13]] not in classes):
                    classes.append([row[4], row[5], row[13]])
                    csv_writer.writerow([row[4],row[5],row[13],row[17],row[18],row[19],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41]])

makeBetterCSV()
