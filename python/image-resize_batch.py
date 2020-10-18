import os
import cv2

os.chdir('D:/sotl/images_repo')
images_path = 'D:/sotl/images_repo'

c = 1

def calculate_image_sizes (shape):
    width = 150
    height = int(150 * shape[1] / shape[0])

    return width, height 




for _file in os.listdir(images_path):
    full_path = os.path.join(images_path, _file)
    print(full_path)
    img = cv2.imread(full_path)

    width, height = calculate_image_sizes (img.shape)
    file_name = 'file-0' + str(c) + '.jpg'
    dimension = (width, height)
    
    resize = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
    cv2.imwrite(file_name, resize)

    c += 1


# img1 = cv2.imread('headphones.jpg')

# scale_percent = 0.08
# width = int(img1.shape[1]* scale_percent)
# height = int(img1.shape[0]* scale_percent)

# dimension = (width, height)

# resize = cv2.resize(img1, dimension, interpolation=cv2.INTER_AREA)

# cv2.imshow('Test', resize)
# cv2.imwrite('headphones-smallest.jpg', resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
