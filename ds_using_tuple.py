zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'caemel',zoo
print('number of cages in the new zoo is', len(new_zoo))
print('all animals in new zoo zre', new_zoo)
print('animals brought from old zoo are',new_zoo[2])
print('last animal brought from old zoo is',new_zoo[2][2])
print('number of animals in the new zoo is ',len(new_zoo)-1+len(new_zoo[2]))