import PIL
from PIL import Image
import os 

path= r"C:\Users\lee.cockcroft\Downloads\monday_attachments"
export_path = r'C:\Users\lee.cockcroft\Documents\python-new\compress/'

images = os.listdir(path)

def resize():
    for image in images:
        image_name = image.split('.', 1)[0]
        image = Image.open(path+"/"+image)

        
        image.save(export_path+image_name+ '.webp', 'webp', optimize=True, quality=80)

resize() 









