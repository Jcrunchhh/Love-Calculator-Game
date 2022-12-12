print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

both_names = lowercase_name1 + lowercase_name2

# for TRUE
true_countt = both_names.count("t")
true_countr = both_names.count("r")
true_countu = both_names.count("u")
true_counte = both_names.count("e")

# for LOVE
love_countl = both_names.count("l")
love_counto = both_names.count("o")
love_countv = both_names.count("v")
love_counte = both_names.count("e")

# total scores
true_score = str(true_countt + true_countr + true_countu + true_counte)
love_score = str(love_countl + love_counto + love_countv + love_counte)

score = int(true_score + love_score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
