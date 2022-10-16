from pathlib import Path
images = Path("/home/roza/PycharmProjects/PoC_junior/imgs").glob("*.jpg")
image_strings = [str(p) for p in images]
print(image_strings)