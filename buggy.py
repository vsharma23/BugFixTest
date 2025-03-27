def process_data_with_bug(data):
    """
    Processes a list of data, adding 1 to even numbers.
    Contains a bug: modifies the original list in unexpected ways.
    """
    results = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            data[i] += 1  # Modifies the original list!
        results.append(data[i])
    return results


def process_data_fixed(data):
    """
    Processes a list of data, adding 1 to even numbers.
    Fixes the bug: does not modify the original list.
    """
    data_copy = data[:]  # Create a copy of the list
    results = []
    for i in range(len(data_copy)):
        if data_copy[i] % 2 == 0:
            data_copy[i] += 1
        results.append(data_copy[i])
    return results
  
# Example Usage
my_data = [1, 2, 3, 4, 5]
processed_data = process_data_with_bug(my_data)

print("Original data:", my_data)
print("Processed data:", processed_data)

#The bug: the original list is modified as well.
#Expected : Original data: [1, 2, 3, 4, 5]
#          Processed data: [1, 3, 3, 5, 5]
#Actual: Original data: [1, 3, 3, 5, 5]
#        Processed data: [1, 3, 3, 5, 5]
