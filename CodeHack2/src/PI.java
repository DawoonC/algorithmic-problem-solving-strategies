import java.util.Arrays;
import java.util.Scanner;

/*
5 
12341234 
11111222 
12122222 
22222222 
12673939
4
2
5
2
14

모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
그 외의 경우 난이도: 10

원주율의 일부가 입력으로 주어질 때, 난이도의 합을 최소화하도록 숫자들을 3자리에서 5자리까지 끊어 읽고 싶습니다. 최소의 난이도를 계산하는 프로그램을 작성하세요.

sol) min( len(3)'s min + classify(n-3), len(4)'s min + classify(n-4), len(5)'s min + classify(n-5) )
 */
public class PI {
    private static Scanner sc;
    static final int MAX_NUM = 100;
//    static int inputSize1 = 0;
    static String inputStr = "";
    static int[][] cache = new int[MAX_NUM+1][MAX_NUM+1];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        
        while(cases-- > 0) {
        	for (int i = 0; i < cache.length; i++) {
            	Arrays.fill(cache[i], -1);
			}
        	
            System.out.println( memorize(0) );
        }
	}

	private static int memorize(int begin) {
		
		// TODO Auto-generated method stub
		return 0;
	}

}
