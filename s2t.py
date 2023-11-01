import whisper 


#  sys.argv[1] - model name 
#  sys.argv[2] - audio file
#  TODO check for valid path assertion errors 

def s2t(model, src_audio):
    model = whisper.load_model(model)
    result = model.transcribe(src_audio)
    with open(src_audio+".txt", "w", encoding="utf-8") as res:
        res.write(result["text"])

    print(result["text"])
