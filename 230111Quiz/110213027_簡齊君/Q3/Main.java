// 有一個函數定義為 F(0) = 0; F(1)= 1; F(2)= 2; F(3n)=3*F(n)-1;F(3n-1)=3*F(n)+1;F(3n+1)=3*F(n);F(3n+2=3*F(n)+1;
// 請用遞迴寫出程式並計算 F(51)=?

public class Main {
    public static void main(String[] arg) {
        System.out.println("學號: 110213027, 姓名: 簡齊君");
        System.out.println("n=51, " + "ans= " + F(51));
    }

    public static int F(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else if (n % 3 == 0) {
            return 3 * F(n / 3) - 1;
        } else if (n % 3 == 1) {
            return 3 * F(n / 3) + 1;
        } else if (n % 3 == 2) {
            return 3 * F(n / 3) + 1;
        }
        return 0;
    }
}