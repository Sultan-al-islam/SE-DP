import java.DiscountStrategy;

public class CoupenDiscount implements DiscountStrategy {
    @Override
    public void giveDiscount() {

        System.out.println("Cashback");
    }
}