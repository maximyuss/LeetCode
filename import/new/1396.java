// https://leetcode.com/problems/design-underground-system
class UndergroundSystem {
    private final Map<Integer, Pair<String, Integer>> checkIns = new HashMap<>();
    private final Map<Pair<String, String>, long[]> times = new HashMap<>();

    public void checkIn(int id, String stationName, int t) {
        checkIns.put(id, new Pair<>(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        Pair<String, Integer> in = checkIns.remove(id);
        String stationStart = in.getKey();
        int dt = t - in.getValue();
        Pair<String, String> key = new Pair<>(stationStart, stationName);
        long[] stats = times.get(key);
        if (stats == null) {
            times.put(key, new long[]{dt, 1});
        } else {
            stats[0] += dt;
            stats[1] += 1;
        }
    }

    public double getAverageTime(String startStation, String endStation) {
        long[] a = times.get(new Pair<>(startStation, endStation));
        return (double) a[0] / a[1];
    }
}
