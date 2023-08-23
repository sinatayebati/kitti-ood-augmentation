import glob
import os
import augmentor as am
import helper as hp

# Define the available augmentation functions
available_augmentation_functions = {
    "brighten"  : am.brighten,
    "darken"    : am.darken,
    "add shadow": am.add_shadow,
    # Add more functions here
}

def process_images(input_path, output_path, augmentation_function):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    images = hp.load_images(input_path)
    processed_images = augmentation_function(images)

    # Save the processed images in the output directory
    for i, image in enumerate(processed_images):
        output_file_path = os.path.join(output_path, f"processed_{i}.jpg")
        hp.save_image(image, output_file_path)

if __name__ == "__main__":
    input_path = 'test_augmentation/input/*.jpg'
    output_path = 'test_augmentation/output'

    print("Available augmentation functions:")
    for func_name in available_augmentation_functions:
        print(func_name)

    selected_function_name = input("Choose an augmentation function: ")

    if selected_function_name in available_augmentation_functions:
        selected_function = available_augmentation_functions[selected_function_name]
        process_images(input_path, output_path, selected_function)
    else:
        print("Invalid augmentation function choice.")
