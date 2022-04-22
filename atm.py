class ATM:
  def __init__(self, pin, card_num):
    self.pin = pin
    self.card_num = card_num
  

  def check_bal(self):
    print("your balance is $70,000")

  def withdrawal(self, amount):
    new_amount = 70000 - amount
    print("you have withdrawan amount "+str(amount)+". Your remaining balance is "+ str(new_amount))

def main():
  card_num = input("insert card number:- ")
  pin = input("enter your pin number:- ")

  new_user = ATM(pin, card_num)

  print("choose your transaction ")
  print("1. Check your Balance        2. Withdraw any cash you have")
  activity = int(input("enter activity number:- "))

  if(activity ==1):
    new_user.check_bal()
  elif(activity == 2):
    amount = int(input("enter the amount:- "))
    new_user.withdrawal(amount)
  
  else:
     print("enter a valid number!")


if __name__ == "__main__":
  main()