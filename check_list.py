import os, csv

add = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
      'recording_morphology_experiment/00results/stimuli_base/'

file_list = os.listdir(add)
a_set = set()

for each in file_list:
    with open(add+each, 'r')as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            name = line[0][8:]
            if name in a_set:
                print(each)
                print(line)
                print(' ')
            else:
                a_set.add(name)
