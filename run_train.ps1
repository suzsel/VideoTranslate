$input_audio = Read-Host "Enter input audio file"
$input_speaker = Read-Host "Enter speake name"
$path_for_train = "cloning/$input_speaker/dataset_raw/$input_speaker"

mkdir $path_for_train

ffmpeg -i $path_for_train + $input_audio -f segment -segment_time 10 -c copy 04d.wav

# start train voice model
svc pre-resample
svc pre-config
svc pre-hubert
svc train -t
