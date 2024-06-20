#Opens the file 'story.txt' in read mode
with open("story.txt","r") as f:
    story=f.read()
#print(story)

#Empty set to store unique words
words =set()
start_of_word =-1
target_start="<"
target_end=">"

for i,char in enumerate(story):           #enumerate give access to position (i) and element (char)
    if char  == target_start:
        start_of_word=i
    if char==target_end and start_of_word !=-1:
       word=story[start_of_word : i+1]
       words.add(word)
       start_of_word =-1
#print(words)
answers = {}       #Empty dictionary to store user answers

for word in words:
    answer=input("Enter a word for "+ word +": ")
    answers[word]=answer
#print(answers)

for word in words:
    story=story.replace(word,answers[word])

print(story)

