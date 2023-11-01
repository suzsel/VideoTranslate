'''
    Stable_Whiper should fix quiteness problem.
    Idea: devide audio into speaker and non-speaker sections. Audio with speaker translate and voiceover  
'''

import stable_whisper


def s2t(src_audio):
    
    model = stable_whisper.load_model('base')
    result = model.transcribe(src_audio, suppress_silence=False)
    result.to_srt_vtt(src_audio + '.srt')
