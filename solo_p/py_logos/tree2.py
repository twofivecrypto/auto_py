from PIL import Image, ImageDraw

# Define the canvas size and background color
canvas_size = (512, 512)
background_color = (255, 255, 255)  # White

# Create a new image with a white background
image = Image.new("RGB", canvas_size, background_color)
draw = ImageDraw.Draw(image)

# Define binary code pattern for the tree trunk
tree_trunk = "000001111100000\n000011111110000\n000111111111000\n001111111111100\n011111111111110\n"

# Define binary code pattern for the tree branches
tree_branches = "000011111110000\n000111111111000\n001111111111100\n011111111111110\n111111111111111\n"

# Define binary code pattern for the tree roots
tree_roots = "000111111111000\n001111111111100\n011111111111110\n"

# Convert binary patterns to a list of rows
trunk_rows = tree_trunk.split("\n")
branches_rows = tree_branches.split("\n")
roots_rows = tree_roots.split("\n")

# Define colors for binary digits
zero_color = (255, 255, 255)  # White
one_color = (0, 0, 0)        # Black

# Define the position and size of the tree
tree_width = len(trunk_rows[0])
tree_height = len(trunk_rows) + len(branches_rows) + len(roots_rows)
tree_x = (canvas_size[0] - tree_width) // 2
tree_y = (canvas_size[1] - tree_height) // 2

# Draw the tree trunk, branches, and roots
for row_index, row in enumerate(trunk_rows + branches_rows + roots_rows):
    for col_index, binary_digit in enumerate(row):
        x = tree_x + col_index
        y = tree_y + row_index
        color = one_color if binary_digit == '1' else zero_color
        draw.point((x, y), fill=color)

# Save the logo as an image file
image.save("large_binary_tree_logo.png")

# Show the logo
image.show()