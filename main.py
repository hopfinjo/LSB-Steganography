from PIL import Image
# Open the image file
with Image.open('./test-images/test-images/original-test-images/1by5.bmp') as img:

    
    # Get the pixel data
    pixel_data_inhex = img.tobytes()

    bits=""

    for byte in pixel_data_inhex:
        # Convert byte from hexadecimal to bits
        bits += format(byte, 'b')

    # Print the binary data
    print(pixel_data_inhex)
    print("\n")
    print(bits)
    print("\n")
    print("And it has ",len(bits) , " length")
    print("that means there are bytes (packs of 8 bits)", len(bits)/8)
    print("\n")
    print()




