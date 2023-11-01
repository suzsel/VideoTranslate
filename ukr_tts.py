from ukrainian_tts.tts import TTS, Voices, Stress
import IPython.display as ipd
import sys

def transcribe(device, src_txt, ):

    tts = TTS(device=device) # can try gpu, mps
    c = 0
    with open(src_txt, 'r', encoding="utf-8") as input:
        for line in input:
            c += 1
            with open("test_ukrs2t" + str(c) + ".wav", mode="wb") as file:
                _, output_text = tts.tts(line, Voices.Dmytro.value, Stress.Dictionary.value, file)
    print(f'transcription to ukr is done \n output[:20] = {output_text[:20]} \n {c} files')

    ipd.Audio(filename="test.wav")