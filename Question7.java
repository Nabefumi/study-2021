package ca.ciccc.wmad202.assignment4.question7;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Question7 {
    public static int searchInputNumber() {
        System.out.println("Assignment4 - Question7 done");
        ArrayList<Integer> numbersList = new ArrayList<>(Arrays.asList(1, 4, 5, 6, 1, 2, 4, 5, 6, 5));

        //input number
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

            if(numbersList.contains(num)) {
                System.out.println(num + " You could search number");
            }
            else {
                System.out.println(num + " You could not search number");
            }
            return -1;
    }
}
