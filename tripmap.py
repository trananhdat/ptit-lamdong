import cv2, os, sys
from trimap_module import trimap
from glob import glob

def extractImage(path):
    # error handller if the intended path is not found
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # image = cv2.imread(path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    return image

list_file = glob("G://2_smoke//1_house//images//*")
print(len(list_file))
count = 0
for file_path in list_file:
    count += 1
    print(file_path)
    try:
        path    = file_path
        # print(path)
        image   = extractImage(path);
        # print(image)
        name    = file_path.split('\\')[-1].split('.png')[0];
        size    = 30; # how many pixel extension do you want to dilate
        number  = 1;  # numbering purpose 
        trimap(image, name, size, number, erosion=False)
    except Exception as e:
        print(e)
        continue

print(count)

