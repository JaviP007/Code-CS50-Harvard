import sys
from PIL import Image
from PIL import ImageOps
x=sys.argv

if len(x)<=2:
    sys.exit("Too few arguments")
elif len(x)>3:
    sys.exit("Too many arguments")
elif x[1][-4:] not in [".jpeg", ".jpg", ".png"] and x[2][-4:] not in [".jpeg", ".jpg", ".png"]:
    sys.exit("No image")
elif x[1][-4:]!=x[2][-4:]:
    sys.exit("No same format")
else:
    try:
        shirt=Image.open("shirt.png")
        size = shirt.size
        ImageOps.fit(shirt,size)
        muppet=ImageOps.fit(Image.open(x[1]), size)
        muppet.paste(shirt,mask=shirt)
        muppet.save(x[2])
    except FileNotFoundError:
        sys.exit("File not found")



