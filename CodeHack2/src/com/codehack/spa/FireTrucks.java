package com.codehack.spa;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class FireTrucks {
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
	private static int vNum;
	private static int eNum;
	private static int fireNum;
	private static int stationNum;
	static ArrayList<ArrayList<Pair>> adj = new ArrayList<ArrayList<Pair>>();

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		int cases = sc.nextInt();

		while (cases-- > 0) {
			adj.clear();
			vNum = sc.nextInt();
			eNum = sc.nextInt();
			fireNum = sc.nextInt();
			stationNum = sc.nextInt();

			for (int i = 0; i <= vNum; i++) {
				adj.add(new ArrayList<Pair>());
			}

			for (int i = 0; i < eNum; i++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				int w = sc.nextInt();
				adj.get(u).add(new Pair(v, w));
				adj.get(v).add(new Pair(u, w));
//				adj.get(sc.nextInt()).add(new Pair(sc.nextInt(), sc.nextInt()));
			}

			ArrayList<Integer> fires = new ArrayList<Integer>(fireNum);
			for (int i = 0; i < fireNum; i++) {
				fires.add( sc.nextInt() );
			}

			for (int i = 0; i < stationNum; i++) {
				adj.get(0).add(new Pair(sc.nextInt(), 0));
			}

//			System.out.println( adj.get(6).size() );
//			System.out.println( dijkstra(0) );
			
			ArrayList<Integer> result = dijkstra(0);
			int sum = 0;
			for (int i = 0; i < fires.size(); i++) {
				sum += result.get( fires.get(i) );
			}
			System.out.println( sum );
		}
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
