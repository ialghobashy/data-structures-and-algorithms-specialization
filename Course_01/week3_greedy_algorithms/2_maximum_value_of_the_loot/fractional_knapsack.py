from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    i = 0
    values_weights = sorted([[val/we, we] for val, we in zip(values, weights)], reverse=True)
    while capacity != 0 and i< len(values):
        if values_weights[i][1] <= capacity:
            value += values_weights[i][1] * values_weights[i][0]
            capacity -= values_weights[i][1]
        else:
            value += capacity * values_weights[i][0]
            capacity -= capacity
        i += 1 
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
