class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int max =Integer.MIN_VALUE;
        for(int i=0;i<costs.length;i++){
            max=Math.max(costs[i],max);
        }
        int count[] =new int[max+1];
        for(int i=0;i<costs.length;i++){
            count[costs[i]]++;
        }
        int j=0;
        for(int i=0;i<count.length;i++){
            while(count[i]>0){
                costs[j]=i;
                j++;
                count[i]--;
            }
        }
        int res=0;
        for(int i=0;i<costs.length;i++){
            if(costs[i]<=coins){
                res++;
                coins-=costs[i];
            }
            else{
                break;
            }
        }
        return res;
    }
}