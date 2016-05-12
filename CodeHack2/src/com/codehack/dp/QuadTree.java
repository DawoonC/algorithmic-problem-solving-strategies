package com.codehack.dp;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class QuadTree {
    private static Scanner sc;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            String compImg = sc.next();
            List<Character> list = new ArrayList<Character>(compImg.length());
            for (int i = 0; i < compImg.length(); i++) {
                list.add(Character.valueOf(compImg.charAt(i)));
            }
            System.out.println( reverse(list.iterator()) );
        }
    }

	private static String reverse(Iterator<Character> iterator) {
		char head = iterator.next();
		if( head == 'b' || head == 'w' )	return String.valueOf(head);
		
		String upperLeft = reverse(iterator);
		String upperRight = reverse(iterator);
		String lowerLeft = reverse(iterator);
		String lowerRight = reverse(iterator);
		
		return "x" + lowerLeft + lowerRight + upperLeft + upperRight;
	}
}
