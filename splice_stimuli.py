from pydub import AudioSegment
import textgrid
import os

add = '/home/nianheng/Documents/hiwi/01januar/fabian/' \
      'Tense_Identificantion_Test/recording_morphology_experiment/' \
      '00results/recordings_with_textgrids/'
out = '/home/nianheng/Documents/hiwi/02februar/fabian/'

file_textgrid = list()
wav_file = list()

for each in os.listdir(add):
    if each.endswith('.TextGrid'):
        file_textgrid.append(each)
    if each.endswith('mono.wav'):
        wav_file.append(each)


def read_textgrid(filename):
    file_textgrid_obj = textgrid.TextGrid.fromFile(add + filename)
    tier_list = file_textgrid_obj.tiers
    intervals_morpheme = list()

    for each_tier in tier_list:
        if each_tier.name == 'morpheme':
            tier_segments = each_tier
            intervals_morpheme = tier_segments.intervals

    for i, each in enumerate(intervals_morpheme):
        if each.mark.strip() == 'ed':
            ori_interv = intervals_morpheme[i-1]
            start_stem = ori_interv.minTime * 1000
            end_stem = ori_interv.maxTime * 1000
            start_ed = each.minTime * 1000
            end_ed = each.maxTime * 1000
            mark = ori_interv.mark
            cut_stem_ed(filename[:-9], start_stem, end_stem, mark)
            cut_ed(filename[:-9], start_ed, end_ed, mark)

        if each.mark.strip() == 's':
            ori_interv = intervals_morpheme[i-1]
            start_stem = ori_interv.minTime * 1000
            end_stem = ori_interv.maxTime * 1000
            start_s = each.minTime * 1000
            end_s = each.maxTime * 1000
            mark = ori_interv.mark
            cut_stem_s(filename[:-9], start_stem, end_stem, mark)
            cut_s(filename[:-9], start_s, end_s, mark)


def cut_s(filename, start_time, end_time, mark):
    this_whole_wav = AudioSegment.from_wav(add + filename + ".wav")
    this_wav = this_whole_wav[int(start_time): int(end_time)]
    this_wav.export(out + 's/' + mark + ".wav", format="wav")


def cut_ed(filename, start_time, end_time, mark):
    this_whole_wav = AudioSegment.from_wav(add + filename + ".wav")
    this_wav = this_whole_wav[int(start_time): int(end_time)]
    this_wav.export(out + 'ed/' + mark + ".wav", format="wav")


def cut_stem_ed(filename, start_time, end_time, mark):
    this_whole_wav = AudioSegment.from_wav(add + filename + ".wav")
    this_wav = this_whole_wav[int(start_time): int(end_time)]
    this_wav.export(out + 'ori_stem_ed/' + mark + ".wav", format="wav")


def cut_stem_s(filename, start_time, end_time, mark):
    this_whole_wav = AudioSegment.from_wav(add + filename + ".wav")
    this_wav = this_whole_wav[int(start_time): int(end_time)]
    this_wav.export(out + 'ori_stem_s/' + mark + ".wav", format="wav")


for each in file_textgrid:
    read_textgrid(each)
