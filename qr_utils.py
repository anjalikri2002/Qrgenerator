import qrcode
from PIL import Image, ImageDraw
import os

def ensure_output():
    if not os.path.exists("output"):
        os.makedirs("output")


def generate_qr(data, filename="qrcode.png", color="black", bg_color="white", logo_path=None):
    ensure_output()

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=bg_color).convert("RGB")

    # Add logo if provided
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        logo = logo.resize((80, 80))
        img_w, img_h = img.size
        pos = ((img_w - 80) // 2, (img_h - 80) // 2)
        img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

    save_path = os.path.join("output", filename)
    img.save(save_path)
    return save_path
