

#задание №1
# import random

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]


# random_word = random.choice(language)
# with open('test.txt', 'w') as write_file:
#     write_file.write(random_word)

# with open('test.txt', 'r') as read_file:
#     read_file.read()


#задание №2

# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""

# with open('text.txt', 'w') as write_file:
#     write_file.write(text)
# with open('text.txt', 'r') as read_file:
#     read_file.read()

# write_file = open('text.txt', 'w')
# write_file.write(text)
# read_file = open('text.txt', 'r')
# read_file.read()


# #задание №3
# with open('text.txt', 'w') as write_file:
#     write_file.write(text)
#     with open('wikipedia.txt', 'w') as write:
#         write.write(text)


# #задание №4
# from ractengle import perimeter, square

# perimeter()
# square()

# #задание №5
# def turn_over():
#     lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
#     end_lst = lst[::-1]
#     print(end_lst)



# #задание №6
# 6) Написать функцию, которая принимает hour(час), min(минуту), sec(секунды). И
# вам нужно превратить их в секунды. Вызовите его на другом файле

# def time(hour, min, sec):
#     result_hour = hour*3600
#     result_min = min*60
#     result_sec = sec
#     print(f'Час в сек. {result_hour}, Минуты в сек. {result_min}, Секунда в сек. {result_sec}')

