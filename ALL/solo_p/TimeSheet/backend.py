from flask import Flask, request, jsonify, csv

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit_hours():
    data = request.get_json()
    # Store the logged hours data in a file or database
    with open("D:\timeApp\time_sheet.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writero(data.values())
    # Perform necessary processing or calculations

    return jsonify({"message": "Hours logged successfully"})

if __name__ == "__main__":
    app.run()
