import glob
import os
import augmentor as am
import helper as hp



input_path='test_augmentation/*.jpg'
output_path='output'
# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

images= hp.load_images(input_path)

bright_images= am.brighten(images) ## if brightness_coeff is undefined brightness is random in each image

# Save the processed images in the output directory
for i, image in enumerate(bright_images):
    output_file_path = os.path.join(output_path, f"brightened_{i}.jpg")
    hp.save_image(image, output_file_path)
