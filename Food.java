package ca.ciccc.wmad202.challenge0.challenge0;

import java.util.ArrayList;

public class Food extends Product{
    private int calorie;
    private int size;
    private ArrayList<String> ingredients;
    public Food(int id, String name, float price, String madeInCountry,int calories,int size,ArrayList<String> ingredients) {
        super(id, name, price, madeInCountry);
        this.calorie=calories;
        this.size=size;
        this.ingredients=ingredients;
    }

    public int getCalorie() {
        return calorie;
    }
    public int getSize() {
        return size;
    }
}
