# This file is able to create a new HLS transport stream container with the BBB video, Albert Gubau NIA: 229416
import os
import shutil


def ex1(in_file):

    # Remove files from other executions
    if os.path.exists("master.m3u8"):
        os.remove("master.m3u8")

    if os.path.exists("stream_0.m3u8"):
        os.remove("stream_0.m3u8")

    if os.path.exists("stream_1.m3u8"):
        os.remove("stream_1.m3u8")

    if os.path.exists("stream_2.m3u8"):
        os.remove("stream_2.m3u8")

    if os.path.exists("stream_0"):
        shutil.rmtree("stream_0")

    if os.path.exists("stream_1"):
        shutil.rmtree("stream_1")

    if os.path.exists("stream_2"):
        shutil.rmtree("stream_2")

    # Create the command line that creates the m3u8 files for the different resolutions and then
    # fills them with created segments as .ts files
    # The resolutions will be: Original (from the video), 854x480 and 640x360

    command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 \
                    -filter_complex \
                    "[0:v]split=3[v1][v2][v3]; \
                    [v1]copy[v1out]; [v2]scale=w=854:h=480[v2out]; [v3]scale=w=640:h=360[v3out]" \
                    -map [v1out] -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" ' \
                    '-b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 10M -preset slow ' \
                    '-g 48 -sc_threshold 0 -keyint_min 48 \
                    -map [v2out] -c:v:1 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" ' \
                    '-b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M -bufsize:v:1 3M -preset slow ' \
                    '-g 48 -sc_threshold 0 -keyint_min 48 \
                    -map [v3out] -c:v:2 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" ' \
                    '-b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M -bufsize:v:2 1M -preset slow ' \
                    '-g 48 -sc_threshold 0 -keyint_min 48 \
                    -map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
                    -map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
                    -map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
                    -f hls \
                    -hls_time 2 \
                    -hls_playlist_type vod \
                    -hls_flags independent_segments \
                    -hls_segment_type mpegts \
                    -hls_segment_filename stream_%v/data%02d.ts \
                    -master_pl_name master.m3u8 \
                    -var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" stream_%v.m3u8""'

    # Call the command line in terminal
    os.system(command_line)


# Call the function of the exercise
ex1("BBB_1min")
