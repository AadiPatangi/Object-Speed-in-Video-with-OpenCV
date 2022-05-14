# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import cv2



def videoProperties(videoIn):

    vid = cv2.VideoCapture(videoIn)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)  # always 0 in Linux python3
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)  # always 0 in Linux python3
    print("opencv: height:{} width:{}".format(height, width))


    flength = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = vid.get(cv2.CAP_PROP_FPS)

    print("Frame Count: {}".format(flength))
    print("Fps        : {}".format(fps))


def extractImages(videoIn, pathOut):
    vidcap = cv2.VideoCapture(videoIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print(count)
      if count > 40 and count < 120 :
          print('Write a new frame: ', success)
          cv2.imwrite( pathOut + "frame%d.jpg" % count, image)     # save frame as JPEG file
      count += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(sys.version)

    input_video = '/users/projects/input/trial3.mov'
    output_dir  = '/users/projects/output/'

    videoProperties(input_video)
    extractImages(input_video,output_dir)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
