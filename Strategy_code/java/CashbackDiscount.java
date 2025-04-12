import java.DiscountStrategy;

public class CashbackDiscount implements DiscountStrategy {
    @Override
    public void giveDiscount() {
        
        System.out.println("Cashback discount");
    }
}