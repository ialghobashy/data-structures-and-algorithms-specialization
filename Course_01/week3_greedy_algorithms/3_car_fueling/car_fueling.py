from sys import stdin


def min_refills(distance, tank, stops):

    all_stops = [0] + stops + [distance]
    num_refills = 0
    current_stop = 0
    n = len(stops)

    while current_stop <= n:

        last_stop = current_stop

        while (current_stop <= n and all_stops[current_stop+1] - all_stops[last_stop] <= tank):
            current_stop += 1

        if current_stop == last_stop:
            return -1
        
        if current_stop <= n:
            num_refills += 1
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
