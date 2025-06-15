subject = ["Chinese", "English", "Maths", "Physics", "Chemistry", "Biology"]
print("Welcome to the subject management system!")
print("Here are the subjects you can manage:")
print(subject)
hate =input(f"Which subject do you hate? {subject} ").capitalize()
num = subject.index(hate)
del subject[num]
print("Here are the remaining subjects:")
print(subject)