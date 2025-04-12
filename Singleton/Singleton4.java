// Bill Pugh’s Singleton
public class Singleton4 {
    private Singleton4() {
    }

    private static class SingletonHelper {
        private static final Singleton4 INSTANCE = new Singleton4();
    }

    public static Singleton4 getInstance() {
        return SingletonHelper.INSTANCE;
    }

    public static void main(String[] args) {
        Singleton4 singleton = Singleton4.getInstance();
        System.out.println(singleton);
        Singleton4 singleton1 = Singleton4.getInstance();
        System.out.println(singleton1);
    }
}
