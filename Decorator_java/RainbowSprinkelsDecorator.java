public class RainbowSprinkelsDecorator extends IceCreamDecorator {
    IceCream iceCream;

    RainbowSprinkelsDecorator(IceCream iceCream) {
        this.iceCream = iceCream;
    }

    @Override
    String getDescription() {

        return iceCream.getDescription() + " with Rainbow Sprinkle";
    }

    @Override
    int cost() {

        return iceCream.cost() + 20;
    }
}