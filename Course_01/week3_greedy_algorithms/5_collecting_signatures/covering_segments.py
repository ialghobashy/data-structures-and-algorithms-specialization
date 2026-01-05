from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # Sort segments by their right endpoints (end)
    segments.sort(key=lambda x: x.end)
    
    points = []
    if not segments:
        return points
        
    # Place the first point at the end of the first segment
    current_point = segments[0].end
    points.append(current_point)
    
    for s in segments:
        # If the current segment starts after our last point, 
        # it is not covered. We need a new point.
        if s.start > current_point:
            current_point = s.end
            points.append(current_point)
            
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
