// https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder {
    private final PriorityQueue<Integer> left = new PriorityQueue<>((a, b) -> b - a);
    private final PriorityQueue<Integer> right = new PriorityQueue<>();

    public void addNum(int num) {
        if (left.isEmpty() || num <= left.peek())
            left.offer(num);
        else
            right.offer(num);
        if (left.size() > right.size() + 1)
            right.offer(left.poll());
        else if (right.size() > left.size())
            left.offer(right.poll());
    }

    public double findMedian() {
        if (left.size() > right.size()) 
            return left.peek();
        return (left.peek() + right.peek()) / 2.0;
    }
}
