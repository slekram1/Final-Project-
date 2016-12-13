def main():
	import pkg_resources
	import string
	import re
	import math
	import operator 

	exclude = list(string.punctuation)

	oldprez = ["Bill Clinton.txt", "FDR.txt", "George W Bush.txt", "Andrew Jackson.txt", "Thomas Jefferson.txt", 
	"JFK.txt", "Abraham Lincoln.txt", "Richard Nixon.txt", "Ronald Reagan.txt", "Teddy Rosevelt.txt"]

	sentence_rank = {
	"Bill Clinton.txt": 0,
	"FDR.txt": 0,
	"George W Bush.txt":0,
	"Andrew Jackson.txt":0,
	"Thomas Jefferson.txt":0, 
	"JFK.txt":0,
	"Abraham Lincoln.txt": 0,
	"Richard Nixon.txt": 0,
	"Ronald Reagan.txt":0,
	"Teddy Rosevelt.txt": 0,
	"User": 0}

	word_rank = {
	"Bill Clinton.txt": 0,
	"FDR.txt": 0,
	"George W Bush.txt":0,
	"Andrew Jackson.txt":0,
	"Thomas Jefferson.txt":0, 
	"JFK.txt":0,
	"Abraham Lincoln.txt": 0,
	"Richard Nixon.txt": 0,
	"Ronald Reagan.txt":0,
	"Teddy Rosevelt.txt": 0,
	"User": 0}

	vocab_rank = {
	"Bill Clinton.txt": 0,
	"FDR.txt": 0,
	"George W Bush.txt":0,
	"Andrew Jackson.txt":0,
	"Thomas Jefferson.txt":0, 
	"JFK.txt":0,
	"Abraham Lincoln.txt": 0,
	"Richard Nixon.txt": 0,
	"Ronald Reagan.txt":0,
	"Teddy Rosevelt.txt": 0,
	"User": 0}

	flesch_ranking = {
	"Bill Clinton.txt": 0,
	"FDR.txt": 0,
	"George W Bush.txt":0,
	"Andrew Jackson.txt":0,
	"Thomas Jefferson.txt":0, 
	"JFK.txt":0,
	"Abraham Lincoln.txt": 0,
	"Richard Nixon.txt": 0,
	"Ronald Reagan.txt":0,
	"Teddy Rosevelt.txt": 0,
	"User": 0}

	gunning_ranking = {
	"Bill Clinton.txt": 0,
	"FDR.txt": 0,
	"George W Bush.txt":0,
	"Andrew Jackson.txt":0,
	"Thomas Jefferson.txt":0, 
	"JFK.txt":0,
	"Abraham Lincoln.txt": 0,
	"Richard Nixon.txt": 0,
	"Ronald Reagan.txt":0,
	"Teddy Rosevelt.txt": 0,
	"User": 0}

	def wordcount(filename):
		file=open(filename, "r")
		wordcount = {}
		for word in file.read().split(" "):
			if word not in wordcount:
				wordcount[word] = 1
		else:
			wordcount[word] += 1
		#for k,v in wordcount.items():
		   # print(k, v)
		vocab_rank[str(oldprez[ticker])] = len(wordcount)

		return(len(wordcount))
	def USER_wordcount(filename):
		file=open(filename, "r")
		wordcount = {}
		for word in file.read().split(" "):
			if word not in wordcount:
				wordcount[word] = 1
		else:
			wordcount[word] += 1

		vocab_rank["User"] = len(wordcount)
		return(len(wordcount))

	def AVEsentence_length(filename):
		wordcounts = []
		with open(filename) as f:
			text = f.read()
			sentences = text.split('.')
			for sentence in sentences:
				words = sentence.split(' ')
				wordcounts.append(len(words))
		average_wordcount = sum(wordcounts)/len(wordcounts)

		sentence_rank[str(oldprez[ticker])] = average_wordcount
		return average_wordcount
	def USER_AVEsentence_length(filename):
		wordcounts = []
		with open(filename) as f:
			text = f.read()
			sentences = text.split('.')
			for sentence in sentences:
				words = sentence.split(' ')
				wordcounts.append(len(words))
		average_wordcount = sum(wordcounts)/len(wordcounts)

		#sentence_rank[str(oldprez[ticker])] = average_wordcount
		sentence_rank["User"] = average_wordcount
		return average_wordcount

	def averagewordlength(filename):
		with open(filename,'r') as f:
			w = [len(word) for line in f for word in line.rstrip().split(" ")]
			w_avg = sum(w)/len(w)

		word_rank[str(oldprez[ticker])] = w_avg
		return w_avg
	def USER_averagewordlength(filename):
		with open(filename,'r') as f:
			w = [len(word) for line in f for word in line.rstrip().split(" ")]
			w_avg = sum(w)/len(w)

		word_rank["User"] = w_avg
		return w_avg	

	def flesch_score(filename):
		def flesch_reading_ease(text):
				ASL = avg_sentence_length(text)
				ASW = avg_syllables_per_word(text)
				FRE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW)
				return round(FRE, 2)

		file = open(filename, 'r')
		new_str = file.read()
		score = flesch_reading_ease(new_str)

		flesch_ranking[str(oldprez[ticker])] = score
		return flesch_reading_ease(new_str)
	def USER_flesch_score(filename):
		def flesch_reading_ease(text):
				ASL = avg_sentence_length(text)
				ASW = avg_syllables_per_word(text)
				FRE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW)
				return round(FRE, 2)

		file = open(filename, 'r')
		new_str = file.read()
		score = flesch_reading_ease(new_str)

		flesch_ranking["User"] = score
		return flesch_reading_ease(new_str)

	def sentence_count(text):
		ignoreCount = 0
		sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
		for sentence in sentences:
			if lexicon_count(sentence) <= 2:
				ignoreCount = ignoreCount + 1
		return max(1, len(sentences) - ignoreCount)
	def avg_sentence_length(text):
		lc = lexicon_count(text)
		sc = sentence_count(text)
		try:
			ASL = float(lc/sc)
			return round(lc/sc, 1)
		except:
			print("Error(ASL): Sentence Count is Zero, Cannot Divide")
			return
	def avg_syllables_per_word(text):
		syllable = syllable_count(text)
		words = lexicon_count(text)
		try:
			ASPW = float(syllable)/float(words)
			return round(ASPW, 1)
		except:
			print("Error(ASyPW): Number of words are zero, cannot divide")
			return
	def syllable_count(text):
		count = 0
		vowels = 'aeiouy'
		text = text.lower()
		text = "".join(x for x in text if x not in exclude)

		if text is None:
			return 0
		elif len(text) == 0:
			return 0
		else:
			if text[0] in vowels:
				count += 1
			for index in range(1, len(text)):
				if text[index] in vowels and text[index-1] not in vowels:
					count += 1
			if text.endswith('e'):
				count -= 1
			if text.endswith('le'):
				count += 1
			if count == 0:
				count += 1
			count = count - (0.1*count)
			return count
	def lexicon_count(text, removepunct=True):
		if removepunct:
			text = ''.join(ch for ch in text if ch not in exclude)
		count = len(text.split())
		return count
	


	ticker = 0
	for i in range(int(len(oldprez))):
		AVEsentence_length(oldprez[ticker])
		averagewordlength(oldprez[ticker])
		wordcount(oldprez[ticker])
		flesch_score(oldprez[ticker])
		
		ticker += 1


	def user_sentence_rank(filename):
		
		user_score = USER_AVEsentence_length(filename)

		xxx = sorted(sentence_rank.values(), reverse=True)
		
		score = xxx.index(user_score) + 1
		print("User input ranked number", score, "for sentence length.") 
		return score

	def user_word_rank(filename):
		
		user_score = USER_averagewordlength(filename)

		xxx = sorted(word_rank.values(), reverse = True)
		score = xxx.index(user_score) + 1
		print("User input ranked number", score, "for word length.") 
		return score

	def user_vocab_rank(filename):
		
		user_score = USER_wordcount(filename)

		xxx = sorted(vocab_rank.values(), reverse = True)
		score = xxx.index(user_score) + 1
		print("User input ranked number", score, "for breadth of vocabulary.") 
		return score

	def user_flesch_rank(filename):
		
		user_score = USER_flesch_score(filename)

		xxx = sorted(flesch_ranking.values(), reverse = True)
		score = xxx.index(user_score) + 1
		print("Scoring a grade of", user_score, "on the Flesch test, user ranked number", score, ".") 
		return score

	
main()

from tkinter import *

root=Tk()
message=Label(root, text="Enter your text here:")
message.grid(column=0)
entry=Entry(root, bd=5)
entry.grid(column=1,row=0)
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
CheckVar5=IntVar()

blank = []
def runCommands():
	if(CheckVar2==1):
		blank.append("user_sentence_rank")
		main()
		user_sentence_rank(get(first))
	if(CheckVar3==1):
		blank.append('2')
		main()
		user_word_rank(get(first))
	if(CheckVar4==1):
		blank.append('3')
		main()
		user_vocab_rank(get(first))
	if(CheckVar5==1):
		blank.append('4')
		main()
		user_flesch_rank(get(first))
   
C2=Checkbutton(root, text="Average Sentence Length", variable=CheckVar2, onvalue=1, offvalue=0)
  
C3=Checkbutton(root, text="Average Word Length", variable=CheckVar3, onvalue=1, offvalue=0)

C4=Checkbutton(root, text="Percentage of simple words used", variable=CheckVar4, onvalue=1, offvalue=0)

C5=Checkbutton(root, text="Flesch Reading Score", variable=CheckVar5, onvalue=1, offvalue=0)
   
done=Button(root, text="Run", command=runCommands)

C2.grid(column=2,row=1)
C3.grid(column=3,row=1)
C4.grid(column=4,row=1)
C5.grid(column=5, row=1)
done.grid(row=2, column=2)
Lb1=Listbox(root)
Lb1.insert(1, "Thomas Jefferson.txt")
Lb1.insert(2,"Andrew Jackson.txt")
Lb1.insert(3,"Abraham Lincoln.txt")
Lb1.insert(4,"Teddy Roosevelt.txt")
Lb1.insert(5,"FDR.txt")
Lb1.insert(6,"JFK.txt")
Lb1.insert(7,"Richard Nixon.txt")
Lb1.insert(8,"Ronald Reagan.txt")
Lb1.insert(9,"Bill Clinton.txt")
Lb1.insert(10,"George W Bush.txt")
Lb1.insert(11,"Barrack Obama.txt")

Lb1.grid(row=5, column=1)

#Lb1.bind("<Button-1>", runCommands)
var=StringVar()
label=Message(root, textvariable = var)
var.set(main())

label.grid(row=5, column = 4)

root.mainloop()
