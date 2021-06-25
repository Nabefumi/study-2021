package ca.ciccc.wmad202.assignment4.question3;

public class Question3 {
    public void makeStar() {
        System.out.println("Assignment4 - Question3 done");

        for (int i = 0; i < 5; i ++) {
            for (int j = 0; j < -5 - i; j ++) {
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k ++){
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = 0; i < 5; i ++) {
            for (int j = 0; j < - i; j ++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 5 - i; k ++){
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = 0; i < 5; i ++) {
            for (int j = 0; j < i; j ++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 7-(i*2)-2; k ++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
