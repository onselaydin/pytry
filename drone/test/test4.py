import cv2
import numpy as np
import sys
import time

if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    inputImage = cv2.imread("C:/pytry/drone/test/qrcode.png")

def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
    cv2.imshow("Results", im)

qrDecoder = cv2.QRCodeDetector()
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage)
    cv2.imshow("Rectified QRCode", rectifiedImage)
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
