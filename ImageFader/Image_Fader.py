from asyncio.windows_utils import pipe
from ctypes.wintypes import CHAR
from configparser import ConfigParser
from lib2to3.pgen2.token import COMMA
import os
from xml.etree.ElementTree import fromstring
from time import sleep
import pyodbc
import re
import logging
from tqdm import tqdm,trange
import time
import os
from PIL import Image,ImageEnhance
from configparser import ConfigParser
from tqdm import tqdm,trange

#Config file Setup
conFile = 'config.ini'
config = ConfigParser()
config.read(conFile)
config.sections()

## Folder Path
#path = "X:\Edwin\FileParser\TR135"
InPath = config.get('ReadPath','Rpath')
factor = config.get('Brightness', 'factor')
# Change the directory
os.chdir(InPath)
  
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'rb') as f:
        print(f.read())

# iterate through all file
counter = 0
fileList =os.listdir()
for in_file in tqdm(fileList[0:]):
    sleep(0.5)
    try:
    # Check whether file is in png format or not
        if in_file.endswith(".png") :
            file_path = f"{InPath}\{in_file}"
            # call read text file function
            read_text_file(file_path)
        else:
            raise Exception("Invalid file")           
    except Exception:
        
        logging.error(in_file +" " + "File Error, invalid name or filetype!")
    else:       
          with open(file_path) as fi:
            WPath = config.get('WritePath','WPath')  
            WPath = open(WPath % counter, 'wb') 

            im = Image.open(in_file)
            enhancer = ImageEnhance.Brightness(im)
            #factor = 1.5 #darkens the image
            #float(factor)
            im_output = enhancer.enhance(float(factor))
          
            im_output.save(WPath)  
            
                                            
            counter +=1








