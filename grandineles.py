import string, random

with open("zdz.txt", "r", encoding="UTF-8") as f:
    words = f.read().split("\n")

# ismetam trumpus zodzius ir padarom viska lowercase
filtered_words = []
for word in words:
  if len(word) >=3:
    filtered_words.append(word.lower())
    

# stackoverflow
def find_neighbours(input):
    words = set(filtered_words)
    res = []
    for i, _ in enumerate(input):
        for c in string.ascii_lowercase:
            w = input[:i] + c + input[i+1:]
            if w != input and w in words:
                res.append(w)
    return res


def generate_chain(len, input):

    chain = []
    used = []
    # pridedam pirma grandineles zodi kas yra inputas
    chain.append(input)
    # used - kad nesikartotu zodziai 
    used.append(input)
    for i in range(len-1):
        res = find_neighbours(input)  
        input = random.choice(res)
        # reikia conditional kad nesikartotu zodziai, nes dbr gali kartotis
        chain.append(input)

    print(chain)

      
generate_chain(4,"titas")

