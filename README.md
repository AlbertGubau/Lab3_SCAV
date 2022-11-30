# Lab3_SCAV

## Task 1 (ex1.py)
This script is able to create an HLS transport stream container with the BBB_1min video file.
In the results, we obtain the following files:

&nbsp; &nbsp; master.u3u8 --> Stores the the playlist with the streams in different resolutions
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  stream_0.u3u8 --> Stores the video fragments in 1280x720 resolution
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data00.ts, data01.ts, data02.ts ...
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  stream_1.u3u8 --> Stores the video fragments in 854x480 resolution
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data00.ts, data01.ts, data02.ts ...
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  stream_2.u3u8 --> Stores the video fragments in 640x360 resolution
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data00.ts, data01.ts, data02.ts ...

Which are the files present in the HLS container and enables us to live stream using fragments with different resolutions (that allows us to apply ABR).

## Task 2 (no script associated, only screenshots)
The screenshots that explain this exercise are the following ones:

&nbsp; &nbsp; &nbsp; &nbsp; fragmentation.png (Shows the fragmentation process of the BBB video)
&nbsp; &nbsp; &nbsp; &nbsp; info_fragmentation.png (Shows the fragmented video info to demonstrate that is fragmented)
&nbsp; &nbsp; &nbsp; &nbsp; dashing_and_encryption.png (Shows the dashing plus encryption process using marlin encryption)
&nbsp; &nbsp; &nbsp; &nbsp; unable_to_open.png (Shows that the video is actually encrypted because we cannot access it using VLC)

Therefore, we can see that we have accomplished our goal, we can also see that the MPD file is created in the output folder.

## Task 3 (ex3.py)
This script is able to livestream the BBB video using ffmpeg. The implementation that I used allows only to see it locally because I didn't find the address that allows me to do it for the same network, using ffplay and the address that I use we can see the livestream properly. I use the UDP network protocol and the address (127.0.0.1:1234). In class I commented with the teacher to use the open address 222.2.2.2:2222 but trying didn't work, so the teacher told me to leave it this way and explain it here.

## Task 4 (no script associated, only screenshots)
For this exercise, I used a Twitch livestreaming to see what protocols and codecs uses.
To do so, I used the dev tools and I found that the streaming protocol used was HLS as it had .m3u8 and .ts files to livestream.
Then I also analyzed one .ts segment in order to see the video codec that it uses and I found that it used h264 and aac codecs. But also, it uses some codecs that ffprobe cannot detect for the second stream.

The screenshots that explain this exercise are the following ones:

&nbsp; &nbsp; &nbsp; &nbsp; dev_tools_twitch.png (Shows the dev tools to look at the network packages that are been sent)
&nbsp; &nbsp; &nbsp; &nbsp; segment_info_twitch.png (Shows the codecs info from the Twitch saved .ts segment)

You can also check the saved segment in the twitch_segment.ts file.


