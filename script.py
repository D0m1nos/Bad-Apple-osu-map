import json
import math
import os

def formatFile(part):
    OSU_FILE = f'osu file format v14\n\n[General]\nAudioFilename: Masayoshi Minoshima - Bad Apple!! feat. nomico - Touhou PV [iichan].mp3\nAudioLeadIn: 1500\nPreviewTime: 29159\nCountdown: 0\nSampleSet: Normal\nStackLeniency: 0.5\nMode: 0\nLetterboxInBreaks: 0\nStoryFireInFront: 0\nWidescreenStoryboard: 1\n\n[Editor]\nBookmarks: 29159,56985,84811,112637,126561,154387,182246,210072\nDistanceSpacing: 0.5\nBeatDivisor: 4\nGridSize: 8\nTimelineZoom: 1\n\n[Metadata]\nTitle:Bad Apple!!\nTitleUnicode:Bad Apple!!\nArtist:Masayoshi Minoshima feat. nomico\nArtistUnicode:Masayoshi Minoshima feat. nomico\nCreator:ouranhshc\nVersion:part{part}\nSource:Touhou\nTags:Krisom -K- Blue Dragon Armin Kecco TKiller Linkred2 Lepidopodus\nBeatmapID:0\nBeatmapSetID:-1\n\n[Difficulty]\nHPDrainRate:0\nCircleSize:10\nOverallDifficulty:0\nApproachRate:10\nSliderMultiplier:2\nSliderTickRate:2\n\n[Events]\n//Background and Video events\n0,0,"flandre-badapple.jpg",0,0\n//Break Periods\n//Storyboard Layer 0 (Background)\n//Storyboard Layer 1 (Fail)\n//Storyboard Layer 2 (Pass)\n//Storyboard Layer 3 (Foreground)\nSprite,Foreground,Centre,"Krisom.png",90,60\n F,0,1333,1767,0,1\n F,0,28724,29376,1,0\nSprite,Foreground,Centre,"Armin.png",90,60\n F,0,29159,29593,0,1\n F,0,56550,57202,1,0\nSprite,Foreground,Centre,"Linkred2.png",120,65\n F,0,56985,57419,0,1\n F,0,84376,85028,1,0\nSprite,Foreground,Centre,"Kecco.png",90,60\n F,0,84811,85246,0,1\n F,0,112202,112854,1,0\nSprite,Foreground,Centre,"-K-.png",90,60\n F,0,126561,126995,0,1\n F,0,153952,154604,1,0\nSprite,Foreground,Centre,"Blue Dragon.png",150,60\n F,0,154387,154821,0,1\n F,0,181778,182455,1,0\nSprite,Foreground,Centre,"TKiller.png",90,60\n F,0,182246,182680,0,1\n F,0,209637,210281,1,0\n//Storyboard Layer 4 (Overlay)\n//Storyboard Sound Samples\n\n[TimingPoints]\n1333,434.782608695652,4,1,1,70,1,0\n84811,-100,4,2,1,100,0,0\n126561,434.782608695652,4,1,1,70,1,0\n182238,434.782608695652,4,1,1,70,1,0\n189520,-200,4,1,1,70,0,0\n189955,-100,4,1,1,70,0,0\n191042,-200,4,1,1,70,0,0\n192020,-100,4,1,1,70,0,0\n197020,-100,4,2,1,70,0,0\n209194,1739.13043478261,4,2,1,70,1,0\n210172,-100,4,2,1,0,0,0\n\n\n[HitObjects]\n'
    return OSU_FILE

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
WIDTH = 512
HEIGHT = 383
CS = 10
RADIUS = round(54.4 - 4.48 * CS) # https://osu.ppy.sh/wiki/en/Beatmap/Circle_size#osu!
OBJ_IN_EACH_PART = 50000

# Hit object syntax: x,y,time,type,hitSound,objectParams,hitSample
# 0,0,1224,1,0,0:0:0:0:
UNUSED_SYNTAX = ',1,0,0:0:0:0:'

with open(ROOT_DIR + '\\data.json', 'r') as f:
    frames = json.load(f)
    f.close()

totalFrames = len(frames)
totalObjects = 0
out = ''
part = 0
time = 1333
objCount = 0

for frame in frames:
    print(f'remaining frames: {totalFrames}')

    if objCount>=OBJ_IN_EACH_PART:
        f = open(ROOT_DIR + f'\\Masayoshi Minoshima feat. nomico - Bad Apple!! (ouranhshc) [part{part}].osu', 'w')
        out = formatFile(part) + out
        f.write(out)
        f.close()
        part += 1
        totalObjects += objCount
        objCount = 0
        out = ''
    circleY = 0
    for x in frame:
        circleX = 0
        for y in x:
            if y==1:
                objCount += 1
                out += str(circleX) + ',' + str(circleY) + ',' + str(time) + UNUSED_SYNTAX
                out += '\n'
            circleX += RADIUS+8
        circleY += RADIUS+8
    time+=42
    totalFrames -= 1

f = open(ROOT_DIR + f'\\Masayoshi Minoshima feat. nomico - Bad Apple!! (ouranhshc) [part{part}].osu', 'w')
out = formatFile(part) + out
f.write(out)
f.close()
totalObjects += objCount

print(f'{len(frames)} total frames with {totalObjects} objects divided in {part} parts ({OBJ_IN_EACH_PART} objects in each part)')