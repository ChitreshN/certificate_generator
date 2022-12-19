# Certificate_generator

This can be used to generate certificates automatically given a list of participants in as CSV file. It also creates a webpage for every participant hosting the certificate and the link to the website is stored in a QR code, this way we can ensure that the certificates are legitimate. It will also automatically mail all the participants their certificates.

Lines from 228 to 242 are commented.
run the code first then comment everything which was previously not and now uncomment 228 to 242. These lines are responsible for sending the mail.

The code requires us to give a template on which it will place the names and QR codes.

before executing the code run the following commands

      pip install Pillow

      pip install qrcode

On line 12 and 13 of the  code in main.py file the font  type is specified, the location of font is specified for POP OS, if using any other OS change it accordingly.

PS. I have used different certificate template for testing the code, so the position of writing will vary on the demo certificate template attached here.
