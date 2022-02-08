# python3
import math


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    min_refills = 0
    if d <= m:
        return min_refills
    min_refills = (d // m)

    # if there are less gas stations than min_refills, return -1
    if len(stops) <= min_refills:
        return -1

    stops.append(d)
    # if the difference btn any two stations is greater than full tank distance, return -1
    for i in range(len(stops) - 1):
        if stops[i + 1] - stops[i] > m:
            return -1
    return min_refills



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
