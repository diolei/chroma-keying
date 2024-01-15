from graphics import *

foreground = Image(Point(1, 0), input("Foreground Image: "))
background = Image(Point(1, 0), input("Background Image: "))

background_width, background_height = background.getWidth(), background.getHeight()
foreground_width, foreground_height = foreground.getWidth(), foreground.getHeight()

if background_width != foreground_width or background_height != foreground_height:
    print("Invalid image sizes")
    exit(0)

new_image = Image(Point(0, 0), background_width, background_height)

key_color_lower = (0, 100, 0)
key_color_upper = (100, 255, 100)

for x in range(foreground_width):
    for y in range(foreground_height):
        F_R, F_G, F_B = foreground.getPixel(x, y)
        B_R, B_G, B_B = background.getPixel(x, y)

        # Pixel in green range
        if (
            key_color_lower[0] <= F_R <= key_color_upper[0]
            and key_color_lower[1] <= F_G <= key_color_upper[1]
            and key_color_lower[2] <= F_B <= key_color_upper[2]
        ):
            new_image.setPixel(x, y, color_rgb(B_R, B_G, B_B))
        else:
            new_image.setPixel(x, y, color_rgb(F_R, F_G, F_B))

output_filename = input("Output Image: ")

try:
    new_image.save(output_filename)
except Exception as e:
    print(f"Error saving image: {e}")
