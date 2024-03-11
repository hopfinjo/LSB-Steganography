from PIL import Image
import binascii

class LSB_Stenograph:


    flag = True
    while flag:
        flag = False
        # get input from user:
        inputu = input("PLease enter your string")
        print(inputu)
        if(len(inputu)>0):
            flag=False
        
        # verify input:
        # ASCII printable characters (character code 32-127)
            
        # not included in my check ??!!
        # The extended ASCII codes (character code 128-255)

        for char in inputu:
            if ord(char) >=32 and ord(char) <=127:
                flag=False;
    
    length_of_string = len(inputu)
    minimal_length_of_picture_needed = length_of_string*8 + 8 # + 8 for end of string character

    print("XXXXXXXXXXXXXXXXXXX")
    print(binascii.a2b_uu("a"))
    print("OOOOOOOOOOOOOOOOOOOOOOO")
    
  
# Python3 code to demonstrate working of
# Converting String to binary
# Using join() + ord() + format()
 

    # https://www.geeksforgeeks.org/python-convert-string-to-binary/
    
    # printing original string 
    print("The original string is : " + str(inputu))
    
    # using join() + ord() + format()
    # Converting String to binary
    res = ''.join(format(ord(i), '08b') for i in inputu)
    
    # printing result 
    print("The string after binary conversion : " + str(res))


    # Open the image file
    with Image.open('./test-images/test-images/original-test-images/1by5.bmp') as img:

        
        # Get the pixel data
        pixel_data_inhex = img.tobytes()

        bits=""

        for byte in pixel_data_inhex:
            # Convert byte from hexadecimal to bits
            bits += format(byte, 'b')

        # Print the binary data
        #print(pixel_data_inhex)
        
        #print("\n")
        print(bits)
        print("\n")
        print("And it has ",len(bits) , " length")

        # check if any ascii can be stored in it.
        # must be able to hold at least 2 asciis.  1 Ascii = 8 bits 
        if (length_of_string) > 16:
            print("YOU CAN STORE ONE INTEGER IN THIS PICTURES")
        else:
            print("YOU CAN NOT NOT NOT IT HAS LESS THAN 16 BITS")

    # convert each character of my input string into bitcode
            
    


    



# def main(): 

# if __name__ == "__main__":
#     main()
