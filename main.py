print("Your Savings Calculator")
user_input = input("How much do you make per hour : ")
user_input2 = input("How many hours do you work in a day : ")

daily_income = int(user_input)*int(user_input2)
print("This is daily income : ", daily_income)

user_input3 = input("How many days do you work in a week : ")
weekly_income = int(daily_income)*int(user_input3)
print('The is weekly income : ',weekly_income)

user_input4 = input("How many days did you work in that months excluding sunday : ")
monthly_income = int(daily_income)*int(user_input4)
print('The is monthly income : ',monthly_income)

yearly_income = int(monthly_income)*12
print('Total income from your earnings this year : ',yearly_income)