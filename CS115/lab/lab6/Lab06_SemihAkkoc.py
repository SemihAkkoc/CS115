def form_sentence(in_list, number):
    new_sentence = ''
    for line in in_list:
        for word in line:
            if len(word) == int(number):
                new_sentence += word + ' '
    return new_sentence


def test_form_sentence():
    array_2d = [['This', 'is', 'lab', 'Script'],
                ['We', 'should', 'finish', 'it'],
                ['we', 'solve', 'some', 'questions']]

    # this part creates a 2d array from song.txt file
    song = []
    song_lyrics = open('song.txt', 'r')
    song_lyrics.readline()
    for line in song_lyrics:
        words = line.split()
        words[-1] = words[-1].strip()
        song.append(words)

    number = input('Enter the search number: ')

    while number:
        print('Two Dimensional List: ')

        # for line in array_2d:
        #     print(line)

        for line in song:
            print(line)

        # print('Sentence: ' + form_sentence(array_2d, number), end='\n\n\n')
        print('Sentence: ' + form_sentence(song, number), end='\n\n\n')

        number = input('Enter the search number: ')


test_form_sentence()
