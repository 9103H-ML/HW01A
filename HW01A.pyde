def setup():
    # Set up canvas size, adjusted according to the given image
    # Syntax: size(width, height)
    size(870, 710)
    # Set background color using rgb, adjusted according to the given image
    background(255, 215, 0)
    # Fill in black (0 = black, 255 = white for grey scale) for the shapes
    fill(0)
    
    # Diameters of small and large dots
    diamSmall = 10
    diamLarge = 3 * diamSmall

    # Syntax: ellipse(x, y, width, height) **x, y are positions
    
    # First, draw the small circles in a completely regular grid
    for x in range(0, width, 5 * diamSmall):
        for y in range(0, height, 5 * diamSmall):
            ellipse(x, y, diamSmall, diamSmall)
    
    # Then, draw the first set of the larger circles for every other row and column
    for x in range(0, width, 2 * 5 * diamSmall):
        for y in range(0, height, 2 * 5 * diamSmall):
            ellipse(x, y, diamLarge, diamLarge)
    
    # Finally, offset the last set of larger circles by
    # one column to the right and one row down
    translate(5 * diamSmall, 5 * diamSmall)
    for x in range(0, width, 2 * 5 * diamSmall):
        for y in range(0, height, 2 * 5 * diamSmall):
            ellipse(x, y, diamLarge, diamLarge)
