import csv

with open('numbers.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([1,0,1,0.7])
        csv_writer.writerow([1,3,-0.5,-0.5])
        csv_writer.writerow([1,0,1,1])
        csv_writer.writerow([0.9,0.1,0,0])
        csv_writer.writerow([0.9,0,0.7,0.3])
        csv_writer.writerow([0.9,0.5,-0.6,-0.2])
        csv_writer.writerow([1,0.5,-0.2,0.5])
        csv_writer.writerow([1,0.5,-0.3,-0.2])
        csv_writer.writerow([0.5,0.9,-0.3,-0.2])
        csv_writer.writerow([0.5,1,-0.3,0])
        csv_writer.writerow([0.5,0.9,-0.3,0])
        csv_writer.writerow([0.7,1,0,0])
        csv_writer.writerow([0,0.5,-0.8,-0.3])
        csv_writer.writerow([0,0.5,0,0])
        csv_writer.writerow([0.5,0,1,0.5])
        csv_writer.writerow([0.5,0,1,0.5])
        csv_writer.writerow([0.5,0,1,0.5])
        csv_writer.writerow([0.5,-0.2,1,0.5])
        csv_writer.writerow([-0.7,-0.1,0.5,1])
        csv_writer.writerow([-0.3,0,0.5,1])
        csv_writer.writerow([0,0.2,0.5,0.9])
        csv_writer.writerow([0.3,0.2,0.5,0.9])
        csv_writer.writerow([-0.5,-0.5,0.5,0.9])
        csv_writer.writerow([0.5,-0.8,0.2,0.5])