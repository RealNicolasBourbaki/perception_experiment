import os, csv
from random import randint

add = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
      'recording_morphology_experiment/00results/old_stimuli_lists/'

sti_add = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
          'recording_morphology_experiment/00results/stimuli/'

sti_base_add = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
               'recording_morphology_experiment/00results/stimuli_base/'

new_list_add = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
               'recording_morphology_experiment/00results/stimuli_lists/'

audio_list = os.listdir(sti_add)
audio_set = set()

for each in audio_list:
    audio_set.add(each)

file_list = os.listdir(add)
count = 100


def fisher_yates_shuffle(the_list):
    list_range = range(0, len(the_list))
    for i in list_range:
        j = randint(list_range[0], list_range[-1])
        the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list


for each in file_list:
    with open(add+each, 'r')as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            if line[0][8:] in audio_set:
                with open(sti_base_add+each, mode='a') as w_f:
                    writer = csv.writer(w_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(line)

new_file_list = os.listdir(sti_base_add)

while count > 0:
    content = list()
    num = count % 4
    if num == 0:
        base = sti_base_add+'perception_stimuli_list_a.csv'
    elif num == 1:
        base = sti_base_add + 'perception_stimuli_list_b.csv'
    elif num == 2:
        base = sti_base_add + 'perception_stimuli_list_c.csv'
    elif num == 3:
        base = sti_base_add + 'perception_stimuli_list_d.csv'

    with open(base, 'r')as base_f:
        reader = csv.reader(base_f, delimiter=',')
        for line in reader:
            content.append(line)
    print(content)
    new_lines = fisher_yates_shuffle(content)

    with open(new_list_add+'perception_stimuli_list_'+str(count)+'.csv', 'a') as new_f:
        writer = csv.writer(new_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for each_line in new_lines:
            writer.writerow(each_line)
    count -= 1
