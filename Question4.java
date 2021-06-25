package ca.ciccc.wmad202.assignment4.question4;
import java.util.Arrays;

public class Question4 {
    public static void mostFrequent() {
        System.out.println("Assignment4 - Question4 done");

        int arr[] = {1, 4, 5, 6, 1, 2, 4, 5, 6, 5};
        int n = arr.length;
        // Sort the array
        Arrays.sort(arr);

        // find the max frequency using linear
        // traversal
        int max_count = 1, res = arr[0];
        int curr_count = 1;

        for (int i = 1; i < n; i++) {
            if (arr[i] == arr[i - 1])
                curr_count++;
            else {
                if (curr_count > max_count) {
                    max_count = curr_count;
                    res = arr[i - 1];
                    System.out.println(res);
                }
                curr_count = 1;
            }
        }

        // If last element is most frequent
        if (curr_count > max_count) {
            max_count = curr_count;
            res = arr[n - 1];
            System.out.println(res);
        }
    }
}
