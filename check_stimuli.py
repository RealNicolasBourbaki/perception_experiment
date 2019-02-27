import os

sti_add = '/home/nianheng/Documents/hiwi/01januar/fabian/' \
          'Tense_Identificantion_Test/recording_morphology_experiment/' \
          '00results/stimuli/'

wav_list = os.listdir(sti_add)

with_ed_original_single = []
with_s_original_single = []
with_only_original = []

for each_word in wav_list:
    cut_us = each_word.find('_')
    cut_dt = each_word.find('.')
    word_suf = each_word[:cut_us]
    word_fea = each_word[cut_us+1 : cut_dt]

    if word_suf.endswith('ed') and word_fea == 'original':
        word = word_suf[:-2]

        if word + 's_original.wav' not in wav_list:
            with_ed_original_single.append(word)

        elif (word+'ed_splice.wav' not in wav_list) or (word + 's_splice.wav' not in wav_list):
            with_only_original.append(word)

    if word_suf.endswith('s') and word_fea == 'original':
        word = word_suf[:-1]

        if word + 'ed_original.wav' not in wav_list:
            with_s_original_single.append(word)

        elif (word + 'ed_splice.wav' not in wav_list) or (word + 's_splice.wav' not in wav_list):
            with_only_original.append(word)

print('with_ed_original_single: ', with_ed_original_single)
print('with_s_original_single: ', with_s_original_single)
print('with_only_original', with_only_original)