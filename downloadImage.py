import requests
import os
def download_image(image_url,index):
    try:

     if(image_url.find("jpeg") != -1&image_url.find("jpg") != -1):

      with open(f'{os.path.join('C:/Users/User/PycharmProjects/devops/images/', f'{index}.jpg')}', 'wb') as handle:
         response = requests.get(image_url, stream=True)
         response.raw.decode_content = True  # Handles gzip/deflate encodings
         image_bytes = response.raw.read()
         handle.write(image_bytes)
         print(image_bytes)
     else:

      with open(f'{os.path.join('C:/Users/User/PycharmProjects/devops/images/', f'{index}.jpg')}', 'wb') as handle:

         response = requests.get(image_url, stream=True)
         response.raw.decode_content = True  # Handles gzip/deflate encodings
         image_bytes = response.raw.read()
         handle.write(image_bytes)
         print(image_bytes)

    except Exception as e:
        print(f"Error downloading image: {e}")
        image_bytes = None

