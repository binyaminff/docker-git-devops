import requests
import os

def download_image(image_url, index):
    try:
        # Check if URL ends with valid image extensions (case insensitive)
        if not image_url.lower().endswith(('.jpeg', '.jpg', '.png')):
            print(f"Skipped URL (not a supported image): {image_url}")
            return

        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        image_bytes = response.content

        if not image_bytes:
            print(f"Skipped empty image from URL: {image_url}")
            return

        save_path = os.path.join('C:/Users/User/PycharmProjects/devops/images/', f'{index}.jpg')
        with open(save_path, 'wb') as handle:
            handle.write(image_bytes)
            print(f"Downloaded image {index} from {image_url}")

    except Exception as e:
        print(f"Error downloading image {image_url}: {e}")
