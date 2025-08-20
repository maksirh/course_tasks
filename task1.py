def check_pi_triangle(array_sides):
     sort_array = sorted(array_sides)

     if sort_array[2]**2 == sort_array[0]**2 + sort_array[1]**2:
         return True
     else:
         return False

print(check_pi_triangle([5, 3, 4]))
print(check_pi_triangle([6, 8, 10]))
print(check_pi_triangle([100, 3, 65]))
