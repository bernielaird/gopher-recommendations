import numpy as np
import csv
import csvWriter

c = [2, 5, 1, 1]
g = [['MATH', '1271', 'Corsi,Craig M'], ['MATH', '1272', 'Willis,Cole Scott'], ['AAS', '3251W', 'Logan,Enid']]

def getUserVector(userMatrix, bigData):
    rows = np.shape(userMatrix)[0]
    vector = np.empty((1,np.shape(userMatrix)[1]))
    vector.fill(0)
    for i in range(rows):
        vector = vector + userMatrix[i]  
    vector = np.transpose(np.matmul(bigData, np.transpose(vector/rows)))
    return vector

def getWeight(answerScores):
    with open('numbers.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        numbers = np.empty((24,4))
        line_count = 0
        for row in csv_reader:
            numbers[line_count] = row
            line_count += 1
    return (np.matmul(numbers, np.transpose(np.multiply(answerScores,1))))

def getBigMatrix():
    with open('SPR2023_raw_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        bigMatrix = np.empty((29618,24))
        bigMatrix.fill(0)
        next(csv_reader)
        line_count = 0
        for row in csv_reader:
            if (row[19] == '' or row[19] == '-1'):
                row[19] = '50'
            if (row[17] != ''):
                    bigMatrix[line_count] = [float(row[17])/5,float(row[18])/5,float(row[19])/100,float(row[21]),float(row[22]),float(row[23]),float(row[24]),float(row[25]),float(row[26]),float(row[27]),float(row[28]),float(row[29]),float(row[30]),float(row[31]),float(row[32]),float(row[33]),float(row[34]),float(row[35]),float(row[36]),float(row[37]),float(row[38]),float(row[39]),float(row[40]),float(row[41])]
            if (row[17] == ''):
                bigMatrix[line_count] = [0.5,0.5,0.5,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
            line_count += 1
        return bigMatrix
    
def biasAlgorithm(answerScores):
    return(np.multiply(np.matmul(getBigMatrix(),getWeight(answerScores)), 1/(np.max(np.matmul(getBigMatrix(),getWeight(answerScores))))))

def takenAlgorithm(taken):
    return(np.multiply(getUserVector(taken,getBigMatrix()),1/np.max(getUserVector(taken,getBigMatrix()))))

def theAlgorithm(answerScores, taken, biasBias, takenBias):
    bigMatrix = getBigMatrix()
    weight = getWeight(answerScores)
    userVector = getUserVector(taken, bigMatrix)
    biasScores = np.matmul(bigMatrix, weight)
    normTaken = np.multiply(userVector, takenBias/np.max(userVector))
    normBias = np.multiply(biasScores, biasBias/np.max(biasScores))
    return np.multiply(np.add(normTaken,normBias), 1/(takenBias + biasBias))

def getUserMatrixProf(takenCodes):
    with open('SPR2023_raw_data.csv', mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in range(len(takenCodes)):
            if takenCodes[len(takenCodes) - 1 - i][2] == 'NA':
                takenCodes.pop(len(takenCodes) - 1 - i)
        userMatrix = np.empty((len(takenCodes), 24))
        userMatrix.fill(0)
        for i in range(len(takenCodes)):
            for row in csv_reader:
                if ((row[4] == takenCodes[i][0]) and (row[5] == takenCodes[i][1]) and (row[13] == takenCodes[i][2])):
                    userMatrix[i] = [float(row[17])/5,float(row[18])/5,float(row[19])/100,float(row[21]),float(row[22]),float(row[23]),float(row[24]),float(row[25]),float(row[26]),float(row[27]),float(row[28]),float(row[29]),float(row[30]),float(row[31]),float(row[32]),float(row[33]),float(row[34]),float(row[35]),float(row[36]),float(row[37]),float(row[38]),float(row[39]),float(row[40]),float(row[41])]
            csv_file.seek(0)
    return userMatrix


def getLargeMatrix():
    #UNTESTED
    with open('.csv', mode ='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        largeMatrix = np.empty((len(csvWriter.ClassList()), 20))
        largeMatrix.fill(0)
        line_count = 0
        for row in csv_reader:
            largeMatrix[line_count] = row
            line_count += 1
    return largeMatrix

print(np.argsort(theAlgorithm(c,getUserMatrixProf(g),1,1)))
