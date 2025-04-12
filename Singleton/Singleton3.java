//use volatile
public class Singleton3 {
    private static volatile Singleton3 instance;

    private Singleton3() {}

    public static Singleton3 getInstance() {
        if (instance == null) {
            synchronized (Singleton3.class) {
                if (instance == null) {
                    instance = new Singleton3();
                }
            }
        }
        return instance;
    }

    public static void main(String[] args) {
        Singleton3 singleton = Singleton3.getInstance();
        System.out.println(singleton);
        Singleton3 singleton1 = Singleton3.getInstance();
        System.out.println(singleton1);
    }
}
