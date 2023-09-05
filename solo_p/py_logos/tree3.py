from PIL import Image, ImageDraw

# Define the canvas size and background color
canvas_size = (512, 512)
background_color = (255, 255, 255)  # White

# Create a new image with a white background
image = Image.new("RGB", canvas_size, background_color)
draw = ImageDraw.Draw(image)

# Define the tree structure using 1s and 0s
tree = [
    "00000000000000000",
    "00000000000000000",
    "00000000000000000",
    "00000000000000000",
    "00000000000100000",
    "00000000001110000",
    "00000000011111000",
    "00000000111111100",
    "00000000000000000",
    "00000000000100000",
    "00000000001110000",
    "00000000011111000",
    "00000000111111100",
    "00000001111111110",
    "00000011111111111",
    "00000000000000000",
]

# Define colors for binary digits
zero_color = (255, 255, 255)  # White
one_color = (0, 0, 0)        # Black

# Define the position and size of the tree
tree_width = len(tree[0])
tree_height = len(tree)
tree_x = (canvas_size[0] - tree_width) // 2
tree_y = (canvas_size[1] - tree_height) // 2

# Draw the tree using visible 1s and 0s
for row_index, row in enumerate(tree):
    for col_index, binary_digit in enumerate(row):
        x = tree_x + col_index
        y = tree_y + row_index
        color = one_color if binary_digit == '1' else zero_color
        draw.text((x, y), binary_digit, fill=color)

# Save the logo as an image file
image.save("binary_tree_logo_visible.png")

# Show the logo
image.show()
