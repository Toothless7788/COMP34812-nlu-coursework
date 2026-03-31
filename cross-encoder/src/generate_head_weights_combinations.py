from itertools import product

weights = [0.0, 0.25, 0.5, 0.75, 1.0]

valid_weights = [
    w for w in product(weights, repeat=3)
    if abs(sum(w) - 1.0) < 1e-6
]


if __name__ == "__main__":
    print(f"valid_weights: {valid_weights}")
