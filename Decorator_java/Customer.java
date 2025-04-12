public class Customer { 
    public static void main(String[] args) { 
    IceCream iceCream = new ButtorScotchIceCream(); 
    iceCream = new ChoclateSyrupDecorator(new ChocochipsDecorator(iceCream)); 
    print(iceCream);
    
    IceCream iceCream2 = new ChoclateIceCream();
    iceCream2 = new RainbowSprinkelsDecorator(new ChocochipsDecorator(iceCream2));
    print(iceCream2);


    } 


    static void print (IceCream iceCream){ 
    System.out.println("Desc: "+iceCream.getDescription()); 
    System.out.println("Cost: "+iceCream.cost()); 
    } 
    }
