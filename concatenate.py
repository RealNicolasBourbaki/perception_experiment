from pydub import AudioSegment
import os

root = '/home/nianheng/Documents/hiwi/02februar/fabian/'

fricatives = ['s', 'z', 'f', 'v', 'h']

ori_stem_ed = os.listdir(root+'ori_stem_ed/')
ori_stem_s = os.listdir(root+'ori_stem_s/')
ed = os.listdir(root+'ed/')
s = os.listdir(root+'s/')
silent_segment = AudioSegment.silent(duration=150)

for each in ori_stem_ed:
    the_audio = AudioSegment.from_wav(root + 'ori_stem_ed/' + each)
    each = each[:-4]
    if each[:1] in fricatives:
        stem_faded = the_audio.fade_in(10)
    elif each[:1] not in fricatives:
        stem_faded = the_audio.fade_in(5)

    if each[:-1] in fricatives:
        stem_faded = the_audio.fade_out(10)
    elif each[:-1] not in fricatives:
        stem_faded = the_audio.fade_out(5)

    suf_audio = AudioSegment.from_wav(root + 'ed/' + each + '.wav')

    if each[:-1] in fricatives:
        suf_audio = suf_audio.fade_in(10)
    elif each[:-1] not in fricatives:
        suf_audio = suf_audio.fade_in(5)

    final = the_audio + suf_audio + silent_segment
    final.export(root + 'ori/' + each + "ed_original.wav", format="wav")


for each in ori_stem_s:
    the_audio = AudioSegment.from_wav(root + 'ori_stem_s/' + each)
    each = each[:-4]
    if each[:1] in fricatives:
        stem_faded = the_audio.fade_in(10)
    elif each[:1] not in fricatives:
        stem_faded = the_audio.fade_in(5)

    if each[:-1] in fricatives:
        stem_faded = the_audio.fade_out(10)
    elif each[:-1] not in fricatives:
        stem_faded = the_audio.fade_out(5)

    suf_audio = AudioSegment.from_wav(root + 's/' + each + '.wav')

    if each[:-1] in fricatives:
        suf_audio = suf_audio.fade_in(10)
    elif each[:-1] not in fricatives:
        suf_audio = suf_audio.fade_in(5)

    final = the_audio + suf_audio + silent_segment
    final.export(root + 'ori/' + each + "s_original.wav", format="wav")
