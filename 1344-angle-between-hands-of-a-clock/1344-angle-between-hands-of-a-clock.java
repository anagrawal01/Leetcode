class Solution {
    public double angleClock(int hour, int minutes) {
        double kk= Math.abs(30*hour-5.5*minutes);
        return Math.min(kk,360-kk);
    }
}