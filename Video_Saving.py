# ***************************************
# Camera Connection through python code..
# ***************************************


# Importing required libraries
import datetime
import cv2 as cv2
import logging
from logging.handlers import TimedRotatingFileHandler
import time
import numpy as np

# LOGGER INFO
# l1 = datetime.datetime.now()
# logger = logging.getLogger("Rotating Log")
# logger.setLevel(logging.INFO)
# handler = TimedRotatingFileHandler("/home/jsw/PycharmProjects/pythonProject/log_cam_connection_2/log_{}.log".format(l1), when="m", interval=60)
# logger.addHandler(handler)

# VARIABLES
sec=0.0
framerate=1.0
out=None
t1=time.time()

# Assigning IP address
ip1 = "192.168.12.10"
ip2 = "192.168.12.11"
ip3 = "192.168.12.12"
ip4 = "192.168.12.13"
ip5 = "192.168.12.14"
ip6 = "192.168.12.15"
ip7 = "192.168.12.16"
ip8 = "192.168.12.17"

# Using opencv for capturing image
cap = cv2.VideoCapture()

# Camera connection using credentials help of rtsp (we can do in https also)
cap.open("rtsp://admin:vert@123@{}/Streaming/channels/1/?tcp".format(ip8))
print("Camera Connected")

# Through https also we can connect live cam to avoid gray imgages
# cam = Client('http://192.168.2.241', 'admin', 'Password@123')
#
# while True:
#
#     # Model is Trying to get live images from camera_1...
#     try:
#         vid = cam.Streaming.channels[102].picture(method='get', type='opaque_data')
#
#         bytes = b''
#
#         with open('screen1.jpg', 'wb') as f:
#             for chunk in vid.iter_content(chunk_size=1024):
#                 bytes += chunk
#                 a = bytes.find(b'\xff\xd8')
#                 b = bytes.find(b'\xff\xd9')
#                 if a != -1 and b != -1:
#                     jpg = bytes[a:b + 2]
#                     bytes = bytes[b + 2:]
#                     img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
#                     cv2.imwrite("/media/jsw/Data/newimage/Cam_image_{}.jpg".format(save_image), img)
#                     save_image += 1
#                     # print("image capture")
#
#                     # Checking blank images from live camera...
#                     if img is None:
#                         none_frame += 1
#                         logger.info("NONE frame for t1 - {}".format(none_frame))
#                         print("None frame -{}".format(none_frame))
#                     else:
#                         none_frame = 0

while True:

    try:

        # GET CURRENT TIME/SEC
        t2=time.time()
        if t2-t1>3540:
            # logger.info("Its 1 hr...will create new video")
            t1=time.time()
            out=None

        # Reading Image from live camera
        _, img=cap.read()
        # print("Image has been read")

        # Checking Image from live camera
        if img is None:
            print("Blank Image")
            # logger.info("None image-{}".format(datetime.datetime.now()))
            continue

        # SKIP FRAMES
        sec = sec + framerate
        if sec % 2 != 0:
            continue

        # RESIZING FRAME
        scale_percent = 40
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
        height, width, _ = img.shape
        size = (width, height)

        # DEFINE VIDEO WRITER for every one hour - Give your video saving path to save live video
        if out == None:

            # logger.info("Creating VideoWriter")
            # out = cv2.VideoWriter("/media/jsw/Data/saved_video_2/video_{}.avi".format(datetime.datetime.now()),cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
            out = cv2.VideoWriter("/home/root1/CVML_2/Live_Video/video_{}.avi".format(datetime.datetime.now()),cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
            # logger.info("VideoWriter Created")

        # SAVING VIDEO from live camera
        # out.write(img)
        # print("start save video")


        # Camera live image show
        cv2.imshow('Live Camera image', img)
        cv2.waitKey(1)

    except Exception as e:
        print("Theres an exception-{}".format(e))