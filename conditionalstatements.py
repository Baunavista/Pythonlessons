# # if...else..statement
# votes = 4000
# if votes >=2500:
#     print("You've won the election")
#     print("You are the governor")
# else:
#     print("You've failed the election")
#     print("You are the governor")
#
# marks = 94
# if marks>80 and marks<=100:
#     print("You've an A")
# elif marks>70 and marks<81:
#     print("You've a B")
# elif marks>60 and marks<71:
#     print("You've a C")
# elif marks>50 and marks<61:
#     print("You've a D")
# elif marks>40 and marks<51:
#     print("You've an E")
# elif marks>=0 and marks<41:
#     print("You've failed")
# else:
#     print("Please enter a value between 0 and 100")
# use if else to create an atm machine that
# pops up a toast when a condition is fulfillled
# if one withdraws above 20,000 output should
#    be, "you have withdrawn above the recommended amount"
# above 10,000 "you have withdrawn below recommended amount"
# and below 10000 "You have withdrawn less"
# use users input
money_withdrawn = float(input("Please enter a withdrawal amount... "))
if money_withdrawn >=20000:
    print("You have withdrawn above the recommended amount")
elif money_withdrawn >= 10000 and money_withdrawn < 20000:
    print("You have withdrawn the recommended amount")
elif money_withdrawn >=0 and money_withdrawn < 10000:
    print("You have withdrawn less")
else:
    print("Please enter a withdrawable amount!!")
# for ..loop
# while loop