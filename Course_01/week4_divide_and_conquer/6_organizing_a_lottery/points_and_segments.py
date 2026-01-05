from sys import stdin


def fast_count_segments(starts, ends, points):
    # This will hold the final count for each point in its original order
    results = [0] * len(points)
    events = []

    # 1. REPRESENT SEGMENTS AS START/END EVENTS
    # Type -1: Start of segment (must come first in a tie)
    # Type  1: End of segment (must come last in a tie)
    for s in starts:
        events.append((s, -1))
    for e in ends:
        events.append((e, 1))

    # 2. REPRESENT QUERY POINTS AS EVENTS
    # Type 0: The actual point query
    # We store the original index (i) to put the answer back in the right place
    for i in range(len(points)):
        events.append((points[i], 0, i))

    # 3. SORT THE TIMELINE
    # Python sorts tuples by coordinate first, then by type (-1, 0, 1)
    events.sort()

    # 4. SWEEP THE LINE
    active_segments = 0
    for event in events:
        coordinate = event[0]
        event_type = event[1]

        if event_type == -1:
            # We entered a segment
            active_segments += 1
        elif event_type == 1:
            # We left a segment
            active_segments -= 1
        else:
            # We hit a query point! 
            # The current count of active_segments is our answer.
            original_index = event[2]
            results[original_index] = active_segments

    return results


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = fast_count_segments(input_starts, input_ends, input_points)
    print(*output_count)
