# This file is able to livestream using ffmpeg the BBB video, Albert Gubau NIA: 229416
import os


def ex3(in_file):

    # Command line to livestream the input video file locally
    # I tried also with rtmp but an error occurs while accessing the ports
    # Therefore, I used this method that enables me to display the livestream locally
    # I also tried with the address 222.2.2.2:2222 which should be opened always but it doesn't work anyways
    command_line = 'ffmpeg -re -i ' + str(in_file) + '.mp4 -vcodec libx264 -f mpegts udp://127.0.0.1:1234'

    # Call the command line in terminal
    os.system(command_line)


# Call the function of the exercise
ex3("BBB_1min")
