#!/usr/bin/python3
import sys

# read the input from files
def get_input():
    index_counter = 1       # for index checking
    probabilities = []
    pairs = []
    with open("AUC1.txt", 'r') as file:
        lines = file.readlines()
        for l in lines:
            x = l.split(',')
            # if not a valid format string
            if len(x) < 2:
                break
            # if index is wrong
            if int(x[0]) != index_counter:
                sys.exit(str(x[0]) + ' is not a valid index. should be ' + str(index_counter))
            probabilities.append(float(x[1].strip(' ,\n')))
            index_counter += 1
    index_counter = 1
    with open("AUC2.txt", 'r') as file:
        lines = file.readlines()
        for l in lines:
            x = l.split(',')
            # if not a valid format string
            if len(x) < 2:
                break
            # if index is wrong
            if int(x[0]) != index_counter:
                sys.exit(x[0] + ' is not a valid index ' + index_counter)
            ground_value = (x[1].strip(' ,.\n'))
            pair = (probabilities[index_counter-1], ground_value)
            pairs.append(pair)
            index_counter += 1
    return pairs


# returns the (FPR, TPR) point based on the input data and the threshold
def get_ROC_point(threshold):
    TP = 0
    TN = 0
    FN = 0
    FP = 0
    for p in pairs:
        # ignore those on the line of threshold
        # if the value is greater than the threshold
        if p[0] >= threshold:
            # and the actual value is P
            if 'P' in p[1]:
                # this is a True Positive
                TP += 1
            elif 'N' in p[1]:
                FP += 1
        elif p[0] < threshold:
            if 'P' in p[1]:
                FN += 1
            elif 'N' in p[1]:
                TN += 1
    TPR = float(TP/(TP+FN))
    FPR = float(FP/(FP+TN))
    point = (FPR, TPR)  # x, y axis
    return point


# returns the area given the points
def calculate_AUC():
    area = 0
    for i in range(len(ROC_points)-1):
        area += (ROC_points[i+1][0] - ROC_points[i][0]) * (ROC_points[i+1][1] + ROC_points[i][1]) / 2
    return area


# store data in a list of pairs (0.33, 'N')
pairs = get_input()
# the points at the ROC curve
ROC_points = []

for pair in pairs:
    # set the threshold to that probability value
    threshold = pair[0]
    ROC_points.append(get_ROC_point(threshold))
ROC_points.sort()   # losing indexes at this step

AUC = calculate_AUC()
print("The AUC for the given data is " + str(AUC))
