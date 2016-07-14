package com.codehack.spa;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class TimeTrip {
	private static class Pair {
		private int cost;
		private int here;

		public Pair(int here, int cost) {
			this.cost = cost;
			this.here = here;
		}
	}

	private static class RetVal {
		int past;
		int future;

		public RetVal(int past, int future) {
			this.past = past;
			this.future = future;
		}
	}

	private static Scanner sc;
	private static final int INF = 9999999;
	private static ArrayList<ArrayList<Pair>> adj = new ArrayList<ArrayList<Pair>>();
	private static boolean[][] worpMat;

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		int cases = sc.nextInt();

		while (cases-- > 0) {
			adj.clear();
			int numG = sc.nextInt();
			int numW = sc.nextInt();
			worpMat = new boolean[numW][numW];

			for (int i = 0; i < numW; i++) {
				adj.add(new ArrayList<Pair>());
			}

			for (int i = 0; i < numW; i++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				int d = sc.nextInt();
				worpMat[u][v] = true;
				adj.get(u).add(new Pair(v, d));
			}

			RetVal retVal = bellman2(0, 1, numW);

			if (retVal.past == INF && retVal.future == INF) {
				System.out.println("UNREACHABLE");
				continue;
			}

			String past = "";
			String future = "";

			if (retVal.past != INF)
				past = ("" + retVal.past);
			else
				past = "INFINITY";

			if (retVal.future != INF)
				future = ("" + retVal.future);
			else
				future = "INFINITY";

			System.out.println(past + " " + future);
		}
	}

	private static RetVal bellman2(int src, int target, int numW) {
		if (numW < 1)
			return new RetVal(INF, INF);

		boolean lowerInf = false;
		boolean upperInf = false;

		int[] upper = new int[numW];
		Arrays.fill(upper, INF);
		upper[src] = 0;

		int[] lower = new int[numW];
		Arrays.fill(lower, -INF);
		lower[src] = 0;

		for (int iter = 0; iter < numW - 1; iter++) {
			for (int here = 0; here < numW; here++) {
				for (int i = 0; i < adj.get(here).size(); i++) {
					int there = adj.get(here).get(i).here;
					int cost = adj.get(here).get(i).cost;

					// try relex
					upper[there] = Math.min(upper[there], upper[here] + cost);
					lower[there] = Math.max(lower[there], lower[here] + cost);
				}
			}
		}

		// check minus cycle
		for (int here = 0; here < numW; here++) {
			for (int i = 0; i < adj.get(here).size(); i++) {
				int there = adj.get(here).get(i).here;
				int cost = adj.get(here).get(i).cost;

				if (upper[here] + cost < upper[there]) {
					if (worpMat[src][here] && worpMat[here][target]) {
						upperInf = true;
					}
				}

				if (lower[here] + cost > lower[there]) {
					if (worpMat[src][here] && worpMat[here][target]) {
						lowerInf = true;
					}
				}
			}
		}

		if (upperInf) {
			return new RetVal(INF, lower[target]);
		} else {
			if (lower[target] == INF)
				return new RetVal(INF, INF); // unreachable
		}

		if (lowerInf) {
			return new RetVal(upper[target], INF);
		} else {
			if (upper[target] == INF)
				return new RetVal(INF, INF);
		}

		return new RetVal(upper[target], lower[target]);
	}

}
