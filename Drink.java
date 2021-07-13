package ca.ciccc.wmad202.challenge0.challenge0;

public class Drink extends Product {
    private boolean isDiet;
    private int size;
    public Drink(int id, String name, float price, String madeInCountry, boolean isDiet, int size ) {
        super(id, name, price, madeInCountry);
        this.isDiet = isDiet;
        this.size = size;
    }
    public int getSize() {
        return size;
    }
    public boolean getIsDiet(){
        return isDiet;
    }
}
