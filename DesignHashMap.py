class MyHashMap(object):

    def __init__(self):
        """
        Initialize the data structure with a fixed-size bucket array.
        Each bucket will store a list of key-value pairs to handle collisions.
        """
        self.size = 1000  # Number of buckets
        self.buckets = [[] for _ in range(self.size)]  # Initialize buckets as lists

    def _hash(self, key):
        """
        Hash function to compute the index for the key.
        :type key: int
        :rtype: int
        """
        return key % self.size

    def put(self, key, value):
        """
        Insert a (key, value) pair into the HashMap. If the key already exists, update the value.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self._hash(key)  # Compute the bucket index
        bucket = self.buckets[index]
        
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value
                return
        
        # If the key is not found, append it to the bucket
        bucket.append((key, value))

    def get(self, key):
        """
        Retrieve the value associated with the key, or -1 if the key does not exist.
        :type key: int
        :rtype: int
        """
        index = self._hash(key)  # Compute the bucket index
        bucket = self.buckets[index]
        
        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v
        
        # Key not found
        return -1

    def remove(self, key):
        """
        Remove the key and its associated value if it exists.
        :type key: int
        :rtype: None
        """
        index = self._hash(key)  # Compute the bucket index
        bucket = self.buckets[index]
        
        # Search for the key and remove it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)  # Remove the key-value pair
                return

# Explanation:
#     Hash Function:
#         The _hash method computes the bucket index by taking the modulo of the key with the number of buckets (key % size).

#     Chaining Technique:
#         Each bucket is a list that stores key-value pairs.
#         When collisions occur (multiple keys map to the same index), they are stored in the same bucket.

#     Operations:
#         put: Insert the key-value pair into the appropriate bucket. If the key already exists, update its value.
#         get: Search for the key in the bucket and return its value, or -1 if the key does not exist.
#         remove: Search for the key in the bucket and remove it if found.

# Complexity Analysis:
#     Time Complexity:
#         put: Average O(1), Worst O(n) (when all keys hash to the same bucket).
#         get: Average O(1), Worst O(n).
#         remove: Average O(1), Worst O(n).
#         The average-case complexity assumes that the hash function distributes keys uniformly across buckets.

#     Space Complexity:
#         O(n), where n is the number of keys stored in the HashMap.

# Example usage
myHashMap = MyHashMap()

# Insert key-value pairs
myHashMap.put(1, 1)  # The map is now [[1,1]]
myHashMap.put(2, 2)  # The map is now [[1,1], [2,2]]

# Get values
print(myHashMap.get(1))  # Output: 1
print(myHashMap.get(3))  # Output: -1 (not found)

# Update an existing key
myHashMap.put(2, 1)  # The map is now [[1,1], [2,1]]

# Get updated value
print(myHashMap.get(2))  # Output: 1

# Remove a key
myHashMap.remove(2)  # The map is now [[1,1]]

# Attempt to get removed key
print(myHashMap.get(2))  # Output: -1 (not found)
