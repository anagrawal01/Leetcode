class Solution {
    public int[] leftRightDifference(int[] nums) {
        int[] leftsum= new int[nums.length];
        int[] rightsum= new int[nums.length];
        int[] answer= new int[nums.length];
        int count=0;
        for(int i=0; i<nums.length; i++){
            leftsum[i]=count;
            count+=nums[i];
        }
        count=0;
        for(int j=nums.length-1; j>=0; j--){
            rightsum[j]=count;
            count+=nums[j];
        }
        for(int p=0; p<nums.length; p++){
            answer[p]= Math.abs(leftsum[p]-rightsum[p]); 
        }
        return answer;
    }
}