from random import choice

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert',
         'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes',
          'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant',
              'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in',
               'like', 'over', 'within']
adverbs = ['Curiously', 'Extravagantly', 'Tantalizingly', 'Furiously',
           'Sensuously']

def makePoem(nouns, verbs, adjs, preps, adverbs):
    noun1 = choice(nouns)
    noun2 = choice(nouns)
    noun3 = choice(nouns)
    while (noun1 == noun2):
        noun2 = choice(nouns)
    while (noun1 == noun3 or noun2 == noun3):
        noun3 = choice(nouns)
    verb1 = choice(verbs)
    verb2 = choice(verbs)
    verb3 = choice(verbs)
    while (verb1 == verb2):
        verb2 = choice(verbs)
    while (verb1 == verb3 or verb2 == verb3):
        verb3 = choice(verbs)
    adj1 = choice(adjs)
    adj2 = choice(adjs)
    adj3 = choice(adjs)
    while (adj1 == adj2):
        adj2 = choice(adjs)
    while (adj1 == adj3 or adj2 == adj3):
        adj3 = choice(adjs)
    adverb = choice(adverbs)
    prep1 = choice(preps)
    prep2 = choice(preps)
    while (prep1 == prep2):
        prep2 = choice(preps)
    if (adj1[0] == 'a' or adj1[0] == 'e' or adj1[0] == 'i' or adj1[0] == 'o' or adj1[0] == 'u'):
        start = 'An'
    else:
        start = 'A'
    if (adj3[0] == 'a' or adj3[0] == 'e' or adj3[0] == 'i' or adj3[0] == 'o' or adj3[0] == 'u'):
        mid = 'an'
    else:
        mid = 'a'
    print(f"""
{start} {adj1} {noun1}

{start} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}.
{adverb}, the {noun1} {verb2}.
The {noun2} {verb3} {prep2} {mid} {adj3} {noun3}.""")

makePoem(nouns, verbs, adjectives, prepositions, adverbs)
          

        
    
        
        
        
            
