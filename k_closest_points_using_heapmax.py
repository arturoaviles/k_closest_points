import heapq

points = [
    (-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)
] * 2000000


def closest_points(points, k):
    # print(points)

    arr = []

    for coordinates in points:
        x = coordinates[0]
        y = coordinates[1]
        d = (x ** 2 + y ** 2) ** 1/2

        target = tuple((d, x, y))
        arr.append(target)
    # print(arr)
    # O(n)

    k_distances = arr[:k]
    heapq._heapify_max(k_distances)
    # O(k)

    for distances_after_k in arr[k:]:  # O(k-n)
        if distances_after_k[0] < k_distances[0][0]:
            k_distances[0] = distances_after_k  # ->
            heapq._heapify_max(k_distances)     # O(logk)
    # O([n-k]*logk)
    # print("\n\n")
    return k_distances[::-1]


print(closest_points(points, 3))  # O(n + (n-k)*log(k))
