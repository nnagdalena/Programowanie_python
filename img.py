import glob
import cv2
from main import detector

path = glob.glob("*jpg")

for filename in path:
    img = detector(cv2.imread(filename))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
