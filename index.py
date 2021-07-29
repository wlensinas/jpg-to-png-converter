from PIL import Image
import os
import sys


if sys.argv.__len__() == 3:
    path_images = sys.argv[1]
    path_new_images = sys.argv[2]
    if os.path.exists(path_images):
        if not os.path.exists(path_new_images):
            os.mkdir(path_new_images)
            print(f'Created directory: {path_new_images}')
        images = [f for f in os.listdir(path_images) if os.path.isfile(os.path.join(path_images, f))]
        for image in images:
            img = Image.open(os.path.join(path_images,image))
            filename, file_extension = os.path.splitext(image)
            my_new_path = os.path.join(path_new_images, filename+'.png')
            img.save(my_new_path, "png")
            print(f'Saved the file {my_new_path}')
        print('Done!')
else:
    print('Warning, you need to call with 2 arguments')
    print('python index.py <path_folder_jpg> <new_path>')
