import numpy as np
import matplotlib.pyplot as plt
import cv2

def drawImg(img , title="Image"):
    plt.imshow(img,cmap='gray')
    plt.axis('off')
    plt.title(title+str(img.shape))
    plt.show()

def convolution(img,img_filter):
    w = img.shape[0]
    h = img.shape[1]
    f = img_filter.shape[0]

    new_image = np.zeros((w-f+1 , h-f+1))

    for row in range(w-f+1):
        for col in range(h-f+1):
            for i in range(f):
                for j in range(f):
                    new_image[row][col] += img[row+i][col+j] * img_filter[i][j]

                if (new_image[row][col]>255):
                    new_image[row][col] = 255

                elif (new_image[row][col]<0):
                    new_image[row][col] = 0

    return new_image

img = cv2.imread("mickey.jpeg")
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
drawImg(img,"Mickey Mouse")
img = cv2.resize(img,(100,100))
drawImg(img)

# Extracting features from an image using filters

# Converting 3D image to 2D using Grayscale since RGB image has 3 channels while gray image has only 1 channel
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
drawImg(img_gray)

# We are averaging the image pixels which leads to blurring
blur_filter = np.ones((3,3))/9.0
output1 = convolution(img_gray , blur_filter)
drawImg(output1)

# Defining a filter such that ony edges are visible
edge_filter = np.array([[1,0,-1],
                        [1,0,-1],
                        [1,0,-1]])

output2 = convolution(img_gray , edge_filter)
drawImg(output2)

xyz_filter = np.array([[2,2,-2],
                       [2,2,-2],
                       [2,2,-2]])

output3 = convolution(img_gray , xyz_filter)
drawImg(output3)