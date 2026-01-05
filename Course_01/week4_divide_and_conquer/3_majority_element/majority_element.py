def majority_element_naive(elements):
    # Base Case: If the list is empty, there is no majority
    if not elements:
        return None
    # Base Case: If there is only one element, it is the majority
    if len(elements) == 1:
        return elements[0]

    # DIVIDE: Split the array in half
    mid = len(elements) // 2
    left_side = majority_element_naive(elements[:mid])
    right_side = majority_element_naive(elements[mid:])

    # CONQUER / COMBINE
    # 1. If both halves agree, that's our candidate
    if left_side == right_side:
        return left_side

    # 2. If they disagree, count how many times each appears in the WHOLE current list
    left_count = elements.count(left_side)
    right_count = elements.count(right_side)

    # Return the one that actually holds the majority (> 50%)
    if left_count > len(elements) // 2:
        return left_side
    if right_count > len(elements) // 2:
        return right_side

    return None


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
