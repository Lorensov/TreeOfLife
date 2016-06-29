from PIL import Image, ImageFilter
try:
    original = Image.open("Imagem.jpg")
    print ("The size of the Image is: ")
    print(original.format, original.size, original.mode)

    # Blur the image
    blurred = original.filter(ImageFilter.SMOOTH_MORE)
    blurred = original.filter(ImageFilter.BLUR)

    # Display both images
    original.show()
    blurred.show()

    # save the new image
    blurred.save("blurred.jpg")
except:
    print ("Unable to load image")

