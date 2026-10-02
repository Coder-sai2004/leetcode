class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")

        parts1 = [int(part) for part in parts1]
        parts2 = [int(part) for part in parts2]
        
        len1 = len(parts1)
        len2 = len(parts2)
        difference = abs(len1 - len2)

        index1 = 0
        index2 = 0
        total_parts = max(len1, len2)
        
        # Make both versions equal in length
        if len1 < len2:
            parts1.extend([0] * difference)
        elif len2 < len1:
            parts2.extend([0] * difference)

        # Compare each version part
        while index2 < total_parts:
            if parts1[index1] < parts2[index2]:
                return -1
            elif parts1[index1] > parts2[index2]:
                return 1

            index1 += 1
            index2 += 1

        return 0