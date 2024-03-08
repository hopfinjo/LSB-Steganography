These images should be used for testing the workflow for extracting text. To do this, choose an image, rename it to "steg.bmp", place it in the
working directory of your application, and run the text extracting workflow.

Images:

- 1 by 6.bmp
	- A successful string extraction will return: "h"

- 1 by 8.bmp
	- A successful string extraction will return: "hi"

- 6 by 1.bmp
	- A successful string extraction will return: "h"

- duq_logo.bmp
	- A successful string extraction will return: "If you can extract this message, then it means that your implementation of LSB steganogr"

- DuquesneMcAnultyCollege.bmp
	- A successful string extraction will return: "If you can extract this message, then it means that your implementation of LSB steganography is working."

- no null term.bmp
	- This image does not have a null terminator, and thus, should display a warning to the user about the nature of the output.
	- The string returned by this image will be the following nonsense output: "ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ"