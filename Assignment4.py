# for numbers in range(2,80):
#     if numbers > 1:
#         for i in range(2,numbers):
#             if numbers % i == 0:
#                 break
#         else:
#             print(numbers)

# code using a for loop to take 4 exam scores form 16 students and displaying the average of that score
# add = 0
# for students in range(1,17):
#     st_name = input(f'Enter student No.{students} name: ')
#     score_1 = int(input('Enter exam score 1: '))
#     score_2 = int(input('Enter exam score 2: '))
#     score_3 = int(input('Enter exam score 3: '))
#     score_4 = int(input('Enter exam score 4: '))
#     average = (score_1 + score_2 + score_3 + score_4) / 4
#     print(f'The average score of {st_name} is {average}')
#     print()
    


# add = 0
# for students in range(1,17):
#     st_name = input(f'Enter student NO.{students} name: ')
#     for score in range(1,5):
#         scores = int(input(f'Enter test score {score}: '))
#         add += scores
#     average = add / 4
#     print(f'The average score of {st_name} is {average}')
#     print()