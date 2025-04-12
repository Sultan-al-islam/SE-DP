public class ChoclateSyrupDecorator extends IceCreamDecorator {
    IceCream iceCream;

    ChoclateSyrupDecorator(IceCream iceCream) {
        this.iceCream = iceCream;
    }

    @Override
    String getDescription() {

        return iceCream.getDescription() + "with Cholate Syrup";
    }

    @Override
    int cost() {

        return iceCream.cost() + 20;
    }
}