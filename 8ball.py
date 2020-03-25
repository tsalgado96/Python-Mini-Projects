import random

answers = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']
keep_playing = True

while keep_playing:
    input('Question: ')
    index = random.randint(0,19)
    print('Answer: ' + answers[index] + '\n')
    
    valid_input = False
    while not(valid_input):
        i = input('Would you like to ask another question? (Yes/No) ')
        if i.lower() == 'no':
            keep_playing = False
            valid_input = True
        elif i.lower() == 'yes':
            print('\n')
            keep_playing = True
            valid_input = True
        else:
            print('*NOT A VALID INPUT*\n')