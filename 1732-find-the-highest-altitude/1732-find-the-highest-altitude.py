class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt= [0]
        for i in range(0, len(gain)):
            f= alt[i]+gain[i]
            alt.append(f)
        return max(alt)