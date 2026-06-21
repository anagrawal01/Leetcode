class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int res=0;
        Arrays.sort(costs);
        for(int i=0;i<costs.length;i++){
            if(costs[i]<=coins){
                res+=1;
                coins-=costs[i];
            }
            else{
                break;
            }
        }
        return res;
    }
}