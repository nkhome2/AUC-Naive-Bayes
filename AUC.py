#!/usr/bin/python3
import sys
import itertools
import copy

def get_input():
    # for index checking
    index_counter = 1
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
                sys.exit(x[0] + ' is not a valid index ' + index_counter)
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


def get_ROC_point(threshold):
    TP = 0
    TN = 0
    FN = 0
    FP = 0
    for p in pairs:
        # ignore those on the line of threshold
        if p[0] > threshold:
            if 'P' in p[1]:
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


def calculate_AUC():
    area = 0
    for i in range(len(ROC_points)-1):
        area += (ROC_points[i+1][0] - ROC_points[i][0]) * (ROC_points[i+1][1] + ROC_points[i][1]) / 2
    return area





# pairs have a format of (probability, actual_value)
pairs = get_input()
ROC_points = []

for pair in pairs:
    # try to set the threshold to that value
    threshold = pair[0]
    ROC_points.append(get_ROC_point(threshold))
ROC_points.sort()   # losing indexes at this step




AUC = calculate_AUC()
print("The AUC for the given data is " + str(AUC))
