public class MobileFactory {
    public Mobile createMobile(String companyName) {
        if (null == companyName || companyName.isEmpty()) {
            return null;
        } else if ("IPHONE".equals(companyName)) {
            return new IPhone();
        } else if ("ONEPLUS".equals(companyName)) {
            return new OnePlusPhone();
        } else if ("REALME".equals(companyName)) {
            return new RealMe();
        } else {
            return null;
        }
    }
}

