package ca.ciccc.wmad202.assignment4.question5;
import java.util.LinkedHashMap;
import java.util.Map;

public class Question5 {
    public static void countList() {
        System.out.println("Assignment4 - Question5 done");

        int list[] = {1, 4, 5, 6, 1, 2, 4, 5, 6, 5};

        Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
        for (Integer i : list) {
            Integer retrievedValue = map.get(i);
            if (null == retrievedValue) {
                map.put(i, 1);
            }
            else {
                map.put(i, retrievedValue + 1);
            }
        }
        System.out.println(map);

    }
}
