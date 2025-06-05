class Solution:
    def calculateMaxGain(self,nums,targetValue,k):
        maxgain = 0
        curr_sum = 0
        for i in nums:
            if i == k:
                curr_sum+= -1
            if i == targetValue:
                curr_sum+= 1
        
            if curr_sum < 0 :
                curr_sum = 0

            maxgain = max(maxgain,curr_sum)

        return maxgain

    def maxFrequency(self, nums: List[int], k: int) -> int:
        freqList = collections.Counter(nums)
        freqgain = 0
        max_target_gain = 0

        for i in freqList:
            freqgain = self.calculateMaxGain(nums,i,k)
            max_target_gain = max(max_target_gain,freqgain)

        return freqList[k] + max_target_gain
        