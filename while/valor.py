user_input = ''
inputs = []

while user_input.lower() != 'realizado':
    if user_input:
        inputs.append(user_input)
    user_input = input('Entre un nuevo valor o digite realizado: ')

print(inputs)

