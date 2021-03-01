# import glob
import normal_save_video
import json
from datetime import datetime
from threading import Thread
import cv2
import pytesseract
import re
from PIL import Image
from pylab import array, uint8
import datetime
import time
import multiprocessing
import threading
import requests
import sys
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

def save_video(tim):
    # IMPORTING
    import datetime
    import numpy as np
    import logging
    import cv2
    import sys

    # VARIABLES
    sec=0.0
    framerate=1.0
    out=None
    write_vid=0

    # DEFINING LOGGER
    # (This will create log file for every call of save_video...)
    logger2 = logging.getLogger('save video')
    logger2.setLevel(logging.DEBUG)
    fh2 = logging.FileHandler('/home/amol/OCR/logistics/result/log_normal_video_save/normal_video_save_{}.log'.format(datetime.datetime.now()))
    fh2.setLevel(logging.INFO)
    logger2.addHandler(fh2)

    # CONNECTING TO CAMERA
    logger2.info("Initialising Camera Connection")
    ip = "192.168.11.3"
    camname = 'WagonSideView1'
    cap = cv2.VideoCapture()
    cap.open("rtsp://admin:jsw@2020@{}/Streaming/channels/1/?tcp".format(ip))
    logger2.info("Connected To Camera")

    while True:
        try:
            sec = sec + framerate
            sec = round(sec, 2)
            _, img = cap.read()
            logger2.info("alive - video_saving - {} - {}".format(camname,datetime.datetime.now()))
            print("alive - video_saving - {} - {}".format(camname,datetime.datetime.now()))

            if img is None:
                continue

            if sec % 10 != 0:
                continue

            # Scaling image to display
            scale_percent = 40
            width = int(img1.shape[1] * scale_percent / 100)
            height = int(img1.shape[0] * scale_percent / 100)
            img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
            height, width, _ = img.shape
            size = (width, height)

            if out==None:
                # VIDEO CREATOR
                logger2.info("Videowriter Creating")
                vf = '/media/amol/DATADRIVE1/normal_video_saving_for_ocr_sideview1/video_cctv_{}_{}.avi'.format(camname,tim)
                out = cv2.VideoWriter(vf, cv2.VideoWriter_fourcc(*'MJPG'), 2, size)
                write_vid=1

            tim1=datetime.datetime.now()
            if write_vid==1:
                if int((abs(tim1 - tim).total_seconds())) <= 600.0:
                    out.write(img)
                else:
                    logger2.info("Video Saving Completed for 10 Min...Breaking While Loop")
                    break

        except Exception as e:
            print("Theres Exception in normal_video_save - {}".format(e))
            logger2.info("Theres Exception in normal_video_save - {}".format(e))
            continue

    # When everything done, release the capture
    cv2.destroyAllWindows()
    cap.release()
    # Terminate Process
    logger2.info("Terminating normal_video_save...")
    sys.exit()
