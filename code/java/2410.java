// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Thread t1 = new Thread(() -> Arrays.sort(players));
        Thread t2 = new Thread(() -> Arrays.sort(trainers));
        t1.start(); t2.start();
        try {
            t1.join(); t2.join();
        } catch (InterruptedException ignored) { }
        // Arrays.parallelSort(players);
        // Arrays.parallelSort(trainers);

        int j = 0, n = players.length;
        for (int t : trainers)
            if (t >= players[j] && ++j == n)
                break;
        return j;
    }
}
