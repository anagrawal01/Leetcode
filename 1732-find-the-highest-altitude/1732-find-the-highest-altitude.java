class Solution {
    public int largestAltitude(int[] gain) {
        int ab= 0;
        int cd= 0;
        for(int i=0;i<gain.length;i++){
            cd+=gain[i];
            ab= Math.max(cd,ab);
        }
        return ab;
    }
}