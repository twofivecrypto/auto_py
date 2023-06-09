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

directory = "D:\\auto_py\\projects\\madLibs\\madLibsStories"

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

# Define the HTML template with interactive JavaScript and CSS
html_template = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Mad Libs Story</title>
    <style>
        body {{
            background-color: #222222;
            color: #00FF00;
            font-family: "Press Start 2P", cursive;
            padding: 20px;
        }}

        #mad-libs-story {{
            margin-bottom: 20px;
        }}

        .input-field {{
            margin-bottom: 10px;
        }}

        .button {{
            background-color: #00FF00;
            color: #000000;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }}

        .button:hover {{
            background-color: #00CC00;
        }}
    </style>
    <script>
        function generateMadLibs() {{
            var noun = document.getElementById('noun').value;
            var verb = document.getElementById('verb').value;
            var adjective = document.getElementById('adjective').value;
            var adverb = document.getElementById('adverb').value;
            var place = document.getElementById('place').value;
            var animal = document.getElementById('animal').value;
            var emotion = document.getElementById('emotion').value;
            var color = document.getElementById('color').value;
            var food = document.getElementById('food').value;
            var number = document.getElementById('number').value;
            var hobby = document.getElementById('hobby').value;
            var song = document.getElementById('song').value;
            var superhero = document.getElementById('superhero').value;

            var madLibsStory = `Once upon a time, in a ${place} far away, there was a ${adjective} ${noun} who loved to ${verb} ${adverb}. ` +
                `One day, while exploring the ${place}, the ${noun} discovered a magical ${animal} with ${color} fur. ` +
                `They quickly became friends and embarked on ${number} exciting adventures together. ` +
                `They would ${verb} through fields of ${color} flowers and swim in crystal-clear lakes. ` +
                `The ${noun} was always filled with ${emotion} whenever they were with their ${animal} friend. ` +
                `One of their favorite activities was picnicking, and they would enjoy delicious ${food} under ` +
                `the shade of a magnificent tree. Their friendship grew stronger with each passing day, ` +
                `and they created memories that would last a lifetime. ` +
                `They would often ${hobby} together and sing their favorite song, '${song}', while exploring new places. ` +
                `They even had a secret superhero alter ego: ${superhero} and ${animal}, ` +
                `protecting the ${place} from any evil forces. Their bond was unbreakable, ` +
                `and they lived happily ever after, bringing joy and laughter to everyone they encountered. ` +
                `Whenever someone needed help, ${superhero} and ${animal} would swoop in to save the day. ` +
                `They used their superpowers and ${noun}-like abilities to overcome any obstacles. ` +
                `Their bravery and kindness inspired others in ${place} and beyond. ` +
                `They were hailed as heroes and celebrated for their extraordinary deeds. ` +
                `Their story became legendary, passed down through generations, ` +
                `and their names were forever etched in the annals of ${place}'s history. ` +
                `Their friendship became a symbol of hope, reminding everyone that together, ` +
                `they could achieve the impossible. And so, the adventures of ${superhero} and ${animal} ` +
                `continued, leaving a lasting legacy of courage, friendship, and the power of dreams.`;

            document.getElementById('mad-libs-story').textContent = madLibsStory;
        }}
    </script>
</head>
<body>
    <h1>Mad Libs Story</h1>
    <div class="input-field">
        <label for="noun">Noun:</label>
        <input type="text" id="noun" />
    </div>
    <div class="input-field">
        <label for="verb">Verb:</label>
        <input type="text" id="verb" />
    </div>
    <div class="input-field">
        <label for="adjective">Adjective:</label>
        <input type="text" id="adjective" />
    </div>
    <div class="input-field">
        <label for="adverb">Adverb:</label>
        <input type="text" id="adverb" />
    </div>
    <div class="input-field">
        <label for="place">Place:</label>
        <input type="text" id="place" />
    </div>
    <div class="input-field">
        <label for="animal">Animal:</label>
        <input type="text" id="animal" />
    </div>
    <div class="input-field">
        <label for="emotion">Emotion:</label>
        <input type="text" id="emotion" />
    </div>
    <div class="input-field">
        <label for="color">Color:</label>
        <input type="text" id="color" />
    </div>
    <div class="input-field">
        <label for="food">Food:</label>
        <input type="text" id="food" />
    </div>
    <div class="input-field">
        <label for="number">Number:</label>
        <input type="text" id="number" />
    </div>
    <div class="input-field">
        <label for="hobby">Hobby:</label>
        <input type="text" id="hobby" />
    </div>
    <div class="input-field">
        <label for="song">Song:</label>
        <input type="text" id="song" />
    </div>
    <div class="input-field">
        <label for="superhero">Superhero Name:</label>
        <input type="text" id="superhero" />
    </div>
    <button class="button" onclick="generateMadLibs()">Generate Story</button>
    <p id="mad-libs-story"></p>
</body>
</html>
'''

# Save the Mad Libs story in an HTML file
filename = f"{directory}/mad_libs_story.html"
with open(filename, "w") as file:
    file.write(html_template)

# Display the file path to the user
print("The Mad Libs story has been saved successfully!")
print(f"You can find it at: {os.path.abspath(filename)}")
