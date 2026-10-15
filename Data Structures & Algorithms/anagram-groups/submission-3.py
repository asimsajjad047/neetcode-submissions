class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for newItem in strs:
            key = tuple(sorted(newItem))

            if key not in found:
                found[key] = [newItem]
            else:
                found[key].append(newItem)
        return list(found.values())