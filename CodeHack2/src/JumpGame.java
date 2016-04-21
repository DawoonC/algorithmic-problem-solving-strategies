import java.util.Scanner;

/*
public class JumpGame {
    private static Scanner sc;
    static int[][] matrix = new int[100][100];
    static int[][] cache = new int[100][100];
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            int size = sc.nextInt();
            
            for (int i = 0; i < size; i++) {
            	for (int j = 0; j < size; j++) {
            		matrix[i][j] = sc.nextInt();
				}
			}

            for (int i = 0; i < 100; i++) {
            	for (int j = 0; j < 100; j++) {
            		cache[i][j] = -1;
				}
			}

            if( jump(size, 0, 0) > 0 )	System.out.println("YES");
//            if( jump(cache, matrix, size, 0, 0) > 0 )	System.out.println("YES");
            else	System.out.println("NO");
        }
    }

	//	base: x == y == matrix.size return true, x > matrix.size || y > matrix.size return false
	//	induction: jump(x+matrix[x][y], y) || jump(x, y+matrix[x][y]
//	private static int jump(int[][] cache, int[][] matrix, int n, int y, int x) {
	private static int jump(int n, int y, int x) {
		if( y >= n || x >= n )	return 0;
		if( y == n-1 && x == n-1 )	return 1;
		
		if( cache[y][x] != -1 )	return cache[y][x];
		int jumpSize = matrix[y][x];
		
		cache[y][x] = jump(n, y+jumpSize, x) + jump(n, y, x+jumpSize);
//		cache[y][x] = jump(cache, matrix, n, y+jumpSize, x) + jump(cache, matrix, n, y, x+jumpSize);
		
		return cache[y][x];
	}
}
*/


public class JumpGame {
    private static Scanner sc;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            int size = sc.nextInt();
            
            int[][] matrix = new int[size][size];
            for (int i = 0; i < matrix.length; i++) {
            	for (int j = 0; j < matrix[0].length; j++) {
            		matrix[i][j] = sc.nextInt();
				}
			}
            
            int[][] cache = new int[size][size];
            for (int i = 0; i < cache.length; i++) {
            	for (int j = 0; j < cache[0].length; j++) {
            		cache[i][j] = -1;
				}
			}

            if( jump(cache, matrix, 0, 0) > 0 )	System.out.println("YES");
            else	System.out.println("NO");
        }
    }

	//	base: x == y == matrix.size return true, x > matrix.size || y > matrix.size return false
	//	induction: jump(x+matrix[x][y], y) || jump(x, y+matrix[x][y]
	private static int jump(int[][] cache, int[][] matrix, int y, int x) {
		int len = matrix.length - 1;
		if( x > len || y > len )	return 0;
		if( x == len && y == len )	return 1;
		
		if( cache[y][x] != -1 )	return cache[y][x];
		
		return cache[y][x] = jump(cache, matrix, y+matrix[y][x], x) + jump(cache, matrix, y, x+matrix[y][x]);
	}
}

