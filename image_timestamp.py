import cv2
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        imag = cv2.imread(os.path.join(folder, filename))
        if imag is not None:
            images.append(filename)
    return images


image_folder_path = os.path.join(os.getcwd(), "Images")
result_folder_path = os.path.join(os.getcwd(), "Result")
if not os.path.exists(image_folder_path):
    os.mkdir(image_folder_path)
if not os.path.exists(result_folder_path):
    os.mkdir(result_folder_path)

image_list = load_images_from_folder(image_folder_path)
for image in image_list:
    # Open an Image
    img = Image.open(os.path.join(os.getcwd(), "Images", image))

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    myFont = ImageFont.truetype('Roboto-Regular.ttf', 20)

    (x, y) = img.size

    # Add Text to an image
    I1.text((10, y-35), "2024/4/25  09:41", font=myFont, fill=(255, 255, 255))

    # Display edited image
    # img.show()

    # Save the edited image
    img.save(os.path.join(os.getcwd(), "Result", image))

