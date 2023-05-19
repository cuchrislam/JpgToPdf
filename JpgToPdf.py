#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from PIL import Image

#This program was created by promting Chatgpt
# Accept the directory path as input from the user
dir_path = input("Enter the directory path: ")

# Walk through the directory and convert all JPG files to PDF
for root, dirs, files in os.walk(dir_path):
    for file in files:
        # Check if the file is a JPG file
        if file.lower().endswith(".jpg"):
            # Open the image file
            image = Image.open(os.path.join(root, file))

            # Calculate the size of the output PDF file
            pdf_size = os.path.getsize(os.path.join(root, file)) / 1024.0 / 1024.0

            # Reduce the quality of the image if necessary to keep the PDF file size below 2.0MB
            while pdf_size > 2.0:
                image.save(os.path.join(root, file), "JPEG", quality=85)
                pdf_size = os.path.getsize(os.path.join(root, file)) / 1024.0 / 1024.0

            # Save the image as a PDF file with the same name
            pdf_file_name = file.split(".")[0] + ".pdf"
            image.save(os.path.join(root, pdf_file_name), "PDF", resolution=100.0)

            print(f"{file} converted to PDF successfully!")

print("All JPG files converted to PDF successfully!")


# In[ ]:




