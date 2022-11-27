# This file is able to livestream using ffmpeg the BBB video, Albert Gubau NIA: 229416
import os


def ex3(in_file):

    command_line = 'ffmpeg -re -i ' + str(in_file) + '.mp4 -vcodec libx264 -f mpegts udp://127.0.0.1:1234'
    # command_line = 'ffmpeg -re -i ' + str(in_file) + '.mp4 -vcodec libx264 -f flv rtmp://localhost:1935/live/stream'

    # Call the command line in terminal
    os.system(command_line)


# Call the function of the exercise
ex3("BBB_1min")
