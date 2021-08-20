//import required classes and packages
import java.util.Scanner;

//create ATMExample class to impliment the Atm functionality
public class ATM_Machine
{
    //main method starts
    public static void main(String args[])
    {
        //declare and intialize  balance, withdraw , and deposit
        int balance = 0,  withdraw , deposit;

        //create Scanner class object to get choice of user
        scanner sc = new Scanner(system.in);

        while(true)
        {
            System.out.println("ATM Machine \n");
            system.out.println("choose 1 for withdraw");
            system.out.println("choose 2 for Deposit");
            system.out.println("choose 3 for check Balance");
            system.out.println("choose 4 for EXIT\n");
            system.out.print("choose the operation: ");

            //get choice from user
            int choice = sc.next();
            switch(choice)
            {
                case 1:
                system.out.print("Enter money to be withdrawn:");

                //get  the withdrawl money from user
                withdraw = sc.nextInt();

                //check whether the balance is greater than or equal to the withdrawal amount
                if (balance >= withdraw)
                {
                    //remove the withdrawal amount from the total balance
                    balance = balance -withdraw;
                    system.out.println("Please collect your money");
                }
                else
                {
                    //show custom error message
                    system.out.println("Insufficient Balance");
                }
                system.out.println("");
                break;

                     case 2:
                     system.out.print("Enter money to be deposited:");

                     //get  deposit amount from te user
                     deposit = sc.nextInt();

                     //add the deposit amount the total balance
                     balance = balance + deposit;
                     system.out.println("Your money has been successfully deposited");
                     system.out.println("");
                     break;

                     case 3:
                     //displaying the total balance of user
                     system.out.println("Balance : "+ balance);
                     system.out.println("");
                     break;

                     case 4:
                     //exit from the menu
                     system.exit("0");
            }
        }
    }
}