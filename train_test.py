import os
import shutil
import random
from collections import defaultdict

def split_data_by_class(input_folder, labels_folder, output_folder, class_names, train_ratio=0.8):
    # Create output folders
    train_images_folder = os.path.join(output_folder, 'train', 'images')
    train_labels_folder = os.path.join(output_folder, 'train', 'labels')
    test_images_folder = os.path.join(output_folder, 'val', 'images')
    test_labels_folder = os.path.join(output_folder, 'val', 'labels')
    os.makedirs(train_images_folder, exist_ok=True)
    os.makedirs(train_labels_folder, exist_ok=True)
    os.makedirs(test_images_folder, exist_ok=True)
    os.makedirs(test_labels_folder, exist_ok=True)

    # Organize images by class
    class_images = defaultdict(list)
    for img in os.listdir(input_folder):
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            for class_name in class_names:
                if img.startswith(class_name):
                    class_images[class_name].append(img)
                    break

    # Split and copy data for each class
    for class_name, images in class_images.items():
        random.shuffle(images)
        train_count = int(len(images) * train_ratio)
        train_images = images[:train_count]
        test_images = images[train_count:]

        # Copy train images and labels
        for image in train_images:
            image_path = os.path.join(input_folder, image)
            label_file = image.rsplit('.', 1)[0] + '.txt'
            label_path = os.path.join(labels_folder, label_file)

            shutil.copy(image_path, train_images_folder)
            if os.path.exists(label_path):
                shutil.copy(label_path, train_labels_folder)
            else:
                print(f"Warning: Label file for {image} not found.")

        # Copy test images and labels
        for image in test_images:
            image_path = os.path.join(input_folder, image)
            label_file = image.rsplit('.', 1)[0] + '.txt'
            label_path = os.path.join(labels_folder, label_file)

            shutil.copy(image_path, test_images_folder)
            if os.path.exists(label_path):
                shutil.copy(label_path, test_labels_folder)
            else:
                print(f"Warning: Label file for {image} not found.")

    print("Data split completed.")

# Usage example
if __name__ == "__main__":
    input_folder = "img&lables\images"  # Path to your images folder
    labels_folder = "img&lables\labels"  # Path to your labels folder
    output_folder = "D:\Projects\Object-Detection\data"  # Path to the output folder
    class_names = ['Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes']  # List of class names
    split_data_by_class(input_folder, labels_folder, output_folder, class_names)
