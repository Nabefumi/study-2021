package ca.ciccc.wmad202.assignment4.question6;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;

public class Question6 {
    public static void removeListNumber() {
        System.out.println("Assignment4 - Question6 done");

        ArrayList<Integer> numbersList = new ArrayList<>(Arrays.asList(1, 4, 5, 6, 1, 2, 4, 5, 6, 5));
        LinkedHashSet<Integer> hashSet = new LinkedHashSet<>(numbersList);
        ArrayList<Integer> listWithoutDuplicates = new ArrayList<>(hashSet);
        System.out.println(numbersList);
        System.out.println(hashSet);
        System.out.println(listWithoutDuplicates);

    }
}
