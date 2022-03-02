import random
import life_line
import time

with open("questions.txt", "r") as file:
    contents = file.readlines()

print("Chris Tarrant: Welcome to who wants to be a millionaire")
time.sleep(2)
name = input("Chris Tarrant: Good evening contestant. What is your name? ").title()

fifty_fifty = 0
ask_aud = 0
phone_friend = 0
winnings = ['£100', '£200', '£300', '£500', '£1000', '£2000', '£4000', '£8000', ' £16000', '£32000', '£64000',
            '£125000', '£250000', '£500000', '£1000000']
money = []
final_winnings = []
turns = 1

life_line.intro(name)

while turns < 16:
    life_line.life_line_count(fifty_fifty, ask_aud, phone_friend)
    ques = contents.pop(random.randint(0, len(contents) - 1)).split("[")
    answers = ques[1].split(",")
    answers = [x.rstrip('\n') for x in answers]
    print(f"Question: {turns} for {winnings[0]}. {ques[0]}\nIs it:")
    time.sleep(3)
    print(f"A:{answers[0]}")
    time.sleep(2)
    print(f"B:{answers[1]}")
    time.sleep(2)
    print(f"C:{answers[2]}")
    time.sleep(2)
    print(f"D:{answers[3]}")

    answer_dict = {
        "A": answers[0],
        "B": answers[1],
        "C": answers[2],
        "D": answers[3],
    }
    check = True
    ans = input("Enter A, B, C or D: ").upper()
    while check:
        if ans not in answer_dict and ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
            ans = input("Enter A, B, C or D: ").upper()
        else:
            check = False
    if ans == "1":
        if fifty_fifty == 0:
            ans = life_line.life_line_fifty(answers, answer_dict)
            fifty_fifty += 1
        elif fifty_fifty != 0:
            print("You have already used your lifeline")
            ans = input("Enter A, B, C or D: ").upper()
    if ans == "2":
        if ask_aud == 0:
            ans = life_line.life_line_audience(answers, answer_dict)
            ask_aud += 1
        elif ask_aud != 0:
            print("You have already used your lifeline")
            ans = input("Enter A, B, C or D: ").upper()
    if ans == "3":
        if phone_friend == 0:
            ans = life_line.phone_a_friend(ques, answers, name, answer_dict)
            phone_friend += 1
        elif phone_friend != 0:
            print("You have already used your lifeline")
            ans = input("Enter A, B, C or D: ").upper()

    if answer_dict[ans] == answers[4]:
        if turns == 5 or turns == 10:
            final_winnings.append(winnings[0])
            money = winnings.pop(0)
        else:
            money = winnings.pop(0)
        print(f"Congratulations, you are moving up the money board\n")
        if 10 < turns < 15:
            print("You are one step closer to becoming a millionaire")
        if turns == 15:
            print(f"********Congratulations********\nYou have just won £1,000,000")
            break
    else:
        print(f"I'm sorry that is not the right answer. The answer was {answers[4]}")
        if 5 <= turns <= 10 or 10 <= turns <= 14:
            print(f"But you are not leaving empty handed.\nYou are leaving with a cheque for {final_winnings[-1]}")
        break

    turns += 1
