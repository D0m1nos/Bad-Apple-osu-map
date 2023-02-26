# Bad Apple osu! map

![Thumbnail](thumbnail.png)
Watch the video on [<img src='https://www.youtube.com/s/desktop/7449ebf7/img/favicon_32x32.png' width='16px'/> Youtube](https://youtu.be/g4x5-5EV3K4)!

## Steps i took to create the video:
1. Split the original Bad Apple video into frames with ffmpeg
2. Resize the original frames into 36x28 images (using [convert.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/convert.py))
3. Create an array containing each pixel of every frame, 1 means black and 0 means white (also done using [convert.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/convert.py), the final result is in [data.json](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/data.json))
4. Convert the array in osu! beatmaps (using [script.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/script.py)), the beatmap is divided into several parts because the original is too big and can't be used with danser
5. Create videos of the beatmaps with [danser](https://github.com/Wieku/danser-go) (settings used are [show map.json](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/show%20map.json)) and [makeVideo.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/makeVideo.py)
6. Trim the videos with [trim.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/trim.py) (requires ffprobe and ffmpeg)
7. Combine the trimmed videos with editing software

**Note**: these scripts are messy and not optimized, they might not work with your setup.

Other things to note:
- You need to change danser's settings to make it work with your setup
- [makeVideo.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/makeVideo.py) must be placed in danser's directory while [trim.py](https://github.com/D0m1nos/Bad-Apple-osu-map/blob/main/trim.py) needs to be placed in danser's output folder
- Creating the videos takes a looooong time, on my pc it took 40 minutes by running 3 instances of danser at the same time
- I used [this](https://osu.ppy.sh/beatmapsets/18260#osu/65419) map as reference to create the different beatmap parts