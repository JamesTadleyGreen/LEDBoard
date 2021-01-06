from PIL import Image
import requests
from io import BytesIO
import numpy as np

class imageParser:
    def __init__(self, image_url, resolution):
        response = requests.get(image_url)
        self.img = Image.open(BytesIO(response.content))
        self.res = resolution
    
    def resize(self):
        """Converts the image to the resolution

        Returns:
            img: the resized image
        """
        return self.img.resize(self.res)

    def convert(self, img):
        """Converts the image top rgb format

        Args:
            img (image): the image to convert

        Returns:
            img: the formatted image
        """
        return img.convert('RGB')
    
    def pixel_list(self):
        """Gets a list of the pixel values

        Returns:
            np.array: array tuples of (r,g,b) values of shape res
        """
        p_l = []
        img = self.convert(self.resize())
        for x in range(self.res[0]):
            for y in range(self.res[1]):
                p_l.append(img.getpixel((x, y)))
        p_a = np.array(p_l, dtype=object).reshape((32, 32, -1))
        return p_a
