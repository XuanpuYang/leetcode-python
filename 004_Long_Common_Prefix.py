def longestCommonPrefix(self, strs) -> str:
        if not strs:
           return ''

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]

def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare with each subsequent string
        for i in range(1, len(strs)):
            # Keep reducing the prefix until it matches the start of current string
            while prefix and not strs[i].startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
            
            # If prefix becomes empty, no common prefix exists
            if not prefix:
                break
        
        return prefix