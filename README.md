🔐 Image-Based Steganography - Hide & Retrieve Secret Messages
A Python project for securely hiding and extracting messages inside images using steganography.

(Replace the above link with an actual image from your project)

📌 Overview
This project implements image-based steganography to hide and retrieve secret messages inside PNG images without noticeable changes. It uses pixel manipulation to embed data securely.

🔹 No password file needed – The passcode is embedded within the image itself.
🔹 Lossless encryption – Works best with PNG images to prevent data corruption.
🔹 Simple & Secure – Ensures that only authorized users can decrypt the hidden message.

🚀 Features
✅ Encrypt Messages – Hide text inside an image with a passcode.
✅ Decrypt Messages – Retrieve the hidden message using the correct passcode.
✅ Works with PNG Images – Maintains high quality and ensures data safety.
✅ Secure Passcode Protection – Ensures unauthorized users cannot decrypt the message.

⚙️ Installation & Usage
1️⃣ Install Dependencies
Ensure you have Python 3+ installed, then install required libraries:
pip install opencv-python numpy

2️⃣ Encryption (Hiding Message)
Run the encrypt.py script to hide a message inside an image:
python encrypt.py

🔹 Example Input:
Enter secret message: Hello, this is a hidden message!
Enter a passcode: mypass123
Message and passcode encrypted inside encryptedImage.png

🔹 Output:
A new encrypted image (encryptedImage.png) is created with the hidden message.

3️⃣ Decryption (Retrieving Message)
Run the decrypt.py script to extract the message:

python decrypt.py
🔹 Example Input:
Enter secret message: Hello, this is a hidden message!
Enter passcode for Decryption: mypass123
Message and passcode encrypted inside encryptedImage.png

🔹 Output:
Decryption message: Hello, this is a hidden message!
🔹 If the wrong passcode is entered:
YOU ARE NOT AUTHORIZED

📌 Why Use PNG Instead of JPG?
We use PNG images because:

PNG is lossless, so the message stays intact.
JPG compresses data, which can corrupt the hidden message.
PNG ensures safe and accurate encryption & decryption.

💡 Future Improvements
🔹 Add GUI support with vibrant colors & animations.
🔹 Implement AES encryption for extra security before embedding.
🔹 Support drag & drop images for easy use.
🔹 Convert into a web-based tool for online encryption & decryption.

📜 License
open source



