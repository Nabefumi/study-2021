package ca.ciccc.wmad202.assignment5.question2_7;

import java.util.ArrayList;

public class Question {
    public String name;
    public ArrayList<String> choices;
    public Question(ArrayList<String> choices) {

        this.choices = choices;
    }
    public void printQuestion() {
        System.out.println(name);

        for (String choice : choices) {
            System.out.println(choice);
        }
    }
    public void checkAnswer(String ans,Character correctAns){
        if(ans.charAt(0)==correctAns){
            System.out.println("You are correct!");
        }
        else{
            System.out.println("The answer is wrong!");
        }
    }
}
