import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img1 = cv2.cvtColor(cv2.imread('1.JPG'), cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(cv2.imread('2.JPG'), cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(cv2.imread('3.JPG'), cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(cv2.imread('4.JPG'), cv2.COLOR_BGR2GRAY)

def read_from_image(img):
     return pytesseract.image_to_string(img)


print(read_from_image(img1))
print(read_from_image(img2))
print(read_from_image(img3))
print(read_from_image(img4))