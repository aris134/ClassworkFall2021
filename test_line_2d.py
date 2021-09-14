
def test_find_eqn_2d_line():
    from line_2d import find_eqn_2d_line
    
    input_coords = [(1, 8), (4, 14)]
    (m, b) = find_eqn_2d_line(input_coords)
    
    assert m == 2
    assert b == 6
    
def test_find_y_from_x():
    from line_2d import find_y_from_x
    
    input_line_x = (2, 6, 8)
    y_result = find_y_from_x(input_line_x)
    
    assert y_result == 22