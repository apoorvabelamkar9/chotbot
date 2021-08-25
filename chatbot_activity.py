from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey)', ['hey there', 'hi there',]],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    #['(.*)(location|city)?', 'Hubballi, Bengaluru'],
    ['(.*) made you?', ['Apoorva made me....']],
    ['how is the weather in your city', ['its amazing as always']],
    ['(.*)help(.*)', ['Yes, I can help you']],
    ['(.*) is  your name?', ['my name is dell']],
    ['(.*) are you ?', ['im good as always, how about you?']],
    ['im doing well', ['okay Thankyou....']],
]



chat = Chat(pairs, reflections)
chat.converse()