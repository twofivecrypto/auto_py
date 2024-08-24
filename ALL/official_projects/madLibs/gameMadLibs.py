import os

# Ask the user to enter different words to fill in the blanks
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")
color = input("Enter a color: ")
food = input("Enter a food: ")
number = input("Enter a number: ")
hobby = input("Enter a hobby: ")
song = input("Enter a song: ")
superhero = input("Enter a superhero name: ")

# Create a Mad Libs story using the user's input
story = f"Once upon a time, in a {place} far away, there was a {adjective} {noun} who loved to {verb} {adverb}. " \
        f"One day, while exploring the {place}, the {noun} discovered a magical {animal} with {color} fur. " \
        f"They quickly became friends and embarked on {number} exciting adventures together. " \
        f"They would {verb} through fields of {color} flowers and swim in crystal-clear lakes. " \
        f"The {noun} was always filled with {emotion} whenever they were with their {animal} friend. " \
        f"One of their favorite activities was picnicking, and they would enjoy delicious {food} under " \
        f"the shade of a magnificent tree. Their friendship grew stronger with each passing day, " \
        f"and they created memories that would last a lifetime. " \
        f"They would often {hobby} together and sing their favorite song, '{song}', while exploring new places. " \
        f"They even had a secret superhero alter ego: {superhero} and {animal}, " \
        f"protecting the {place} from any evil forces. Their bond was unbreakable, " \
        f"and they lived happily ever after, bringing joy and laughter to everyone they encountered. " \
        f"Whenever someone needed help, {superhero} and {animal} would swoop in to save the day. " \
        f"They used their superpowers and {noun}-like abilities to overcome any obstacles. " \
        f"Their bravery and kindness inspired others in {place} and beyond. " \
        f"They were hailed as heroes and celebrated for their extraordinary deeds. " \
        f"Their story became legendary, passed down through generations, " \
        f"and their names were forever etched in the annals of {place}'s history. " \
        f"Their friendship became a symbol of hope, reminding everyone that together, " \
        f"they could achieve the impossible. And so, the adventures of {superhero} and {animal} " \
        f"continued, leaving a lasting legacy of courage, friendship, and the power of dreams."

# Create a directory to store the Mad Libs stories if it doesn't exist
directory = "madLibsStories"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the Mad Libs story in a .txt file
filename = f"{directory}/mad_libs_story.txt"
with open(filename, "w") as file:
    file.write(story)

# Display the file path to the user
print("The Mad Libs story has been saved successfully!")
print(f"You can find it at: {os.path.abspath(filename)}")
