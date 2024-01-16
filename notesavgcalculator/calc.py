from visual import visual

class calc:
    def calculate():
        visual.lines()
        divider = int(input('How many notes you want to insert: '))
        visual.lines()
        notes = []
        #Put the inputs of the user to a list
        for i in range(0, divider):
            note = float(input(f'Insert your note: '))
            notes.append(note)
        visual.lines()
        avgNeed = float(input('How many points you need to be approved: '))
        visual.lines()
        #Calculate the average
        avg = sum(notes)/divider
        #Give the informations to the user
        if avg >= avgNeed:
            print(f'Your average is {avg}, and you are approved!')
        
        else:
            print(f'Your average is {avg}, and you are not approved!')
