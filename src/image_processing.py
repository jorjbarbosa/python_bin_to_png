from PIL import Image
import numpy as np

def read_and_convert_to_png(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = np.fromfile(f, dtype=np.uint8)

    for channels in [4, 3]:
        pixels = len(data) // channels
        width = int(np.sqrt(pixels))
        height = pixels // width
        if width * height * channels == len(data):
            break

    data = data[:width * height * channels]
    data = data.reshape((height, width, channels))

    image = Image.fromarray(data, 'RGBA' if channels == 4 else 'RGB')
    image.save(output_file, 'PNG')
