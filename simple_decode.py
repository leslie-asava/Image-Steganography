import cv2 
import numpy as np

def decimal_to_binary(number, bits):
    binary = bin(number)
    binary_str = str(binary)[2:]
    padding = "0" * (bits - len(binary_str))
    binary_str = padding + binary_str
    #print(binary_str)
    return binary_str

def char_to_ascii(char):
    decimal_ascii = ord(char)
    binary_ascii_str = decimal_to_binary(decimal_ascii, 8)
    #print(binary_ascii_str)
    return binary_ascii_str

def simple_decode(image_file):

    input_image = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)
    #input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2BGRA)
    width, height = input_image.shape[:2]
    image_array = input_image.reshape((width * height), 4)

    ascii_str = ""
    for pixel in image_array[0:12]:
        for value in pixel:
            binary_str = decimal_to_binary(value, 8)
            ascii_str += binary_str[6:8]


    w = int(ascii_str[0:32], 2)
    h = int(ascii_str[32:64], 2)
    l = int(ascii_str[64:96], 2)

    print(h,w,l)

    if (h, w) != (height, width):
        print("[!] Image not encoded")
        return

    output_text = ""

    pixel_index = 12
    for pixel in range(pixel_index,pixel_index + l):
        pixel = image_array[pixel_index]
        ascii_str = ""
        for value in pixel:
            binary_str = decimal_to_binary(value, 8)
            ascii_str += binary_str[6:8]

        ascii_decimal = int(ascii_str, 2)
        char = chr(ascii_decimal)
        output_text += char

        pixel_index += 1

    print("[+] Successfully decoded image to text")
    print(output_text)

if __name__ == "__main__":
    simple_decode("output.png")