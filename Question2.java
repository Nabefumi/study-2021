package ca.ciccc.wmad202.assignment4.question2;

import java.util.Scanner;

public class Question2 {
    public void searchNextPrimeNumber() {
        System.out.println("Assignment4 - Question2 done");

        System.out.println("Please enter a number.");
        Scanner sc = new Scanner(System.in);
        int target = sc.nextInt();

        boolean isPrime = true;

        for (int i = 2; i <= target / 2; i++) {
            if (target % i == 0) {
                break;
            }
        }
        for (int newNum = target + 1; newNum <= Integer.MAX_VALUE; newNum++) {
            isPrime = true;
            for (int i = 2; i <= newNum / 2; i++) {
                if (newNum % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.println("Next prime number = " + newNum);
                break;
            }
        }
    }
}
