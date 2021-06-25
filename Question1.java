package ca.ciccc.wmad202.assignment4.question1;

import java.util.Scanner;

public class Question1 {
    public void main() {
        System.out.println("Assignment3 - Question1 done");

        System.out.println("Please enter a number.");
        Scanner sc = new Scanner(System.in);
        int target = sc.nextInt();

        if (target < 2) {
            System.out.println(target + " This number is not prime number. ");
        }

        for (int i = 2; i < target; i++) {
            if (target % i == 0) {
                System.out.println(target + " This number is not prime number. ");
            }
        }

        System.out.println(target + " This number is prime number. ");
    }
}
