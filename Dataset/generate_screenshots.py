import cv2
import os
import time


def take_screenshot(file_path):
    file_name = file_path.split('/')[-1]
    if not os.path.exists('Dataset/Images'):
        os.makedirs('Dataset/Images')
    if not os.path.exists(f'Dataset/Images/{file_name}'):
        os.makedirs(f'Dataset/Images/{file_name}')
    
    cam = cv2.VideoCapture(file_path)

    currentframe = -1
    every_n_frame = 23

    while cam.isOpened():
        ret, frame = cam.read()
        if ret:
            currentframe += 1
            if currentframe % every_n_frame == 0:
                name = f'Dataset/Images/{file_name}/frame_' + str(currentframe // every_n_frame) + '.jpg'
                cv2.imwrite(name, frame)
        else:
            break


directory = 'Dataset/Videos'

for file in os.listdir(directory):
    print(file)
    take_screenshot(directory + '/' + file)
