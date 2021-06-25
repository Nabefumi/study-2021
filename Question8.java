package ca.ciccc.wmad202.assignment4.question8;

import java.util.ArrayList;
import java.util.Scanner;

public class Question8 {
    public static void topLimit() {
        System.out.println("Assignment4 - Question8 done");

        ArrayList<Integer> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for (int i = 40; i <= 100; i ++) {
            list.add(i);
        }
        int resultNum = 0;
        for (int test : list) {
            //System.out.print(test);
            if (test % num == 0) {
                System.out.print(test);
            }
        }
    }
}
