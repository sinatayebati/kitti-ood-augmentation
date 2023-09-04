import glob
import os
import augmentor as am
import helper as hp


input_path='KITTI/training/image_2/*.png'
output_path='KITTI-C/image/wet_ground/heavy'
# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

images= hp.load_images(input_path)

bright_images= am.add_rain(images, rain_type="torrential", slant=20) 

# Save the processed images in the output directory
for i, image in enumerate(bright_images):
    output_file_path = os.path.join(output_path, f"{i}.png")
    hp.save_image(image, output_file_path)