package ca.ciccc.wmad202.challenge0.challenge0;

public class Product extends Object{
    private int id;
    private String name;
    private float price;
    private String madeInCountry;
    public Product(int id, String name, float price, String madeInCountry) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.madeInCountry = madeInCountry;
    }
    public int getId(){
        return id;
    }
    public String getMadeInCountry() {
        return madeInCountry;
    }
    public float getPrice() {
        return price;
    }
    public String getName() {
        return name;
    }
}
