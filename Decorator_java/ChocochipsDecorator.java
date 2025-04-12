public class ChocochipsDecorator extends IceCreamDecorator {
    IceCream iceCream;

    ChocochipsDecorator(IceCream iceCream) {
        this.iceCream = iceCream;
    }

    @Override
    String getDescription() {

        return iceCream.getDescription() + "with Choco Chips";
    }

    @Override
    int cost() {

        return iceCream.cost() + 15;
    }
}