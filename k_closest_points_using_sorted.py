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

        coordinates_with_distance = {
            "coordinates": tuple((x, y)),
            "distance": d
        }
        arr.append(coordinates_with_distance)
    # print(arr)

    sorted_arr = sorted(arr, key=lambda item: item['distance'])
    # Timsort n log2 n
    # print("\n\n")
    return sorted_arr[:k]


print(closest_points(points, 3))
