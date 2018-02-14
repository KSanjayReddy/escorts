import os

cmd = "opencv_createsamples -img pos/{} -bg negatives.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 400"
def create_sh():
    for file_type in ['pos']:

        for img in os.listdir(file_type):

            with open('run.sh','a') as f:
                f.write(cmd.format(img)+'\n')

create_sh()
