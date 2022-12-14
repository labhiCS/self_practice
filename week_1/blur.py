from PIL import Image, ImageFilter

before = Image.open("bridge.bmp")
after = before.Filter(ImageFilter.BoxBlur(10))
after.save ("out.bmp")