
def find_eqn_2d_line(input_coords):
    # INPUT: [(x1, y1), (x2, y2)]
    # OUTPUT: m = slope, b = y-intercept
    m = (input_coords[1][[1] - input_coords[0][1]) / (input_coords[1][0] - input_coords[0][0])
    b = input_coords[0][1] - m * input_coords[0][0]
    return (m, b)
    
def find_y_from_x(m, b, x):
    # INPUT: m, b, x
    # OUTPUT: y = m*x + b
    y = m*x + b
    return y