import cv2

image_path = r'sneara.jpeg'
image = cv2.imread(image_path)

if image is None:
    print(f'Error: Unable to load image from {image_path}')
else:
    height, width, channels = image.shape
    print(f'Image loaded successfully. Height: {height}, Width: {width}, Channels: {channels}')

for y in range(height):
    for x in range(width):
        b, g, r = image[y, x]
        print(f'Pixel at position ({x}, {y}) - R: {r}, G: {g}, B: {b}')