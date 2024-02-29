from moviepy.editor import *
import os
from glob import glob


def append_Vids_to_trgtVid(trgt_vid_path, vid_path_list):
    trgt_vid_nm = split_by(split_by(trgt_vid_path, "/", -1), "_", 1) + "_" + split_by(split_by(trgt_vid_path, "/", -1), "_", 2)
    for another_vid_path in vid_path_list:
        another_vid_nm = split_by(split_by(another_vid_path, "/", -1), "_", 1) + "_" + split_by(split_by(another_vid_path, "/", -1), "_", 2)
        tmp_vid_list = [VideoFileClip(trgt_vid_path)]
        tmp_vid_list.append(VideoFileClip(another_vid_path))
        tmp_vid_list.append(VideoFileClip(another_vid_path))
        concat_vid = concatenate_videoclips(tmp_vid_list)
        concat_vid.to_videofile(f"output/{trgt_vid_nm}_{another_vid_nm}.mp4", fps=24, remove_temp=False)


def split_by(input_str, deli, idx):
    return input_str.split(deli)[idx]


if __name__ == '__main__':
    scrn_shot_list = glob("input_videos/screen_shot_20240229/*.mp4")

    append_Vids_to_trgtVid(scrn_shot_list.pop(3), scrn_shot_list)

