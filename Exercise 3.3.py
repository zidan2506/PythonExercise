gender = input('Enter your gender: ')
hemoglobin = float(input('Enter your hemoglobin value : '))
if gender == 'male' and  hemoglobin < 134:
    print("Your hemoglobin value is low ")
elif hemoglobin > 167:
    print("Your hemoglobin value is high ")
elif gender == 'female' and hemoglobin < 117:
    print("Your hemoglobin value is low ")
elif hemoglobin > 155:
    print("Your hemoglobin value is high ")
elif gender == 'male' and 134 < hemoglobin < 167:
    print("Your hemoglobin value is normal ")
else:
    print('Your hemoglobin value is normal ')


