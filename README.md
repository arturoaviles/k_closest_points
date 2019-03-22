# K Closest Points

## Inspired by

__Youtube Channel:__ CS Dojo 
__Title:__ Amazon Coding Interview Question - K Closest Points to the Origin
__Url:__ https://youtu.be/eaYX0Ee0Kcg

## General Info

Used:

* Euclidean distance
* Sorted (Timsort) / Max Heap

## To time the 2 different methods

```bash
python -m cProfile file.py
```

## Possible Optimizations

1. We don't need the actual distances, just relative distances. So, skip calculating the square roots (computationally heavy). Just store the sum of squares as "distance". (In case that distance is not necessary)
2. No need to create the entire points_with_distance array/tuple and storing it. Create the max heap right away and put/replace elements into the heap as you calculate the "distances". The heap still has points and distances, but only k of them.

## Other ways of calculating distance

1. Manhattan distance (Ex. Point 1: (a,b) Point 2: (c, d), MD = |c-a|+|d-b|)