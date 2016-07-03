import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Gallery {
    private static final int UNWATCHED = 0;
	private static final int WATCHED = 1;
	private static final int INSTALLED = 2;
	
	private static Scanner sc;
    static int vertexNum = 0;
    static int edgeNum = 0;
	private static boolean[] visited = new boolean[1001];
	private static ArrayList<ArrayList<Integer>> adj;
	private static int installed = 0;
    
	public static void main(String[] args) {
        sc = new Scanner(System.in);
        int cases = sc.nextInt();
        		
        while(cases-- > 0) {
        	vertexNum = sc.nextInt();
        	edgeNum = sc.nextInt();

        	if( adj != null )	adj.clear();
        	Arrays.fill( visited, false );
        	adj = new ArrayList<ArrayList<Integer>>();
        	for (int i = 0; i < vertexNum; i++) {
				adj.add( new ArrayList<Integer>() );
			}
        	installed = 0;

			for (int j = 0; j < edgeNum; j++) {
				int u = sc.nextInt();
				int v = sc.nextInt();
				adj.get(u).add(new Integer(v));
			}
        	
//        	for (int i = 0; i < vertexNum; i++) {
//        		ArrayList<Integer> vertax = adj.get(i);
//        		for (int j = 0; j < vertax.size(); j++) {
//					System.out.print( i + " " + vertax.get(j) );
//				}
//        		System.out.println("");
//			}
        	
        	System.out.println( installCamera() );
        }
	}

	private static int installCamera() {
		installed = 0;
		Arrays.fill( visited, false );
		
		for (int i = 0; i < vertexNum; i++) {
			if( !visited[i] && (dfs(i) == UNWATCHED) )
				installed++;
		}
		
		return installed;
	}

	private static int dfs(int here) {
		visited[here] = true;
		int[] children = {0, 0, 0};
		for (int i = 0; i < adj.get(here).size(); i++) {
			int there = adj.get(here).get(i);
			if( !visited[there] )	{
				children[dfs(there)] += 1;
			}
		}
		
		if( children[UNWATCHED] > 0 )	{
			++installed;
			return INSTALLED;
		}
		
		if( children[INSTALLED] > 0 )	return WATCHED;
		
		return UNWATCHED;
	}

}
