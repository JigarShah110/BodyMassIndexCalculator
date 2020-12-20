#!/usr/bin/python3
import os
import json
import time

def calculate_bmi(height, weight):
    # This method will calculate BMI and perform rounding off to two digits
    return format((int(weight) / ((int(height)/100) ** 2)), '.2f')

def process_patient_file(file_path):
    # This method is created for processing the json data file and will create an result file and also calculate overweighted patients.
    data_file = open(file_path, "r")
    data = json.loads(data_file.read())
    data_list = []
    overweight_patients = 0
    for dicts in data:
        patient_bmi = float(calculate_bmi(dicts['HeightCm'], dicts['WeightKg']))  # calling calculator_bmi method for getting bmi value
        if(patient_bmi <= 18.4):
            dicts["BMI Category"] = "Underweight"
            dicts["BMI Range"] = "18.4 and below"
            dicts["Health risk"] = "Malnutrition risk"
        elif(patient_bmi >= 18.5 and patient_bmi <= 24.9):
            dicts["BMI Category"] = "Normal weight"
            dicts["BMI Range"] = "18.5 - 24.9"
            dicts["Health risk"] = "Low risk"
        elif(patient_bmi >= 25 and patient_bmi <= 29.9):
            dicts["BMI Category"] = "Overweight"
            dicts["BMI Range"] = "25 - 29.9"
            dicts["Health risk"] = "Enhanced risk"
            overweight_patients += 1
        elif(patient_bmi >= 30 and patient_bmi <= 34.9):
            dicts["BMI Category"] = "Moderately obese"
            dicts["BMI Range"] = "30 - 34.9"
            dicts["Health risk"] = "Medium risk"
        elif(patient_bmi >= 35 and patient_bmi <= 39.9):
            dicts["BMI Category"] = "Severely obese"
            dicts["BMI Range"] = "35 - 39.9"
            dicts["Health risk"] = "High risk"
        else:
            dicts["BMI Category"] = "Very severely obese"
            dicts["BMI Range"] = "40 and above"
            dicts["Health risk"] = "Very high risk"
        data_list.append(dicts)
    file_name = "ResultBMI_" + str(time.time()) + ".json" # Randomly generated result filename on basis of timestamp
    with open(file_name, 'w') as json_file:
        json.dump(data_list, json_file)  # Writing to result file
    return file_name, overweight_patients

def validate_patient_file(file_path):
    # This method will validate the json data file exists or not
    if os.path.isfile(file_path):
        return True
    else:
        return False

patient_file = input("Enter FilePath: ")
if(validate_patient_file(patient_file)):
    output_file, overweight_patients = process_patient_file(patient_file)
    print("Total number of Overweight patients are: %d" % overweight_patients)
    print("Please check result file : %s" % output_file)
else:
    print("File does not exists!!")