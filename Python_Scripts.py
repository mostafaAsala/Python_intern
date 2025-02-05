import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar'],
        'Scripts': ['.py', '.sh', '.bat']
    }
    
    for category, extensions in file_types.items():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                for category, extensions in file_types.items():
                    if any(file.lower().endswith(ext) for ext in extensions):
                        shutil.move(file_path, os.path.join(directory, category, file))
                        break

    print("Files organized successfully!")

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ")
    organize_files(target_directory)
