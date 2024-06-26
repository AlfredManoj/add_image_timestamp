import datetime
import cv2
import os
import shutil
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


date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
time_entry = input('Enter the time in 24 hour format hh:mm')
hour, minute = map(int, time_entry.split(':'))
user_given_datetime = datetime.datetime(year, month, day, hour, minute)

image_folder_path = os.path.join(os.getcwd(), "Images")
result_folder_path = os.path.join(os.getcwd(), "Result")
if not os.path.exists(image_folder_path):
    os.mkdir(image_folder_path)
if os.path.exists(result_folder_path):
    shutil.rmtree(result_folder_path)
os.mkdir(result_folder_path)

# clear result folder each time
# shutil.rmtree(result_folder_path)
# for file in os.listdir(result_folder_path):


# we are assuming that only 3 images will be taken in one minute
# so any image list containing more than 3 images will have auto-incremented timeline
total_images = 0

image_list = load_images_from_folder(image_folder_path)
for image in image_list:
    # Open an Image
    img = Image.open(os.path.join(os.getcwd(), "Images", image))

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    myFont = ImageFont.truetype('Roboto-Regular.ttf', 20)

    (x, y) = img.size

    increment_value = total_images // 3
    computed_datetime = user_given_datetime + datetime.timedelta(minutes=increment_value)

    # datetime_string = computed_datetime.strftime("%Y/%-m/%d %H:%M")
    datetime_string = '{d.year}/{d.month}/{d.day} {d.hour:02}:{d.minute:02}'.format(d=computed_datetime)
    # Add Text to an image
    I1.text((10, y-35), datetime_string, font=myFont, fill=(255, 255, 255))

    # increment total image count
    total_images += 1

    # Display edited image
    # img.show()

    # Save the edited image
    img.save(os.path.join(os.getcwd(), "Result", image))

