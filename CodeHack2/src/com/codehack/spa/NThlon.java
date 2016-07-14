package com.codehack.spa;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class NThlon {
	private static class Pair implements Comparable<Pair> {
		private int cost;
		private int here;

		public Pair(int here, int cost) {
			this.cost = cost;
			this.here = here;
		}

		@Override
		public int compareTo(Pair o) { // ASE
			if (this.cost > o.cost)
				return 1;
			else if (this.cost < o.cost)
				return -1;

			return 0;
		}
	}
	
    private static Scanner sc;
    private static final int INF_NUM = 9999999;
    private static int vNum = 402;
    static ArrayList<ArrayList<Pair>> adj = new ArrayList<ArrayList<Pair>>(410);
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
		for (int i = 0; i < vNum; i++) {
			adj.add( new ArrayList<Pair>() );
		}
        
        while(cases-- > 0) {
        	int typeNum = sc.nextInt();
        	int[] a = new int[typeNum];
        	int[] b = new int[typeNum];
        	for (int i = 0; i < typeNum; i++) {
				a[i] = sc.nextInt();
				b[i] = sc.nextInt();
			}
        	
        	int retVal = solve(a, b);
        	if( retVal < 0 )	System.out.println( "IMPOSSIBLE" );
        	else	System.out.println( retVal );
        }
	}

	
	private static int solve(int[] a, int[] b) {
		for (int i = 0; i < vNum; i++) {
			adj.get(i).clear();
		}
		
		for (int i = 0; i < a.length; i++) {
			int delta = a[i] - b[i];
			adj.get(401).add( new Pair(vertex(delta), a[i]) );
		}
		
		for (int delta = -200; delta <= 200; delta++) {
			for (int i = 0; i < a.length; i++) {
				int next = delta + a[i] - b[i];
				if( Math.abs(next) > 200 )	continue;
				adj.get( vertex(delta) ).add( new Pair(vertex(next), a[i]) );
			}
		}
		
		ArrayList<Integer> shortest = dijkstra(401);
		int ret = shortest.get( vertex(0) );
		if( ret == INF_NUM )	return -1;
		
		return ret;
	}


	private static int vertex(int delta) {
		return delta+200;
	}


	private static ArrayList<Integer> dijkstra(int src) {
		ArrayList<Integer> dist = new ArrayList<Integer>(vNum);
		for (int i = 0; i <= vNum; i++) {
			dist.add(INF_NUM);
		}
		dist.set(src, 0);

		PriorityQueue<Pair> pq = new PriorityQueue<Pair>(vNum);
		pq.add(new Pair(src, 0));

		while (!pq.isEmpty()) {
			int cost = -pq.peek().cost;
			int here = pq.poll().here;
//			System.out.println( "=====here: " + here + " cost: " + cost );
//			System.out.println( "dist.get(here): " + dist.get(here) );
			
			if (dist.get(here) < cost && cost > -1)
				continue;

			// visit edges...
			for (int i = 0; i < adj.get(here).size(); i++) {
				int there = adj.get(here).get(i).here;
				int nextDist = cost + adj.get(here).get(i).cost;
//				System.out.println( "111there: " + there + " ndist: " + nextDist );
				
				if (dist.get(there) > nextDist) {
					dist.set(there, nextDist);
					pq.add(new Pair(there, -nextDist));
				}
				
			}
		}

		return dist;
	}

}
