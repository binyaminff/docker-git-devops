import cv2
import os

def makeVideo(image_folder, video_name, fps=1):
    # List only image files (jpg, png, jpeg)
    images = [img for img in os.listdir(image_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()  # Sort alphabetically for consistent frame order

    if not images:
        print("No images found in folder.")
        return

    first_frame_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_frame_path)
    if frame is None:
        print(f"Failed to read the first image {images[0]}")
        return

    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can use 'MJPG', 'XVID', 'MP4V', etc.
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    for image_name in images:
        img_path = os.path.join(image_folder, image_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Skipping unreadable image {image_name}")
            continue

        # Resize image if needed to match first frame size
        if img.shape[:2] != (height, width):
            img = cv2.resize(img, (width, height))

        video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {video_name}")
