import os
import sys
import random

def randomizeWordCase(word):
	choice = random.randint(0,1)
	if choice == 1:
		return word.lower()
	return word
def randomizeWordCase2(word):
	choice = random.randint(0,1)
	if choice == 1:
		return word.capitalize()
	return word
def getRandomDelim():
	choice = random.randint(0,2)
	if choice == 1:
		return "-"
	if choice == 2:
		return "."
	return ""
def getRandomNumber():
	numbers =  [ "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "123", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "01", "02", "03", "04"]
	choice = random.randint(0,2)
	if choice == 1 or choice == 2:
		return random.choice(numbers)
	return ""
def getRandomDomain():
	domains = ["gmail.com", "yahoo.com", "hotmail.com", "inbox.com", "icloud.com", "aol.com", "msn.com"]
	choice = random.randint(0,9)
	if choice == 0 or choice == 1 or choice == 2 or choice == 3:
		return domains[0]
	if choice == 4 or choice == 5 or choice == 6:
		return "yahoo.com"
	if choice == 7 or choice == 8:
		return "hotmail.com"
	return random.choice(domains)
def getRandomFirstName():
	firstNames =  ["Jacob", "Emily", "Michael", "Madison", "Joshua", "Emma", "Matthew", "Olivia", "Daniel", "Hannah", "Christopher", "Abigail", "Andrew", "Isabella", "Ethan", "Samantha", "Joseph", "Elizabeth", "William", "Ashley", "Anthony", "Alexis", "David", "Sarah", "Alexander", "Sophia", "Nicholas", "Alyssa", "Ryan", "Grace", "Tyler", "Ava", "James", "Taylor", "John", "Brianna", "Jonathan", "Lauren", "Noah", "Chloe", "Brandon", "Natalie", "Christian", "Kayla", "Dylan", "Jessica", "Samuel", "Anna", "Benjamin", "Victoria", "Nathan", "Mia", "Zachary", "Hailey", "Logan", "Sydney", "Justin", "Jasmine", "Gabriel", "Julia", "Jose", "Morgan", "Austin", "Destiny", "Kevin", "Rachel", "Elijah", "Ella", "Caleb", "Kaitlyn", "Robert", "Megan", "Thomas", "Katherine", "Jordan", "Savannah", "Cameron", "Jennifer", "Jack", "Alexandra", "Hunter", "Allison", "Jackson", "Haley", "Angel", "Maria", "Isaiah", "Kaylee", "Evan", "Lily", "Isaac", "Makayla", "Luke", "Brooke", "Mason", "Nicole", "Jayden", "Mackenzie", "Jason", "Addison", "Gavin", "Stephanie", "Aaron", "Lillian", "Connor", "Andrea", "Aiden", "Zoe", "Aidan", "Faith", "Kyle", "Kimberly", "Juan", "Madeline", "Charles", "Alexa", "Luis", "Katelyn", "Adam", "Gabriella", "Lucas", "Gabrielle", "Brian", "Trinity", "Eric", "Amanda", "Adrian", "Kylie", "Nathaniel", "Mary", "Sean", "Paige", "Alex", "Riley", "Carlos", "Leah", "Bryan", "Jenna", "Ian", "Sara", "Owen", "Rebecca", "Jesus", "Michelle", "Landon", "Sofia", "Julian", "Vanessa", "Chase", "Jordan", "Cole", "Angelina", "Diego", "Caroline", "Jeremiah", "Avery", "Steven", "Audrey", "Sebastian", "Evelyn", "Xavier", "Maya", "Timothy", "Claire", "Carter", "Autumn", "Wyatt", "Jocelyn", "Brayden", "Ariana", "Blake", "Nevaeh", "Hayden", "Arianna", "Devin", "Jada", "Cody", "Bailey", "Richard", "Brooklyn", "Seth", "Aaliyah", "Dominic", "Amber", "Jaden", "Isabel", "Antonio", "Mariah", "Miguel", "Danielle", "Liam", "Melanie", "Patrick", "Sierra", "Carson", "Erin", "Jesse", "Molly", "Tristan", "Amelia", "Alejandro", "Isabelle", "Henry", "Madelyn", "Victor", "Melissa", "Trevor", "Jacqueline", "Bryce", "Marissa", "Jake", "Shelby", "Riley", "Angela", "Colin", "Leslie", "Jared", "Katie", "Jeremy", "Jade", "Mark", "Catherine", "Caden", "Diana", "Garrett", "Aubrey", "Parker", "Mya", "Marcus", "Amy", "Vincent", "Briana", "Kaleb", "Sophie", "Kaden", "Gabriela", "Brady", "Breanna", "Colton", "Gianna", "Kenneth", "Kennedy", "Joel", "Gracie", "Oscar", "Peyton", "Josiah", "Adriana", "Jorge", "Christina", "Cooper", "Courtney", "Ashton", "Daniela", "Tanner", "Lydia", "Eduardo", "Kathryn", "Paul", "Valeria", "Edward", "Layla", "Ivan", "Alexandria", "Preston", "Natalia", "Maxwell", "Angel", "Alan", "Laura", "Levi", "Charlotte", "Stephen", "Margaret", "Grant", "Cheyenne", "Nicolas", "Mikayla", "Dakota", "Miranda", "Omar", "Naomi", "Alexis", "Kelsey", "George", "Payton", "Eli", "Ana", "Collin", "Alicia", "Spencer", "Jillian", "Gage", "Daisy", "Max", "Mckenzie", "Ricardo", "Ashlyn", "Cristian", "Sabrina", "Derek", "Caitlin", "Micah", "Summer", "Brody", "Ruby", "Francisco", "Rylee", "Nolan", "Valerie", "Ayden", "Skylar", "Dalton", "Lindsey", "Shane", "Kelly", "Peter", "Genesis", "Damian", "Zoey", "Jeffrey", "Eva", "Brendan", "Sadie", "Travis", "Alexia", "Fernando", "Cassidy", "Peyton", "Kylee", "Conner", "Kendall", "Andres", "Jordyn", "Javier", "Kate", "Giovanni", "Jayla", "Shawn", "Karen", "Braden", "Tiffany", "Jonah", "Cassandra", "Bradley", "Juliana", "Cesar", "Reagan", "Emmanuel", "Caitlyn", "Manuel", "Giselle", "Edgar", "Serenity", "Mario", "Alondra", "Erik", "Lucy", "Edwin", "Bianca", "Johnathan", "Kiara", "Devon", "Crystal", "Erick", "Erica", "Wesley", "Angelica", "Oliver", "Hope", "Trenton", "Chelsea", "Hector", "Alana", "Malachi", "Liliana", "Jalen", "Brittany", "Raymond", "Camila", "Gregory", "Makenzie", "Abraham", "Lilly", "Elias", "Veronica", "Leonardo", "Abby", "Sergio", "Jazmin", "Donovan", "Adrianna", "Colby", "Delaney", "Marco", "Karina", "Bryson", "Ellie", "Martin", "Jasmin"]
	return randomizeWordCase(random.choice(firstNames))
def getRandomLastName():
	lastNames =  ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "","ussell", "Griffin", "Diaz", "Hayes"]
	choice = random.randint(0,2)
	if choice == 0 or choice == 1:
		return randomizeWordCase(random.choice(lastNames))
	return ""
def getRandomMiddleInitial():
	initials = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]
	choice = random.randint(0,4)
	if choice == 4:
		return randomizeWordCase(random.choice(initials))
	return ""
def getRandomWord():
	words = ["forget", "accent", "eye", "impound", "comfort", "route", "knot", "bow", "hurt", "dome", "mixture", "bike", "memory", "rung", "capture", "random", "garlic", "fall",  "theft", "lost", "wrong", "dome", "deport", "meal", "spy", "desert", "nun", "wood", "duty", "joke", "rich", "swipe", "expose", "trial", "neutral", "heroin", "advice", "blue", "lick", "watch", "formal", "squash", "hair", "custody", "return", "rage", "cry", "metal", "master", "radio", "scrape", "area", "bake", "eject", "cereal", "fresh", "cluster", "freedom", "drug", "bitter", "red", "jungle", "remain", "spell", "beef", "text", "stroll", "lift", "oral", "lease", "flat", "level", "story", "sniff", "contain", "flour", "degree", "art", "mercy", "jacket", "silence", "Sunday", "limit", "lighter", "mine", "bee", "break", "powder", "love", "flight", "courage", "sleeve", "gem", "witness", "problem", "brush", "reason", "retired", "alcohol", "chest", "tiger", "fast", "say", "kidney", "officer", "product", "outlook", "insight", "equip", "affair", "chapter", "crevice", "comedy", "widen", "army", "shake", "block", "gown", "tract", "layer", "bitch", "differ", "ensure", "illness", "figure", "free", "fashion", "land", "evening", "limited", "process", "thread", "dinner", "belly", "trolley", "trouble", "load", "efflux", "carry", "profit", "grind", "lie", "reform", "owl", "wash", "wind", "slam", "patent", "calm", "latest", "brown", "chop", "stride", "get", "grant", "default", "bride", "leave", "barrel", "trust", "combine", "temple", "root", "faith", "sour", "answer", "bishop", "curtain", "falsify", "prefer", "grief", "contact", "percent", "virgin", "staff", "hate", "zone", "fantasy", "export", "reign", "cause", "ribbon", "coal", "refund", "mix", "effort", "patient", "park", "venture", "hope", "depend", "nuclear", "snuggle", "list", "walk", "common", "suffer", "appeal", "brave", "live", "bracket", "layout", "perfume", "chew", "seize", "plastic", "realism", "peace", "agile", "gene", "theory", "record", "safety", "mayor", "coffin", "paint", "laborer", "system", "angle", "prevent", "moment", "heaven", "set", "smart", "genuine", "creep", "licence", "coat", "basket", "smoke", "ticket", "left", "thaw", "hammer", "sail", "east", "trust", "blank", "chapter", "lick", "inject", "fraud", "term", "assume", "efflux", "stain", "year", "free", "young", "portion", "notice", "cry", "provoke", "cereal", "file", "mosque", "sow", "refuse", "biology", "price", "day", "hallway", "tribe", "please", "avenue", "summary", "fun", "mutter", "wonder", "fate", "owner", "quota", "child", "porter", "hostage", "animal", "delay", "doll", "inch", "office", "flock", "dull", "eternal", "network", "genetic", "counter", "linen", "colony", "joint", "pursuit", "hip", "normal", "moral", "kinship", "crew", "carve", "sip", "report", "help", "exact", "denial", "crisis", "visual", "calorie", "solve", "flex", "grip", "snatch", "fossil", "trivial", "doctor", "current", "sign", "crude", "secure", "symptom", "heat", "right", "half", "loose", "clerk", "cheek", "deliver", "artist", "pepper", "pupil", "explain", "era", "referee", "related", "quaint", "effect", "novel", "tip", "strain", "brown", "storm", "begin", "tough", "wait", "frozen", "remind", "maximum", "shorts", "calf", "peasant", "dive", "chest", "dawn", "abolish", "factory", "index", "self", "empire", "patrol", "action", "studio", "economy", "flag", "pause", "steam", "frog", "matter", "draw", "fund", "shock", "essay", "fence", "glory", "golf", "study", "motif", "cycle", "outside", "tidy", "miss", "general", "percent", "modest", "mystery", "station", "cluster", "tiptoe", "kneel", "lead", "split", "aisle", "ice", "dip", "taxi", "budge", "fruit", "member", "brand", "get", "swear", "summit", "safety", "upset", "woman"]
	return randomlyModifyWord(randomizeWordCase2(random.choice(words)))
def randomlyModifyWord(word):
	choice = random.randint(0, 9)
	if choice < 3:
		modified = 0
		for x in range(len(word)):
			#print word + " to be modified..."
			if((word[x] == "l" or word[x] == "i") and modified == 0):
				word = word.replace("l", "1")
				word = word.replace("i", "1")
				chance = random.randint(0,1)
				if chance == 0:
					modified = 1
			if((word[x] == "o" or word[x] == "O") and modified == 0):
				word = word.replace("o", "0")
				word = word.replace("O", "0")
				chance = random.randint(0,1)
				if chance == 0:
					modified = 1
			if((word[x] == "a" or word[x] == "A") and modified == 0):
				word = word.replace("a", "@")
				word = word.replace("A", "@")
				chance = random.randint(0,1)
				if chance == 0:
					modified = 1
			if((word[x] == "e" or word[x] == "E") and modified == 0):
				word = word.replace("e", "3")
				word = word.replace("E", "3")
				chance = random.randint(0,1)
				if chance == 0:
					modified = 1
	return word



def getPsuedoRandomEmail():
	#top 200 names according to some website
	fillers = ["Rox", "6969", "TheSlayer", "LovesBirds", "LovesDogs", "Master", "Masta", "Diamond", "Running", "EatsPizza"]
	number = getRandomNumber()
	delimiter = getRandomDelim()
	domain = getRandomDomain()
	firstname = getRandomFirstName()
	lastname = getRandomLastName()
	if lastname != "":
		middle = getRandomMiddleInitial()
	else:
		middle = ""
	if lastname == "":
		delimiter = ""
	if lastname == "" and number == "":
		number = randomizeWordCase(random.choice(fillers))
	if middle != "":
		lastname = middle + delimiter + lastname
	
	#basic example: get name/number/domain and return email
	total = firstname + delimiter + lastname + number + "@" + domain
	print total

def getPsuedoRandomPassword():
	# goal here is to satsify password req"s and make a random password
	# we will be going at least 1 uppercase, 1 lowercase, 1 number, with potential of having a special character 
	currPass = ""
	choice = random.randint(0,1)
	if choice == 1:
		numWords = random.randint(1,3)
		for x in range(numWords):
			currPass += getRandomWord()
		hasNumber = random.randint(0,1)
		currPass += getRandomNumber()
		
	if choice == 0:
		choice2 = random.randint(0,1)
		if choice2 == 0:
			numNames = random.randint(1,2)
			for x in range(numNames):
				currPass += getRandomFirstName()
			currPass += getRandomNumber()
		if choice2 == 1:
			numNames = random.randint(1,2)
			for x in range(numNames):
				currPass+= getRandomLastName()
			currPass += getRandomNumber()


	if(len(currPass) < 8):
		currPass += getRandomWord()
	print currPass



for x in range(50):
  getPsuedoRandomEmail()
  getPsuedoRandomPassword()