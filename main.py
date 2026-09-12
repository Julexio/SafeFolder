import os
import shutil

# Step 2 — Ask for the folder to organize
folder_path = input("Enter the folder path to organize: ").strip()

# Step 3 — Check that the folder actually exists
if not os.path.exists(folder_path):
    print(f"Error: The folder '{folder_path}' does not exist.")
else:
    # Step 4 — Get the list of files in the folder
    all_items = os.listdir(folder_path)

    # Step 5 — Set up counters
    images_count = 0
    documents_count = 0
    videos_count = 0
    others_count = 0

    # Define category names
    categories = ["Images", "Documents", "Videos", "Others"]

    # Step 6 — Create the destination subfolders
    for category in categories:
        subfolder_path = os.path.join(folder_path, category)
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)

    # Step 7 — Loop through every file and sort it
    for item in all_items:
        item_path = os.path.join(folder_path, item)

        # Skip if it is one of the category subfolders or any other folder
        if item in categories or os.path.isdir(item_path):
            continue

        # Convert filename to lowercase to handle extensions safely (e.g., .JPG)
        item_lower = item.lower()

        # Determine the target category based on file extensions
        if item_lower.endswith((".jpg", ".jpeg", ".png", ".gif")):
            target_folder = "Images"
            images_count += 1
        elif item_lower.endswith((".pdf", ".docx", ".txt", ".pptx")):
            target_folder = "Documents"
            documents_count += 1
        elif item_lower.endswith((".mp4", ".mov", ".avi")):
            target_folder = "Videos"
            videos_count += 1
        else:
            target_folder = "Others"
            others_count += 1

        # Step 8 — Actually move the file
        destination_path = os.path.join(folder_path, target_folder, item)
        shutil.move(item_path, destination_path)

        # Step 9 — Print what happened, file by file
        print(f"Moved: {item} -> {target_folder}/")

    # Step 10 — Print a final summary
    total_files = images_count + documents_count + videos_count + others_count
    print("\n----- FOLDER SUMMARY -----")
    print(f"Images moved: {images_count}")
    print(f"Documents moved: {documents_count}")
    print(f"Videos moved: {videos_count}")
    print(f"Others moved: {others_count}")
    print(f"Total files organized: {total_files}")
