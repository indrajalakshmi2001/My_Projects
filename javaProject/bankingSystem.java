import java.util.*;

class BankingSystem {
    public static void main(String[] args) {
        int i = 1, pin, n, dep, accbal = 500, withdraw;
        System.out.println("Welcome to SBI");
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Enter 4 digit pin:");
            pin = sc.nextInt();
            if (pin == 1010) {
                System.out.println("1. Deposit");
                System.out.println("2. Account balance");
                System.out.println("3. Withdraw");
                System.out.println("4. Exit");
                System.out.println("Enter your choice:");
                while (true) {
                    n = sc.nextInt();
                    if (n == 1) {
                        System.out.println("Enter deposit amount:");
                        dep = sc.nextInt();
                        System.out.println("Before deposit: " + accbal);
                        accbal += dep;
                        System.out.println("After deposit: " + accbal);
                        System.out.println("1. Deposit");
                        System.out.println("2. Account balance");
                        System.out.println("3. Withdraw");
                        System.out.println("4. Exit");
                        System.out.println("Enter your choice:");
                    }
                    if (n == 2) {
                        System.out.println("Account balance: " + accbal);
                        System.out.println("1. Deposit");
                        System.out.println("2. Account balance");
                        System.out.println("3. Withdraw");
                        System.out.println("4. Exit");
                        System.out.println("Enter your choice:");
                    }
                    if (n == 3) {
                        System.out.println("Enter withdraw amount:");
                        withdraw = sc.nextInt();
                        System.out.println("Before withdraw: " + accbal);
                        accbal -= withdraw;
                        System.out.println("After withdraw: " + accbal);
                        System.out.println("1. Deposit");
                        System.out.println("2. Account balance");
                        System.out.println("3. Withdraw");
                        System.out.println("4. Exit");
                        System.out.println("Enter your choice:");
                    }
                    if (n == 4) {
                        System.out.println("Thank you");
                        break;
                    }
                }
                break;
            } else {
                if (i == 3) {
                    System.out.println("Invalid pin. Contact bank.");
                    break;
                }
                System.out.println("Invalid pin");
                i++;
            }
        }
    }
}

