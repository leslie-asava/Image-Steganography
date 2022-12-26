# Image-Steganography
My implementation of steganography using Python. Works by modifying the two least significant bit of each pixel value in order to match the intended message. The resulting image looks very similar to the original making it hard to notice any change.

# What is Steganography?
Steganography is the study and practice of concealing information within objects in such a way that it deceives the viewer as if there is no information hidden within the object. Simply put, it is hiding information in plain sight, such that only the intended recipient would get to see it. 

# How is this different from cryptography?
It may immediately occur to us that this is similar to cryptography, but it is not so. In cryptography, the objective is to modify the original message in such a fashion it becomes difficult to get to the original message from the modified message. The original and modified messages are explicitly expected to look different. While in image steganography, the objective is to deceptively hide a message within another original message and thereby, modifying it. The modified message is expected to look very similar to the original message. 
