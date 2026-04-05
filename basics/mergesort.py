def mergesort(array):
    print(f"array: {array}")

    if len(array) <= 1:
        return array

    m = len(array) // 2
    print(f"m: {m}")

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    print("Merging...")
    print(f"left: {left}")
    print(f"right: {right}")

    merged = merge(left, right)

    print(f"merged: {merged}")

    return merged


def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
    input_list = input_str.split(",")

    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError:
            print("Invalid input.")
            quit(1)

    print(f"input_list: {input_list}")
    print(f"value_list: {value_list}")

    sorted_list = mergesort(value_list)
    print(sorted_list)