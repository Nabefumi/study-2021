package ca.ciccc.wmad202.challenge0.challenge0;

import java.util.ArrayList;

public class ApplicationDriver {
    public static void applicationDriver() {
        // Problem 0
        Product example = new Product(110, "Diet Pepsi", 2, "USA");
        // Problem 1
        Material material1 = new Material(1, "cotton");
        Material material2 = new Material(1, "satin");

        ArrayList<Material> materials = new ArrayList<>();
        materials.add(material1);
        materials.add(material2);

        ArrayList<String> ingredients = new ArrayList<>();
        ingredients.add("potato");
        ingredients.add("egg");
        ingredients.add("sugar");

        Product cloth = new Cloth(111, "Takafumi", 10, "JAPAN", materials);
        Product drink = new Drink(112, "coke", 1, "USA", false, 3);
        Product food = new Food(113, "Poutine", 5, "CANADA", 500, 2, ingredients);
        // Problem 3
        Register test1 = new Register(cloth, 3);
        Register test2 = new Register(drink, 1);
        Register test3 = new Register(food, 2);

        ShoppingCart test7 = new ShoppingCart(test1);
        test7.addRegisteredProduct(test1);
        test7.addRegisteredProduct(test2);
        test7.addRegisteredProduct(test3);

        float totalAmount4 = test7.totalAmount();
        System.out.println("Total: " + totalAmount4);
//        test7.printProducts();
        System.out.println(test7);
    }
}
