package com.codehack.heap;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class RunningMedian {
    private static Scanner sc;
	private static int listLen;
	private static int numGenMul;
	private static int numGenAdd;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();

        while(cases-- > 0) {
        	listLen = sc.nextInt();
        	numGenMul = sc.nextInt();
        	numGenAdd = sc.nextInt();
        
        	int sum = runningMedian( new RNG(numGenMul, numGenAdd) );
        	System.out.println( sum );
        }
	}

	private static int runningMedian( RNG rng ) {
		PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(listLen/2+1, new Comparator<Integer>() {	//	left
			@Override
			public int compare(Integer o1, Integer o2) {
				return o2 - o1;
			}
		});
		PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(listLen/2+1);	//	right (min, default is asc)
		int ret = 0;
		
		for (int i = 0; i < listLen; i++) {
			//	for invariant1
			if( maxHeap.size() == minHeap.size() )	{
				maxHeap.add( rng.next() );
			}
			else	{
				minHeap.add( rng.next() );
			}
			
			//	for invariant2
			if( !maxHeap.isEmpty() && !minHeap.isEmpty() &&
					maxHeap.peek() > minHeap.peek() )	{
				int left = maxHeap.poll();
				int right = minHeap.poll();
				maxHeap.add(right);
				minHeap.add(left);
			}
			
			ret = (ret + maxHeap.peek()) % 20090711;
		}

		return ret;
	}

}

class RNG	{
	private long seed;
	private long a;
	private long b;

	public RNG(int numGenMul, int numGenAdd) {
		this.seed = 1983;
		this.a = numGenMul;
		this.b = numGenAdd;
	}

	public Integer next() {
		long ret = seed;
		seed = ((seed * a) + b) % 20090711;
		return (int)ret;
	}
	
}