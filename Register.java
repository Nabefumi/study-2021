package ca.ciccc.wmad202.challenge0.challenge0;

public class Register {
    private Product product;
    private int amount;
    // Scenario2(Register)
// Properties:
// Register Has-A: registeredProduct, amount
// Methods:
// Register return product's amount
// Register return product's name
// Use Case:
// user can add a product and its amount
    public Register(Product product, int amount) {
        this.product = product;
        this.amount = amount;
    }
    public int getAmount() {
        return amount;
    }
    public float getPrice(){
        float price = product.getPrice();
        return price;
    }
    public String getName(){
        String name = product.getName();
        return name;
    }
}
