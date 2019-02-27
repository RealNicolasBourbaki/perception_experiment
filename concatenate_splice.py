from pydub import AudioSegment
import os

root = '/home/nianheng/Documents/hiwi/02februar/fabian/'

fricatives = ['s', 'z', 'f', 'v', 'h', 'k']

ori_stem_ed = os.listdir(root+'ori_stem_ed/')
ori_stem_s = os.listdir(root+'ori_stem_s/')
ed = os.listdir(root+'ed/')
s = os.listdir(root+'s/')
ori = os.listdir(root + 'ori/')
silent_segment = AudioSegment.silent(duration=150)

for each in ori:

    both_exit = False
    if each[:each.find('_')].endswith('ed'):
        stem = each[:each.find('_')-2]
        if stem+'s_original.wav' in ori:
            both_exit = True
        else:
            both_exit = False

    elif each[:each.find('_')].endswith('s'):
        stem = each[:each.find('_')-1]
        if stem+'ed_original.wav' in ori:
            both_exit = True
        else:
            both_exit = False

    if both_exit:
        stem_ed_audio = AudioSegment.from_wav(root + 'ori_stem_ed/' + stem + ".wav")
        stem_s_audio = AudioSegment.from_wav(root + 'ori_stem_s/' + stem + ".wav")
        ed_audio = AudioSegment.from_wav(root + 'ed/' + stem + '.wav')
        s_audio = AudioSegment.from_wav(root + 's/' + stem + '.wav')

        if stem[:1] in fricatives:
            stem_ed_faded = stem_ed_audio.fade_in(10)
            stem_s_faded = stem_s_audio.fade_in(10)
        elif each[:1] not in fricatives:
            stem_ed_faded = stem_ed_audio.fade_in(5)
            stem_s_faded = stem_s_audio.fade_in(5)

        if each[:-1] in fricatives:
            ed_faded = ed_audio.fade_out(10)
            s_faded = s_audio.fade_out(10)
        elif each[:-1] not in fricatives:
            ed_faded = ed_audio.fade_out(5)
            s_faded = s_audio.fade_out(5)

        splice_ed = stem_s_audio + ed_audio + silent_segment
        splice_s = stem_ed_audio + s_audio + silent_segment
        splice_ed.export(root + 'splice/' + stem + "ed_splice.wav", format="wav")
        splice_s.export(root + 'splice/' + stem + 's_splice.wav', format='wav')


