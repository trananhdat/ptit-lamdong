import cv2
from glob import glob

list_files = glob("G:\\2_smoke\\1_house\\images\\*")

for file in list_files:
    print(file)

    # Load .png image
    image = cv2.imread(file)
    
    image_name = str(file).split("\\")[-1].split(".")[0]
    print(image_name)

    # Save .jpg image
    cv2.imwrite("G:\\2_smoke\\1_house\\images_jpg\\" + image_name + ".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    # break
    
