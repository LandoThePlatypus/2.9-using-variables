# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#hehe

def is_collinear(p1, p2, p3):
     # Check if three points are collinear using the determinant method
    # The area of the triangle formed by p1, p2, and p3 is zero if collinear
    return (p2[1] - p1[1]) * (p3[0] - p1[0]) == (p3[1] - p1[1]) * (p2[0] - p1[0])

def no_three_in_line(n):
    points = [] # Initialize the list of points

    for x in range(n):
        for y in range(n):
            # Start by assuming the point is valid
            is_valid = True
            # Check this point against all pairs of existing points
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    if is_collinear(points[i], points[j], [x, y]):
                        is_valid = False # Mark as invalid if collinear
                        break
                if not is_valid:
                    break

            # If the point is valid, add it to the list
            if is_valid:
                points.append([x, y])

            # Stop if we've found n points (as required)
            if len(points) >= n:
                return points
    return points

print(no_three_in_line(3))
print(no_three_in_line(6))
print(no_three_in_line(4))