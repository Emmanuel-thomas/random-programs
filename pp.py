import PIL.Image
import numpy


ASCII_CHARS = [ ",", " "]


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = (height / width) - .4
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    charecters = "".join([ASCII_CHARS[pixel // 128] for pixel in pixels])
    return charecters


def main(new_width=100):
    path = input(" search : ")
    try:
        image = PIL.Image.open(path)
    except Exception:
        print("invalid ")

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))
    image_array = numpy.array(ascii_image)
    print(image_array)
    for i in range(len(ascii_image)):
        print(ascii_image[i], end="")

    print()


main()