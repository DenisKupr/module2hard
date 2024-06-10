def generate_password(num):
    result = ''
    for i in range(1, num):
        for j in range(i+1, num):
            if num % (i+j) == 0:
                result += f'{i}{j}'
    return result

for num in range(3, 21):
    print(f'{num} - {generate_password(num)}')

