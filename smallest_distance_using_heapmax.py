import heapq

points = [
    (-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)
]


def closest_points(points, k):
    print(points)

    arr = []
    distances = []

    for coordinates in points:
        x = coordinates[0]
        y = coordinates[1]
        d = (x ** 2 + y ** 2) ** 1/2

        coordinates_with_distance = {
            "coordinates": tuple((x, y)),
            "distance": d
        }
        arr.append(coordinates_with_distance)
        distances.append(d)
    print(arr)

    k_distances = distances[:k]
    print(k_distances)
    heapq._heapify_max(k_distances)
    print(k_distances)

    for distances_after_k in distances[k:]:
        if distances_after_k < k_distances[0]:
            k_distances[0] = distances_after_k
            heapq._heapify_max(k_distances)
    
    return k_distances


print(closest_points(points, 3))
