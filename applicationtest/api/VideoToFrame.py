import cv2 as cv
import datetime
import random
import os
import shutil

class VideoToFrame:
    def __init__(self):
        pass

    def readVideo(self, path):
        capture = cv.VideoCapture(path)
        return capture
    def toFrame(self, capture):
        count = 0
        while True:
            count += 1
            isTrue, frame = capture.read()
            screenshot_name = 'applicationtest/static/images/'+str(count)+ '.jpg'        
            cv.imwrite(screenshot_name, frame)
            if cv.waitKey(20) & 0xff == ord('d'):  # this will wait for key press d
                break
    def deleteAll(slef, folder_path):
        for file_object in os.listdir(folder_path):
            file_object_path = os.path.join(folder_path, file_object)
            if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
                os.unlink(file_object_path)
            else:
                shutil.rmtree(file_object_path)
