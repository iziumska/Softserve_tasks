#!/usr/bin/python3

"""Sorting triangles

Develop a console program that performs the output of triangles
in descending order of their area. After adding each new triangle,
the program asks if the user wants to add one more.
If the user answers "y" or "yes" (not case sensitive), the program
will ask you to enter data for one more
triangle, otherwise - prints the result to the console.

• Calculation of the area of ​​the triangle should be made according
to Heron's formula.
• Each triangle is defined by the name and lengths of its sides.
Input format (comma delimited):
<name>, <side length>, <side length>, <side length>
• The application must handle the input of floating-point numbers.
• Input must be case-insensitive, spaces, and tab.
"""

from triangle.task3_triangles.traingle import Triangle
from triangle.task3_triangles.list_triangles import List_Triangles
from triangle.task3_triangles.validation_triangles import \
    is_validation_count_data, is_validation_value, is_triangle


def main():
    answer = 'y'
    all_triangles = List_Triangles()
    while answer in('y', 'yes'):
        data_triangle = input('Enter the data in the '
                              'format:\n'
                              '"the name of the triangle", '
                              '"value of the first side",'
                              '"value of the second side ",'
                              '" value of the third side " \n - ')

        data_triangle = (data_triangle.replace(' ', '')).split(',')

        if not is_validation_count_data(data_triangle):
            print('Data for calculation  is not right. Restart and '
                  'enter again: "the name of the triangle", "value of'
                  ' the first side","value of the second side "," '
                  'value of the third side "  ')
            quit()
        try:
            if not is_validation_value(data_triangle):
                print('Calculations are impossible, numbers must '
                      'be greater than 0. Restart and enter again.')
                quit()

            name_of_triangle = str(data_triangle[0])
            first_side = float(data_triangle[1])
            second_side = float(data_triangle[2])
            third_side = float(data_triangle[3])
            if not is_triangle(first_side, second_side, third_side):
                print('The data you entered can not be a triangle.')
                quit()

        except ValueError:
            print('You entered incorrect data.Restart and enter again.')
            quit()

        triangle = Triangle(name_of_triangle, first_side,
                            second_side, third_side)
        triangle.calculation_perimeter_triangle()
        triangle.calculation_square_triangle()
        all_triangles.add_triangle9(triangle)

        answer = (input('Are we adding another triangle? ')).lower()

    all_triangles.sort_all_triangles()


if __name__ == '__main__':
    main()
