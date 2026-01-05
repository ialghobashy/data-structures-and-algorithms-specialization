from itertools import combinations


def merge_and_count(a, b):
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array
    merged = []
    inversions = 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            # a[i] > b[j], so b[j] is an inversion with a[i] 
            # and ALL elements after a[i] in the left array
            merged.append(b[j])
            inversions += (len(a) - i)
            j += 1
            
    # Append remaining elements
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, inversions

def count_inversions(a):
    def count_inversions_inner(a):
        # Base case: a single element has 0 inversions
        if len(a) <= 1:
            return a, 0
        
        mid = len(a) // 2
        left_sorted, left_inv = count_inversions_inner(a[:mid])
        right_sorted, right_inv = count_inversions_inner(a[mid:])
        
        # Merge halves and count "split" inversions
        merged_sorted, split_inv = merge_and_count(left_sorted, right_sorted)
        
        return merged_sorted, left_inv + right_inv + split_inv
    _, inversions = count_inversions_inner(a)
    return inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(count_inversions(elements))
