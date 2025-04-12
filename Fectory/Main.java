public class Main {
    public static void main(String[] s) {
        MobileFactory mobileFactory = new MobileFactory();
        Mobile mobile = mobileFactory.createMobile("IPHONE");
        mobile.createMobile();
        mobile = mobileFactory.createMobile("ONEPLUS");
        mobile.createMobile();
        mobile = mobileFactory.createMobile("REALME");
        mobile.createMobile();
    }
}