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

def simple_encode(image_file, text_file):

    input_image = cv2.imread(image_file)
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2BGRA)
    width, height = input_image.shape[:2]
    image_array = input_image.reshape((width * height), 4)

    with open(text_file, "r") as input_file:
        input_text = input_file.read()

    if len(input_text) > len(image_array):
        print("[!] Image size too small. Pick a larger Image. Exiting ...")
        return

    # Encode width and height into the first 8 bytes
    binary_str_split = []
    for value in [width, height, len(input_text)]:
        binary_str = decimal_to_binary(value, 32)

        for i in range(0, 32, 2):
            binary_str_split.append(binary_str[i: i + 2])

    print(binary_str_split)

    split_index = 0
    pixel_index = 0
    for pixel in image_array[:12]:
        for i in range(4):
            binary_str = decimal_to_binary(image_array[pixel_index][i], 8)
            binary_str = binary_str[:7] + binary_str_split[split_index]

            image_array[pixel_index][i] = int(binary_str, 2)

            split_index += 1

        pixel_index += 1


    pixel_index = 12
    for character in input_text:
        ascii_str = char_to_ascii(character)
        ascii_str_split = [ascii_str[0:2], ascii_str[2:4], ascii_str[4:6], ascii_str[6:8]]

        for i in range(4):
            binary_str = decimal_to_binary(image_array[pixel_index][i], 8)
            binary_str = binary_str[:7] + ascii_str_split[i]

            image_array[pixel_index][i] = int(binary_str, 2)

        pixel_index += 1

        # if pixel_index < 2:

        #     print(ascii_str, decimal_to_binary(image_array[pixel_index - 1][3]))


    image_array = image_array.reshape(width, height, 4)

    cv2.imwrite("output.png", image_array)
    print("[+] Successfully encoded text to image")

if __name__ == "__main__":
    simple_encode("gumball.png", "input.txt")