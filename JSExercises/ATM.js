var balance = 100;
var checkBalance = true;
var isActive = true;

if(checkBalance===true)
{
    if(isActive===true && balance>0)
    {
      console.log("Your balance is $" + balance.toFixed(2) +".");
    }
    else if (isActive===true && balance===0)
    {
      console.log("Your account is empty.");
    }
    else if (isActive===true && balance<0)
    {
      console.log("your balance is negative. please contact bank.");
    }
    else{
      console.log("Your account is no longer active.");

    }
}
else
{
    console.log("Thank you. Have a nice day!")
}