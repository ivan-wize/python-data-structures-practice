import collections
import bisect

class TimeMap:
    def __init__(self):
        """
        Initialize the TimeMap object.
        """
        # Dictionary to store key -> list of (timestamp, value) pairs
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the value at the given timestamp.
        """
        # Append (timestamp, value) to the list corresponding to the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns the value associated with the largest timestamp_prev <= timestamp.
        If no valid timestamp exists, return "".
        """
        # If the key does not exist, return an empty string
        if key not in self.store:
            return ""

        # Get the list of (timestamp, value) pairs for the key
        values = self.store[key]

        # Use binary search to find the rightmost timestamp <= given timestamp
        idx = bisect.bisect_right(values, (timestamp, "")) - 1

        # If idx is valid, return the corresponding value
        if idx >= 0:
            return values[idx][1]
        
        # Otherwise, return ""
        return ""
