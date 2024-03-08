These images should be used for testing the workflow for embedding text. To do this, choose an image, rename it to "original.bmp", place it in the
working directory of your application, and run the text embedding workflow.

Images:

- 1 by 1.bmp
	- This image is used for testing an edge case where the image is too small to store any text.
	- No "steg.bmp" output image should be generated.

- 1 by 5.bmp
	- This image is used for testing an edge case where the image is too small to store any text.
	- No "steg.bmp" output image should be generated.

- 1 by 6.bmp
	- This image is used for testing a case where there is only enough space to store one character as well as the null terminator.
	- The test string used for this is "hi". The version of "1 by 6.bmp" provided in "steg-test-images" contains the following: "h"

- 1 by 8.bmp
	- This image is used for testing a case where the number of available bits is exactly the number of bits needed for storing the input string.
	- The test string used for this is "hi". The version of "1 by 8.bmp" provided in "steg-test-images" contains this string.

- 5 by 1.bmp
	- This image is used for testing an edge case where the image is too small to store any text.
	- No "steg.bmp" output image should be generated.

- 6 by 1.bmp
	- This image is used for testing a case where there is only enough space to store one character as well as the null terminator.
	- The test string used for this is "hi". The version of "6 by 1.bmp" provided in "steg-test-images" contains the following: "h"

- duq_logo.bmp
	- This image is used for testing a scenario in which an input string must be truncated.
	- The test string used for this is: "If you can extract this message, then it means that your implementation of LSB steganography is working."
	- The version of "duq_logo.bmp" provided in "steg-test-images" contains the following: "If you can extract this message, then it means that your implementation of LSB steganogr"

- DuquesneMcAnultyCollege.bmp
	- This image is used for testing a scenario in which only a portion of the image is used for steganography.
	- The test string used for this is: "If you can extract this message, then it means that your implementation of LSB steganography is working."
	- The version of "DuquesneMcAnultyCollege.bmp" provided in "steg-test-images" contains the following: "If you can extract this message, then it means that your implementation of LSB steganography is working."