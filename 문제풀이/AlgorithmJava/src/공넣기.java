import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] cnt = new int[n];

        for (int i = 0; i < m; i++) {
            int r = sc.nextInt();
            int c = sc.nextInt();
            int num = sc.nextInt();

            for (int j = r - 1; j <= c - 1; j++) {
                cnt[j] = num;
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(cnt[i]+ " ");
        }
    }
}