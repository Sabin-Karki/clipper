import subprocess
import os

input_file = "benzema.mp4"
output_file = "output/new_clip.mp4"

start_time = "00:00:00"
duration = "00:01:20"


os.makedirs("output",exist_ok=True)

original_size =  os.path.getsize(input_file) / (1024 * 1024) 
print(f"Original size: {original_size:.2f} MB")


# trim video , need it under 25mb

command = ["ffmpeg","-ss",start_time,"-i" ,input_file,"-t", duration,"-c","copy",output_file]

subprocess.run(command,check=True)

#output size
output_size = os.path.getsize(output_file) / (1024 * 1024)
print(f"output size : {output_size:.2f} MB")