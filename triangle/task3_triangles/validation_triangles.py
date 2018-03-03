def is_validation_count_data(data_triangle):
    return len(data_triangle) == 4


def is_validation_value(data_triangle):
    return (data_triangle[0].isalnum()) and \
                   float(data_triangle[1]) > 0 and \
                   float(data_triangle[2]) > 0 and \
                   float(data_triangle[3]) > 0


def is_triangle(first_side, second_side, third_side):
    return ((first_side + second_side) > third_side) and \
            ((second_side + third_side) > first_side) and \
            ((third_side + first_side) > second_side)
