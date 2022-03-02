import random
import time


def intro(name):
    time.sleep(2)
    print(f"Chris Tarrant: Welcome to the show {name}.")
    time.sleep(2)
    print(f"Chris Tarrant: {name}, I am sure you know the rules to the game but i will give you a refresher anyway.")
    time.sleep(4)
    print("Chris Tarrant: You have 3 life lines, press 1 for 50/50, 2 for ask the audience and 3 for phone a friend.")
    time.sleep(4)
    print("Chris Tarrant: Lets play Who wants to be a millionaire\n")
    time.sleep(2)


def life_line_fifty(answers, answer_dict):
    check = True
    random_removed = []
    final_key = {}
    removed = dict(answer_dict)
    for key, value in removed.items():
        if value != answers[4]:
            del answer_dict[key]
    for key in answer_dict:
        if key in removed:
            del removed[key]
    random_removed.append(random.choice(list(removed.items())))
    new_dict = dict(random_removed)
    answer_dict.update(new_dict)
    for key in sorted(answer_dict.keys()):
        final_key = f"{key}: {answer_dict[key]}"
        print(final_key)
    ans = input(f"Chris Tarrant: Can i have your final answer please: ").upper()
    while check:
        if ans not in final_key:
            ans = input("Select one of the 2 remaining options: ").upper()
        elif ans in final_key:
            return ans
        elif ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
            ans = input("Enter A, B, C or D: ").upper()
        else:
            check = False
        if ans == "2" or ans == "3":
            print("Chris Tarrant: You can only use one lifeline per question")
            ans = input("Enter A, B, C or D: ").upper()
            if ans not in answer_dict and ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
                ans = input("Enter A, B, C or D: ").upper()
        elif ans == "1":
            print("Chris Tarrant: You have used that life line already")
            ans = input("Enter A, B, C or D: ").upper()
    return ans


def life_line_audience(answers, answer_dict):
    check = True
    print("Chris Tarrant: You would like to ask the audience for help.")
    time.sleep(2)
    print(f"Chris Tarrant: Audience please help by answering the question correctly.")
    time.sleep(2)
    print("Chris Tarrant: Ok the results are in:")
    time.sleep(2)
    audience_answer = random.choice(list(open("audience_vote.txt")))
    audience_answer = audience_answer.split(",")
    print(f"A: {answers[0]} {audience_answer[0]}")
    print(f"B: {answers[1]} {audience_answer[1]}")
    print(f"C: {answers[2]} {audience_answer[2]}")
    print(f"D: {answers[3]} {audience_answer[3]}")
    time.sleep(1)
    ans = input(f"Chris Tarrant: I hope the audience have helped. What is your answer? ").upper()
    while check:
        if ans not in answer_dict and ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
            ans = input("Enter A, B, C or D: ").upper()
        elif ans in answer_dict:
            return ans
        if ans == "1" or ans == "3":
            print("Chris Tarrant: You can only use one lifeline per question")
            ans = input("Enter A, B, C or D: ").upper()
            if ans not in answer_dict and ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
                ans = input("Enter A, B, C or D: ").upper()
        elif ans == "2":
            print("Chris Tarrant: You have used that life line already")
            ans = input("Enter A, B, C or D: ").upper()
    return ans


def phone_a_friend(ques, answers, name, answer_dict):
    check = True
    print("Chris Tarrant: You would like to phone a friend.")
    friend = input("Chris Tarrant: What is the name of your friend? ").upper()
    print(f"Chris Tarrant: Ok lets call {friend} and see if he can help.")
    time.sleep(2)
    print("Ring..Ring")
    time.sleep(2)
    print("Ring..Ring")
    time.sleep(2)
    print(f"\t{friend}: Hello..")
    time.sleep(2)
    print("Chris Tarrant: Hi, it's Chris Tarrant here from who wants to be a millionaire")
    time.sleep(3)
    print(f"\t{friend}: Hi Chris")
    time.sleep(2)
    print(f"Chris Tarrant: I have {name} here needs your help. Hopefully you can help him towards the million pounds.")
    time.sleep(3)
    print(f"\tContestant: Hi {friend}, the question is :")
    time.sleep(3)
    print(f"{ques[0]}\nIs it:")
    time.sleep(4)
    print(f"A:{answers[0]}")
    time.sleep(2)
    print(f"B:{answers[1]}")
    time.sleep(2)
    print(f"C:{answers[2]}")
    time.sleep(2)
    print(f"D:{answers[3]}")
    time.sleep(4)
    friend_response = random.choice(answers[0:3])
    print(f"\t{friend}: This is a hard one, i am no expert but i think it is {friend_response}")
    time.sleep(3)
    ans = input(f"Chris Tarrant: Can i have your final answer please: ").upper()
    while check:
        if ans not in answer_dict and ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
            ans = input("Enter A, B, C or D: ").upper()
        elif ans in answer_dict:
            return ans
        if ans == "1" or ans == "2":
            print("Chris Tarrant: You can only use one lifeline per question")
            ans = input("Enter A, B, C or D: ").upper()
            if ans not in answer_dict and ans != "1" and ans != "2" and ans != "3" and len(ans) > 1:
                ans = input("Enter A, B, C or D: ").upper()
        elif ans == "3":
            print("Chris Tarrant: You have used that life line already")
            ans = input("Enter A, B, C or D: ").upper()
    return ans


def life_line_count(fifty_fifty, ask_aud, phone_friend):
    if fifty_fifty == 0 and phone_friend == 0 and ask_aud == 0:
        print(f"Your lifelines: 1.Fifty Fifty, 2.Ask the Audience, 3.Phone a Friend")
    elif fifty_fifty == 0 and phone_friend == 0:
        print("Your lifelines: 1.Fifty Fifty, 3.Phone a Friend")
    elif fifty_fifty == 0 and ask_aud == 0:
        print("Your lifelines: 1.Fifty Fifty, 2.Ask the Audience")
    elif fifty_fifty == 0:
        print("Your lifeline: 1.Fifty Fifty")
    elif phone_friend == 0 and ask_aud == 0:
        print("Your lifelines: 2.Ask the Audience, 3.Phone a Friend")
    elif phone_friend == 0:
        print("Your lifelines: 3.Phone a Friend")
    elif ask_aud == 0:
        print("Your lifelines: 2.Ask the Audience")
    else:
        print("You have no lifelines left")
