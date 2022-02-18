from PIL import Image

print("Image to ascii art!!\n")
STRING = "Ñ@#W$9876543210?!abc;:+=-,._"

try:
    FILE_PATH = input("Enter the image file path: ")
    IM = Image.open(FILE_PATH).convert('RGB')
except:
    print("Invalid input")

WIDTH, HEIGHT = IM.size
for X in range(HEIGHT):
    for Y in range(WIDTH):
        R, G, B = IM.getpixel((Y, X))
        brightness = sum([R,G,B])/3
        num = round(brightness/9.10714285714)
        print(STRING[-num], end = "")
    print()

while True:
    pass