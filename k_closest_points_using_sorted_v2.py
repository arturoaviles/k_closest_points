points = [
    (-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)
] * 2000000


def closest_points(points, k):
    # print(points)

    arr = [tuple(((coordinates[0] ** 2 + coordinates[1] ** 2) ** 1/2, coordinates[0], coordinates[1]))
           for coordinates in points]
    # print(arr)

    sorted_arr = sorted(arr, key=lambda tup: tup[0])
    # Timsort n log2 n
    # print("\n\n")
    return sorted_arr[:k]


print(closest_points(points, 3))
