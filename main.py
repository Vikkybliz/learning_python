from Question import Question

# def min_num(num1, num2, num3):
#     if num1 <= num2 and num1 <= num3:
#         return num1
#     elif num2 <= num1 and num2 <= num3:
#         return num2
#     else:
#         return num3
#
#
# print(min_num(3, 3, 1))
#
# num1 = float(input('Enter a number : '))
# op = input('Enter operator : ')
# num2 = float(input('Enter second number : '))
#
# if op == '+':
#     print(num1 + num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == '*':
#     print(num1 * num2)
# elif op == '/':
#     print(num1 / num2)
# else:
#     print('Invalid operator')
#
# months = {
#     'Jan': 'January',
#     'Feb': 'February',
#     'Mar': 'March',
#     'Apr': 'April',
# }
#
# print(months['Jan'])
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print('Done')
#
# for letter in 'Vikkybliz':
#     print(letter)
#
# friends = ['Vikkybliz', 'Airblast', 'Mr. G', 'Lekzy']
# for friend in friends:
#     # print(friend)
#     for f in friend:
#         print(f)
#
# # print(pow(3, 2))

question_prompts = [
    "What language is this written in?\n (a) Dart\n (b) Java\n (c) Python\n\n ",
    "What brand is my laptop?\n (a) Asus\n (b)Acer\n (c) Hp\n\n",
    "Which is the correct spelling?\n (a)Congo\n (b)Kongo\n (c) Gongo \n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
