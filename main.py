from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir=r"C:\Users\USER\Pictures\Camera Roll", title='Select an Image')
#print(filename)

def add_watermark(image, wm_text):
    #creates an image object
    opened_image = Image.open(image)

    #this line of code gets the image size
    image_width, image_height = opened_image.size

    #writes on image
    write= ImageDraw.Draw(opened_image)

    #specifing a font size
    font_size = int(image_width / 11)

    #changing the font type
    font = ImageFont.truetype('arial.ttf', font_size)

    #cordinates from where we want the image
    x, y = int(image_width/2), int(image_height/2)

    #adds watermark
    write.text((x,y), wm_text, font=font, fill='#fff', stroke_width=5, stroke_fill='#222', anchor='ms')

    #show the water marked image
    opened_image.show()

add_watermark(filename, "Sammy's lib")