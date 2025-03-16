import java.util.Scanner;

public class ExpenseTracker {
	public static void main(String[] args) {
		String[] dates = new String[50];
        	String[] descriptions = new String[50];
        	double[] amounts = new double[50];
        	int count = 0;

        	Scanner keyboard = new Scanner(System.in);

        	System.out.println("WELCOME TO THE EXPENSE TRACKER APP");
		System.out.println("===========================================");

       		while (true) {

            		System.out.println("""
1. Add expense
2. View expenses
3. View total expenses
4. Exit
""");

            		int choice = keyboard.nextInt();
            		keyboard.nextLine();

            		if (choice == 1) {
                		System.out.print("Enter date (YYYY-MM-DD): ");
                		dates[count] = keyboard.nextLine();

                		System.out.print("Enter description: ");
                		descriptions[count] = keyboard.nextLine();

                		System.out.print("Enter amount: ");
                		amounts[count] = keyboard.nextDouble();

                		count++;

                		System.out.println("Expense added!");
                		System.out.println();


           
			} else if (choice == 2) {

               			if (count == 0) {
                    			System.out.println("No expenses added.");

                		} else {
                   			for (int i = 0; i < count; i++) {
                        			System.out.printf("%s, %s: #%.2f\n", dates[i], descriptions[i], amounts[i]);
                   		 	}
               			 }

            		} else if (choice == 3) {

                		if (count == 0) {
                    			System.out.println("No expenses added.");

                		} else {
                    			double total = 0;
                    			for (int i = 0; i < count; i++) {
                        			total += amounts[i];
                    			}
                    		System.out.printf("Total Expenses: $%.2f\n", total);
                		}

            		} else if (choice == 4) {

                		System.out.println("Goodbye!Exitting the App");
               	 		break;
            		}
        	}

	}
}
