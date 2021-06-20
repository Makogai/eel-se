from PIL import Image
# provide path of image that you want to convert into pdf
img = Image.open(r"placeholder.png")  
imgg = img.convert("RGB")
# provide path of folder where you want to save pdf with name
imgg.save(r"img.pdf")  
print("Image is saved as img.pdf")