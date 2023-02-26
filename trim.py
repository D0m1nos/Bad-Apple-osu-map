import subprocess
import json

TOTAL_PARTS = 72
for i in range(0, TOTAL_PARTS+1):
    input_filename = "part"+str(i)
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", input_filename+str(".mp4")])
    duration = json.loads(out)
    print(duration)

    subprocess.call(["ffmpeg", "-i", input_filename+str(".mp4"), "-ss", "3.53", "-t", str(duration-5.16-3.53), "-async", "1", input_filename+str("Trimmed.mp4")])