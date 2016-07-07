package com.codehack.spa;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Routing {
	private static class Pair implements Comparable<Pair> {
		private double cost;
		private int here;

		public Pair(int here, double cost) {
			this.cost = cost;
			this.here = here;
		}

		@Override
		public int compareTo(Pair o) {	//	ASE
			if( this.cost > o.cost )	return 1;
			else if(this.cost < o.cost )	return -1;
			
			return 0;
		}
		
//		public int compareTo(Pair o) {	//	DSE
//			if( this.cost > o.cost )	return -1;
//			else if(this.cost < o.cost )	return 1;
//			
//			return 0;
//		}

	}

	private static final double INF_NUM = 9999999;

	private static Scanner sc;
	static ArrayList<ArrayList<Pair>> adj = new ArrayList<ArrayList<Pair>>();
	private static int comNum;
	private static int lineNum;

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		int cases = sc.nextInt();

		while (cases-- > 0) {
			adj.clear();
			comNum = sc.nextInt();
			lineNum = sc.nextInt();

			for (int i = 0; i < comNum; i++) {
				adj.add(new ArrayList<Pair>());
			}

			for (int i = 0; i < lineNum; i++) {
				adj.get(sc.nextInt()).add(new Pair(sc.nextInt(), sc.nextDouble()));
			}

			String retStr = String.format( "%.10f", dijkstra(0).get(comNum-1) );
			System.out.println( retStr );
		}
	}

	private static ArrayList<Double> dijkstra(int src) {
		ArrayList<Double> dist = new ArrayList<Double>(comNum);
		for (int i = 0; i < comNum; i++) {
			dist.add(INF_NUM);
		}
		dist.set( src, 0.0 );
		
		PriorityQueue<Pair> pq = new PriorityQueue<Pair>(comNum);
//		PriorityQueue<Pair> pq = new PriorityQueue<Pair>(comNum, Collections.reverseOrder());
//		pq.add(new Pair(src, 0));
		pq.add(new Pair(src, 1.0));

		while (!pq.isEmpty()) {
			double cost = -pq.peek().cost;
			int here = pq.poll().here;

			if (dist.get(here) < cost)
				continue;

			// visit edges...
			for (int i = 0; i < adj.get(here).size(); i++) {
				int there = adj.get(here).get(i).here;
				
//				double nextDist = cost + adj.get(here).get(i).cost;
				double nextDist = Math.abs(cost * adj.get(here).get(i).cost);

				if (dist.get(there) > nextDist) {
					dist.set(there, nextDist);
					pq.add(new Pair(there, -nextDist));
				}
			}
		}

		return dist;
	}
}
