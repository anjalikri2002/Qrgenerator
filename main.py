from qr_utils import generate_qr

def main():
    print("\n===== PROFESSIONAL QR CODE GENERATOR =====\n")

    text = input("Enter text/URL: ")
    filename = input("Enter filename (example: myqr.png): ")

    color = input("QR Color (default: black): ") or "black"
    bg_color = input("Background Color (default: white): ") or "white"

    include_logo = input("Add logo? (y/n): ").lower() == "y"
    logo_path = "assets/sample_logo.png" if include_logo else None

    if not filename.endswith(".png"):
        filename += ".png"

    path = generate_qr(text, filename, color, bg_color, logo_path)

    print(f"\nQR Code generated successfully: {path}\n")


if __name__ == "__main__":
    main()
