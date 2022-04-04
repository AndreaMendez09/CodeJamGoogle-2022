import java.util.*;
import java.io.*;

public class Solution {
   public static void main(String[] args) {
   Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
   int t = in.nextInt(); 
    for (int i = 1; i <= t; ++i) {
        int n = in.nextInt();
        List<Integer> data = new ArrayList<Integer>();
        for(int j = 0 ; j < n ; j++){
            data.add(in.nextInt());
        }
        
        Collections.sort(data);
        int maxValue = 0;
        for(int j = 0; j < n; j++){
            if(data.get(j) > maxValue){
                maxValue++;
            }
        }
        System.out.println("Case #" + i + ": " + maxValue);
    } 
  }
}