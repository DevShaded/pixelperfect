import os
from PIL import Image


def compress_image(input_path, output_path, output_format, quality=85):
    try:
        with Image.open(input_path) as img:
            if img.mode == "RGBA":
                img = img.convert("RGB")

            output_path = os.path.splitext(output_path)[0] + f".{output_format}"
            img.save(output_path, optimize=True, quality=quality)
            print(f"Komprimert bilde lagret på {output_path}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Velkommen til PixelPerfekt!")
    input_path = input("Skriv inn filbanen til bildet du vil komprimere: ")

    if not os.path.isfile(input_path):
        print("Error: Filen eksisterer ikke. Sjekk filbanen og prøv igjen.")
        return

    output_path = input("Skriv inn filnavne til det komprimerte bildet (f.eks. komprimert): ")

    output_format = input("Skriv inn utdataformatet (f.eks. jpg, png): ").lower()

    quality = input("Skriv inn kvaliteten du vil komprimere bildet til (0-100, standardverdi er 85): ")
    if quality:
        try:
            quality = int(quality)
            if quality < 0 or quality > 100:
                print("Error: Kvaliteten skal være et heltall mellom 0 og 100. Prøv igjen.")
                return
        except ValueError:
            print("Error: Kvaliteten skal være et heltall mellom 0 og 100. Prøv igjen.")
            return
    else:
        quality = 85

    compress_image(input_path, output_path, output_format, quality)


if __name__ == "__main__":
    main()
