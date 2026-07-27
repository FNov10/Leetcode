class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We choose an arbritary item in the list as our loop length
        # doesn't matter which as each item will contain the minimum prefix
        final = ""
        completed = False
        for index in range(len(strs[0])):
            if completed:
                break
            for item in strs:
                if not item:
                    completed = True
                elif index>=len(item):
                    completed=True
                elif item[index] == strs[0][index]:
                    pass
                else:
                    completed = True
            if not completed:
                final+=item[index]

        return final