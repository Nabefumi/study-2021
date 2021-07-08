package ca.ciccc.wmad202.assignment5.question2_2;

import java.util.ArrayList;

public class Book {
    public ArrayList<Page> pages = new ArrayList<>();

    public int searchForWords(String word) {
        int count = 0;
        for (int i = 0; i < pages.size(); i++) {
            for (int j = 0; j < pages.get(i).words.size(); j++){
                if (pages.get(i).words.get(j).equals(word)) {
                    count++;
                }

            }
        }
        return count;
    }
}
