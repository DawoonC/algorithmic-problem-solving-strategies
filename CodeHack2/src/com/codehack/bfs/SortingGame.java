package com.codehack.bfs;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class SortingGame {
    private static Scanner sc;
	private static int nums;
	private static HashMap<ArrayList<Integer>, Integer> toSort = new HashMap<ArrayList<Integer>, Integer>();
	private static ArrayList<HashMap<ArrayList<Integer>, Integer>> toSortCache = new ArrayList<HashMap<ArrayList<Integer>, Integer>>(8);
	private static ArrayList<Integer> reversedHere = new ArrayList<Integer>();
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
      
        for (int i = 0; i < 8; i++) {
			toSortCache.add( (HashMap<ArrayList<Integer>, Integer>) toSort.clone() );
		}
        
        while(cases-- > 0) {
        	toSort.clear();
        	nums = sc.nextInt();
        	ArrayList<Integer> numList = new ArrayList<Integer>();

        	for (int i = 0; i < nums; i++) {
				numList.add( sc.nextInt() );
			}

        	System.out.println( solve(numList) );
//        	System.out.println( bfs(numList) );
        }
	}

	private static void precalc() {
//		System.out.println( "make precalc for " + nums );
		ArrayList<Integer> perm = new ArrayList<Integer>();
		for (int i = 0; i < nums; i++) {
			perm.add( i );
		}
		
		Queue<ArrayList<Integer>> queue = new LinkedList<ArrayList<Integer>>();
		
		queue.add( (ArrayList<Integer>) perm.clone() );
		toSort.put( (ArrayList<Integer>) perm.clone(), 0 );
		
		while( !queue.isEmpty() )	{
			ArrayList<Integer> here = queue.poll();
			int cost = toSort.get(here);
			
			for (int i = 0; i < nums; i++) {
				for (int j = i+2; j <= nums; j++) {
					ArrayList<Integer> hereCopy = (ArrayList<Integer>) here.clone();
					List<Integer> head = hereCopy.subList(0, i);
					List<Integer> mid = hereCopy.subList(i, j);
					List<Integer> tail = hereCopy.subList(j, nums);
					
					Collections.reverse( mid );

					reversedHere.clear();
					reversedHere.addAll( head );
					reversedHere.addAll( mid );
					reversedHere.addAll( tail );

					ArrayList<Integer> reversedHereCopy = (ArrayList<Integer>) reversedHere.clone();
					if( !toSort.containsKey(reversedHereCopy) )	{
//						System.out.println( "toSort.put: " + reversedHere + " cost: " + (cost+1) );
						toSort.put(reversedHereCopy, cost+1);
						queue.add( reversedHereCopy );
					}

					Collections.reverse( mid );
				}
			}
		}
		
		toSortCache.set( nums-1, (HashMap<ArrayList<Integer>, Integer>) toSort.clone() );
	}

	private static int solve(ArrayList<Integer> numList) {
		ArrayList<Integer> fixed = new ArrayList<Integer>();
		
		toSort = toSortCache.get( nums-1 );
    	if( toSort == null || toSort.size() == 0 )	precalc();
		
		for (int i = 0; i < nums; i++) {
			int smaller = 0;
			for (int j = 0; j < nums; j++) {
				if( numList.get(j) < numList.get(i) )	smaller++;
			}
			fixed.add( smaller );
		}
		
		return toSort.get( fixed );
	}


	private static int bfs(ArrayList<Integer> numList) {
//		ArrayList<Integer> reversedHere = new ArrayList<Integer>();
		reversedHere.clear();

		//	for stop
		ArrayList<Integer> sorted = (ArrayList<Integer>) numList.clone();
		Collections.sort( sorted );
//		System.out.println( numList );
//		System.out.println( numListClone );
//		System.out.println( sorted );
		
		Queue<ArrayList<Integer>> queue = new LinkedList<ArrayList<Integer>>();
		HashMap<ArrayList<Integer>, Integer> distance = new HashMap<ArrayList<Integer>, Integer>();
		
		distance.put( (ArrayList<Integer>) numList.clone(), 0 );
		queue.add( (ArrayList<Integer>) numList.clone() );
		
		while( !queue.isEmpty() )	{
			ArrayList<Integer> here = queue.poll();
			
//			System.out.println( "here: " + here );
//			System.out.println( "sorted: " + sorted );
			if( here.equals(sorted) )	return distance.get(here);
			int cost = distance.get(here);
			
			for (int i = 0; i < nums; i++) {
				for (int j = i+2; j <= nums; j++) {
					ArrayList<Integer> hereCopy = (ArrayList<Integer>) here.clone();
					
					List<Integer> head = hereCopy.subList(0, i);
					List<Integer> mid = hereCopy.subList(i, j);
					List<Integer> tail = hereCopy.subList(j, nums);
					
					Collections.reverse( mid );

					reversedHere.clear();
					reversedHere.addAll( head );
					reversedHere.addAll( mid );
					reversedHere.addAll( tail );

					ArrayList<Integer> reversedHereCopy = (ArrayList<Integer>) reversedHere.clone();
					if( !distance.containsKey(reversedHereCopy) )	{
//						System.out.println( "toSort.put: " + reversedHere + " cost: " + (cost+1) );
						distance.put(reversedHereCopy, cost+1);
						queue.add( reversedHereCopy );
					}

					Collections.reverse( mid );
				}
			}
			
		}
		
		return -1;
	}

}
