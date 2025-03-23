# You’re working on automation for validating power-related logs from battery tests. 
# You receive a list of log entries captured during a device test session. 
# Each entry is a dictionary with a timestamp and a power_state, such as "charging", "discharging", "idle", or "error".
# Write a Python function that:
#     Scans the logs and identifies any entries with invalid or unexpected power_state values.
#     Returns a list of all such invalid entries (the full dictionary for each).
# Assume valid states are: "charging", "discharging", "idle"

class Solution(object):
    def findInvalidPowerStates(self, logs):
        """
        :type logs: List[Dict[str, str]]
        :rtype: List[Dict[str, str]]
        """

        # Define valid power states
        valid_states = {"charging", "discharging", "idle"}

        # Collect invalid entries
        invalid_entries = []
        for entry in logs:
            state = entry.get("power_state", "")
            if state not in valid_states:
                invalid_entries.append(entry)

        return invalid_entries

# Time Complexity: O(n)
#     We iterate through each log entry once, where n is the number of logs.
# Space Complexity: O(k)
#     k is the number of invalid entries. In the worst case, k = n.

sol = Solution()

# Test Case 1: Mixed valid/invalid states
logs = [
    {"timestamp": "2025-03-22T10:00:00Z", "power_state": "charging"},
    {"timestamp": "2025-03-22T10:01:00Z", "power_state": "discharging"},
    {"timestamp": "2025-03-22T10:02:00Z", "power_state": "suspended"},
    {"timestamp": "2025-03-22T10:03:00Z", "power_state": "idle"},
    {"timestamp": "2025-03-22T10:04:00Z", "power_state": "unknown"},
]
print(sol.findInvalidPowerStates(logs))
# Expected: Entries with "suspended" and "unknown"

# Test Case 2: All valid
logs = [
    {"timestamp": "2025-03-22T10:00:00Z", "power_state": "charging"},
    {"timestamp": "2025-03-22T10:01:00Z", "power_state": "idle"},
]
print(sol.findInvalidPowerStates(logs))
# Expected: []

# Test Case 3: All invalid
logs = [
    {"timestamp": "2025-03-22T10:00:00Z", "power_state": "failure"},
    {"timestamp": "2025-03-22T10:01:00Z", "power_state": "unknown"},
]
print(sol.findInvalidPowerStates(logs))
# Expected: All entries

# Test Case 4: Missing power_state field
logs = [
    {"timestamp": "2025-03-22T10:00:00Z"},
    {"timestamp": "2025-03-22T10:01:00Z", "power_state": "charging"}
]
print(sol.findInvalidPowerStates(logs))
# Expected: One entry without power_state
