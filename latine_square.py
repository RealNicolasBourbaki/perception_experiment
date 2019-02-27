import os
import csv
from random import randint

root = '/home/nianheng/Documents/hiwi/02februar/fabian/'
out_without =  '/home/nianheng/Documents/hiwi/02februar/fabian/stimuli_lists_without_extra/'
out_with = '/home/nianheng/Documents/hiwi/02februar/fabian/stimuli_lists_with_extra/'
ori = os.listdir(root + 'ori/')
spl = os.listdir(root + 'splice/')


def fisher_yates_shuffle(the_list):
    list_range = range(0, len(the_list))
    for i in list_range:
        j = randint(list_range[0], list_range[-1])
        the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list


def without_extra():

    splice_stem = set()

    for each in spl:
        word = each[:each.find('_')]
        if word.endswith('s'):
            splice_stem.add(word[:-1])
        if word.endswith('ed'):
            splice_stem.add(word[:-2])

    for each in splice_stem:

        latine_square = [(each+'s_splice.wav', 'present'), (each+'ed_splice.wav', 'past'),
                         (each+'s_original.wav', 'present'), (each+'ed_original.wav', 'past')]
        latine_square = fisher_yates_shuffle(latine_square)

        with open(out_without+'perception_stimuli_list_1.csv', 'a+')as out:
            writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['stimuli/'+latine_square[0][0], latine_square[0][1]])

        with open(out_without+'perception_stimuli_list_2.csv', 'a+')as out:
            writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['stimuli/'+latine_square[1][0], latine_square[1][1]])

        with open(out_without+'perception_stimuli_list_3.csv', 'a+')as out:
            writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['stimuli/'+latine_square[2][0], latine_square[2][1]])

        with open(out_without+'perception_stimuli_list_4.csv', 'a+')as out:
            writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['stimuli/'+latine_square[3][0], latine_square[3][1]])


def with_extra():

    splice_stem = set()
    ori_stem = set()
    extra = set()
    for each in spl:
        word = each[:each.find('_')]
        if word.endswith('s'):
            splice_stem.add(word[:-1])
        if word.endswith('ed'):
            splice_stem.add(word[:-2])

    for each in ori:
        word = each[:each.find('_')]
        if word.endswith('s'):
            ori_stem.add(word[:-1])
        if word.endswith('ed'):
            ori_stem.add(word[:-2])

    for each in ori_stem:

        if each in splice_stem:

            latine_square = [(each+'s_splice.wav', 'present'), (each+'ed_splice.wav', 'past'),
                         (each+'s_original.wav', 'present'), (each+'ed_original.wav', 'past')]
            latine_square = fisher_yates_shuffle(latine_square)

            with open(out_with+'perception_stimuli_list_1.csv', 'a+')as out:
                writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['stimuli/'+latine_square[0][0], latine_square[0][1]])

            with open(out_with+'perception_stimuli_list_2.csv', 'a+')as out:
                writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['stimuli/'+latine_square[1][0], latine_square[1][1]])

            with open(out_with+'perception_stimuli_list_3.csv', 'a+')as out:
                writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['stimuli/'+latine_square[2][0], latine_square[2][1]])

            with open(out_with+'perception_stimuli_list_4.csv', 'a+')as out:
                writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['stimuli/'+latine_square[3][0], latine_square[3][1]])

        else:

            for every in ori:
                if every.startswith(each+'s_'):
                    if every in extra:
                        print('error ', every)
                    extra.add(every)
                elif every.startswith(each+'ed_'):
                    if every in extra:
                        print('error ', every)
                    extra.add(every)

    count = 1

    for each in extra:
        print(each)
        if count != 5:
            with open(out_with + 'perception_stimuli_list_'+str(count)+'.csv', 'a+')as out:
                writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if each[each.find('_')-1:] == 's_original.wav':
                    writer.writerow(['stimuli/'+each, 'present'])
                if each[each.find('_')-1:] == 'ed_original.wav':
                    writer.writerow(['stimuli/'+each, 'past'])
            count += 1

        else:
            count = 1


without_extra()
with_extra()
