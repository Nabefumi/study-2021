package ca.ciccc.wmad202.challenge0.challenge0;

import java.util.ArrayList;

public class Cloth extends Product{
    private ArrayList<Material> materials;
    public Cloth(int id, String name, float price, String madeInCountry, ArrayList<Material> materials){
        super(id, name, price, madeInCountry);
        this.materials = materials;
    }
    public ArrayList<Material> getMaterials() {
        return materials;
    }
}