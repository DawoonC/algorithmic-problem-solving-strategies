package com.codehack.bfs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SortingGame {
	private static Scanner sc;
	private static int nums;
	private static HashMap<Integer, Integer> toSort = new HashMap<Integer, Integer>();
	private static ArrayList<HashMap<Integer, Integer>> toSortCache = new ArrayList<HashMap<Integer, Integer>>(8);

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		int cases = sc.nextInt();

		for (int i = 0; i < 8; i++) {
			toSortCache.add( toSort );
		}

		int[] numList = new int[8];
		while (cases-- > 0) {
			toSort.clear();
			nums = sc.nextInt();

			for (int i = 0; i < nums; i++) {
				numList[i] = sc.nextInt();
			}

			System.out.println( solve(numList) );
			// System.out.println( bfs(numList) );
		}
	}

	private static int solve(int[] numList) {
		toSort = toSortCache.get(nums - 1);
		if (toSort == null || toSort.size() == 0)
			precalc();

		int fixedInt = 0;
		for (int i = 0; i < nums; i++) {
			int smaller = 1;
			for (int j = 0; j < nums; j++) {
				if (numList[j] < numList[i])
					smaller++;
			}
			
			fixedInt += (smaller * (Math.pow(10, (nums-i-1))) );
		}
		

//		for (int i = 0; i < nums ; i++) {
//			fixedInt += (fixed.get(i) * (Math.pow(10, (nums-i-1))) );
//		}

//		System.out.println( "fixedInt: " + fixedInt );
		return toSort.get(fixedInt);
	}


	private static void precalc() {
//		System.out.println( "make precalc for " + nums );
		int perm = 0;
		for (int i = 1; i <= nums; i++) {
			perm += (i * (Math.pow(10, (nums-i))) );
		}
		
		Queue<Integer> queue = new LinkedList<Integer>();

		queue.add( perm );
		toSort.put( perm, 0);

		while (!queue.isEmpty()) {
			int here = queue.poll();
			int cost = toSort.get(here);
			
			StringBuffer sb = new StringBuffer();
			sb.append(here);
			String hereStr = sb.toString();
//			String hereStr = here + "";

			for (int i = 0; i < nums; i++) {
				for (int j = i + 2; j <= nums; j++) {
					int reversedHere = reverse( hereStr.toCharArray(), i, j );
					if (!toSort.containsKey(reversedHere)) {
						toSort.put(reversedHere, cost + 1);
						queue.add(reversedHere);
					}
				}
			}
		}

		toSortCache.set( nums-1, (HashMap<Integer, Integer>) toSort.clone() );
	}


	private static int reverse(char[] list, int start, int end) {
		int listSize = list.length;
		StringBuffer str = new StringBuffer();
		
		for (int i = 0; i < start; i++) {
			str.append( list[i] );
		}
		
		int idx = end-1;
		for (int i = start; i < end; i++) {
			str.append( list[idx] );
			idx--;
		}

		for (int i = end; i < listSize; i++) {
			str.append( list[i] );
		}
		
		return Integer.parseInt( str.toString() );
	}
	
	
}
