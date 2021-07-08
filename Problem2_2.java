package ca.ciccc.wmad202.assignment5.question2_2;

import java.util.ArrayList;

public class Problem2_2 {
    public static void main() {

        Book b = new Book();

        String s1 = "ANIMAL";
        String s2 = "anime";
        String s3 = "MOVIE";
        String s4 = "Ali";
        String s5 = "aaa";

        ArrayList<String> strings = new ArrayList<>();
        strings.add(s1);
        strings.add(s2);
        strings.add(s3);
        strings.add(s4);
        strings.add(s5);

        Page p = new Page();
        p.words.addAll(strings);

        Page p1 = new Page();
        p1.words.addAll(strings);

        Page p2 = new Page();
        p2.words.addAll(strings);

        ArrayList<Page> pages = new ArrayList<>();
        pages.add(p);
        pages.add(p1);
        pages.add(p2);

        b.pages.addAll(pages);

        System.out.println(b.searchForWords("ANIMAL"));

    }
}
