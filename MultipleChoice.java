package ca.ciccc.wmad202.assignment5.question2_7;

import java.util.ArrayList;
import java.util.Scanner;

public class MultipleChoice {
    public static void main() {

        String c1 = "A. Java";
        String c2 = "B. PHP";
        String c3 = "C. Python";

        ArrayList<String> choices = new ArrayList<>();
        choices.add(c1);
        choices.add(c2);
        choices.add(c3);

        Question question = new Question(choices);

        question.name = "Question1 : What are you studying now?";
        question.printQuestion();

        Scanner in = new Scanner(System.in);
        System.out.println("Enter your answer: ");
        question.checkAnswer(in.nextLine(),'A');
    }
}
