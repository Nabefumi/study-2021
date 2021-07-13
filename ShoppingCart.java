package ca.ciccc.wmad202.challenge0.challenge0;

import java.util.ArrayList;

// Scenario2(ShoppingCart)
// Properties:
// shoppingCart Has-A: registeredProduct, list of registeredProducts
// Methods:
// ShoppingCart add registeredProduct
// ShoppingCart return total price of listed products
// ShoppingCart prints all listed product's name
// Use Case:
// user can add any registered products and theirs amount
// user can get the total price depending on the amount
// user can see the product's name
public class ShoppingCart {
    private Register registeredProduct;
    private ArrayList<Register> registeredProducts;
    public ShoppingCart(Register registeredProduct) {
        this.registeredProduct = registeredProduct;
        this.registeredProducts = new ArrayList<>();
    }
    public ShoppingCart(Register registeredProduct, ArrayList<Register> registeredProducts) {
        this.registeredProduct = registeredProduct;
        this.registeredProducts = registeredProducts;
    }
    public void addRegisteredProduct(Register registeredProduct){
        registeredProducts.add(registeredProduct);
    }
    public float totalAmount(){
        float sum = 0;
        for(Register r: registeredProducts){
            sum = sum+r.getAmount()*r.getPrice();
        }
        return sum;
    }
    @Override
    public String toString(){
        String text = "----Products----\n";
        for(Register r: registeredProducts){
            String pre = "Product name: ";
            text = text + pre;
            text = text + r.getName() + "\n";
        }
        return text;
    }
    public void printProducts(){
        System.out.println("----Products----");
        for(Register r: registeredProducts){
            System.out.println("Product name: " + r.getName());
        }
    }
}
