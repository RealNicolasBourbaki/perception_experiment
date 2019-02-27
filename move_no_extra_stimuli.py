import os, shutil

splice_add = '/home/nianheng/Documents/hiwi/02februar/fabian/splice/'
ori_add = '/home/nianheng/Documents/hiwi/02februar/fabian/ori/'
sti_add = '/home/nianheng/Documents/hiwi/02februar/fabian/stimuli/'
wav_list = os.listdir(splice_add)

for each in wav_list:
    word = each[:each.find('_')]
    stem = None
    if word.endswith('ed'):
        stem = word[:-2]
    elif word.endswith('s'):
        stem = word[:-1]

    shutil.copy(ori_add+word+'_original.wav', sti_add+word+'_original.wav')
    shutil.copy(splice_add + word + '_splice.wav', sti_add + word + 'splice.wav')
