from collections import namedtuple
from itertools import combinations
import math

Point = namedtuple('Point', 'x y')

def dist(p1, p2):
    """Calculates the Euclidean distance between two points."""
    # Using attribute access (.x, .y) for the namedtuple
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force(points):
    """Helper for the base case when there are very few points."""
    m_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            m_dist = min(m_dist, dist(points[i], points[j]))
    return m_dist

def closest_strip(strip, d):
    """The 'Combine' step: Checks the strip for pairs closer than d."""
    min_d = d
    # Step 1: Sort the strip by Y-coordinate
    strip.sort(key=lambda p: p.y)
    
    # Step 2: The 7-neighbor rule
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # If the vertical distance is already >= min_d, no point checking further
            if (strip[j].y - strip[i].y) >= min_d:
                break
            min_d = min(min_d, dist(strip[i], strip[j]))
    return min_d

def find_closest(points_sorted_x):
    """Recursive Divide and Conquer function."""
    n = len(points_sorted_x)
    
    if n <= 3:
        return brute_force(points_sorted_x)

    mid = n // 2
    mid_point = points_sorted_x[mid]
    
    # DIVIDE & CONQUER
    d_left = find_closest(points_sorted_x[:mid])
    d_right = find_closest(points_sorted_x[mid:])
    
    d = min(d_left, d_right)
    
    # COMBINE: Create the vertical strip around the mid-line
    strip = []
    for p in points_sorted_x:
        if abs(p.x - mid_point.x) < d:
            strip.append(p)
    
    return min(d, closest_strip(strip, d))

def minimum_distance(points):
    """Entry point: Sorts by X and starts the recursion."""
    points.sort(key=lambda p: p.x)
    return find_closest(points)

# --- DO NOT TOUCH THE MAIN PART BELOW (as per your grader) ---
if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # Note: Removed the extra sqrt() from your original print 
    # because the dist() function already calculates it.
    print("{0:.9f}".format(minimum_distance(input_points)))