total_bill=float(input("enter total bill amount"))
amount_paid=float(input ("amount paid by the customer"))
due_amount=total_bill-amount_paid
if due_amount>0:
    print("amount still due",due_amount)
elif due_amount==0:
    print("bill fully paid")
else:
    print("extra amount paid",due_amount)

