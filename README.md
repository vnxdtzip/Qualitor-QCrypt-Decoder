# Qualitor-QCrypt-Decoder
Simple qcrypt decoder for Qualitor Software.

At some point I did a pentest on a web software called Qualitor. After fixing some of the vulnerabilities, they added a type of encryption to the GET and POST parameters.

This made it very difficult to perform new exploits since I didn't know the content of the requests. After analyzing it more deeply, I understood how the "encryption" worked and I wrote a script to encode and decode this information.

## Decoder

![image](https://github.com/user-attachments/assets/660917e3-ef01-485a-8342-5f9f7e6347f7)


## Encoder

The script for encoding was made using a javascript with the encryption function improperly exposed in the Qualitor software itself (wtf?). Based on it, I created an HTML that allows you to encrypt the information.

You can combine encryption and decryption during pentests and research on the software.

![image](https://github.com/user-attachments/assets/0d542b55-f8bb-4e34-9e60-e2713da19a57)
