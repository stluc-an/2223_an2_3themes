# Generate @font-faces from font files in a given directory.
# Very basic; doesn't suppport multiple files per @font-face

from pathlib import Path
import sys

font_formats = {"ttf":"truetype", "otf":"opentype", "woff":"woff", "woff2":"woff2"}

dir = ""

# You can pass the directory in an argument
if len(sys.argv) > 1:
    dir = sys.argv[1]

# Getting all the files
files = Path(dir)

# Keeping only the font files
font_files = [file for file in files.iterdir() if file.suffix[1:].lower() in font_formats]

if len(font_files) > 1:
    font_family = ""

    # Determining the font family
    c = 0
    while c < min(len(font_files[0].stem),len(font_files[-1].stem)) and font_files[0].stem[c] == font_files[-1].stem[c]:
        font_family += font_files[0].stem[c]
        c+=1
    font_family = font_family.rstrip("-_")

    # Going through all the fonts
    for font in font_files:
        # Removing case & separator characters
        cleaname = font.stem.lower().translate({ord(i): None for i in "-_ "})

        font_weight = 400
        font_style = "normal"
        font_format = font_formats[font.suffix[1:].lower()]

        # Guessing the font-weight from the filename
        if      "heavy" in cleaname or\
                "extrablack" in cleaname or\
                "ultrablack" in cleaname:
            font_weight = 900

        elif    "black" in cleaname or \
                "extrabold" in cleaname or \
                "ultrabold" in cleaname:
            font_weight = 800

        elif    "semibold" in cleaname or \
                "demibold" in cleaname:
            font_weight = 600

        elif    "bold" in cleaname:
            font_weight = 700

        elif    "medium" in cleaname:
            font_weight = 500

        elif    "book" in cleaname or \
                "demi" in cleaname:
            font_weight = 350

        elif    "extralight" in cleaname or \
                "ultralight" in cleaname:
            font_weight = 200

        elif    "light" in cleaname:
            font_weight = 300

        elif    "thin" in cleaname or \
                "hairline" in cleaname:
            font_weight = 100

        # Guessing the font-style from the filename
        if "italic" in cleaname:
            font_style = "italic"

        font_face_template = "@font-face {{\n"\
              "\tfont-family: '{family}';\n"\
              "\tsrc: url('{filename}') format('{format}');\n"\
              "\tfont-weight: {weight};\n"\
              "\tfont-style: {style};\n"\
              "}}";

        # Just printing, up to you to redirect the output to whatever you want
        print(font_face_template.format(family=font_family, filename=font.name, format=font_format, weight=font_weight, style=font_style))

else:
    print("There's like one font file... just do it by hand!")