import java.util.ArrayList;
import java.util.Scanner;

public class FanMeeting {
    private static Scanner sc;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            char[] members = sc.next().toCharArray();
            char[] fans = sc.next().toCharArray();
            for (int i = 0; i < members.length; i++) {
            	System.out.println(members[i]);
			}
            
            System.out.println( hug(members, fans) );
        }
    }

	private static int hug(char[] members, char[] fans) {
		int[] number1 = new int[members.length];
		int[] number2 = new int[fans.length];
//		for (int i = 0; i < members.length; i++) {
//			number1[i] = (members[i] == 'M');
//		}
//		
//		for (int i = 0; i < fans.length; i++) {
//			number2.add( (fans[fans.length-i-1] == 'M') );
//		}
//		
		int[] result = karatsuba( number1, number2 );
		
		int allHugs = 0;
		for (int i = members.length-1; i < fans.length; i++) {
			if( result[i] == 0 )	++allHugs;
		}
		
		return allHugs;
	}

	private static int[] karatsuba(int[] number1, int[] number2) {
		int n1Len = number1.length;
		int n2Len = number2.length;
		if( n1Len < n2Len )	return karatsuba( number2, number1 );
		if( n1Len == 0 || n1Len == 0 )	return new int[0];
//		if( n1Len <=50 )	return multiply( number1, number2 );
		
		int half = n1Len / 2;
		//	z2 = a1 * b1;
		//	z1 = (a0 + a1) * (b0 + b1) - z0 - z2
		//	z0 = a0 * b0
		//	vector<int> a0(number1.begin(), number1.begin()+half);
		//	vector<int> a1(number1.begin()+half, number1.end());
		//	vector<int> b0(number2.begin(), number2.begin() + min(number2.length, half) );
		//	vector<int> b1(number2.begin() + min(number2.length, half), number2.end() );
		
		//	z2 = a1 * b1;
		//	vector<int> z2 = karatsuba( a1, b1 );
		//	z0 = a0 * b0
		//	vector<int> z0 = karatsuba( a0, b0 );
		//	z1 = (a0 + a1) * (b0 + b1) - z0 - z2
		
		int[] retVal;

//		... not completed
//		return retVal;
		return null;
	}

}
