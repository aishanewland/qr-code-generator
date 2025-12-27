# QR Code Generator 

This is a simple Python script that lets you create a customized QR code for any website URL. You can specify the version, box size, border, and colors of the QR code before saving it as an image.

---

## Features

- Generate a QR code from any website URL.  
- Customize the look with user-specified:
  - Version (1–40)
  - Box size (1–10)
  - Border size (1–10)
  - Background and fill colors (named colors or hex codes)
- Automatically saves the QR code as `myqrcode.png`.

---

## Requirements

Make sure you have **Python 3** installed, then install the required module:
pip install qrcode[pil]


---

## Usage

1. Clone or download this repository.  
2. Run the script in your terminal or IDE:
qr_code.py


3. Provide the required input values when prompted:
   - Website URL
   - QR version (1–40)
   - Box size (1–10)
   - Border size (1–10)
   - Background color
   - Fill color

4. Your generated QR code will be saved in the same directory as **`myqrcode.png`**.

---

## Example Output

A preview will look something like this (colors and size depend on your selections):

![Example QR Code](example_qr.png)

---

## Notes

- If you’re unsure which colors to use, try simple color names like `"black"` and `"white"`, or use hex codes like `#000000` and `#FFFFFF`.
- Larger version or box sizes will generate bigger QR codes.
- The image file will overwrite each time you run the script unless you rename it.

---

## License

This project is open-source under the [MIT License](LICENSE).

---

## Author

Created by **Aisha Nelwand** — a simple way to make sharing links easy!

