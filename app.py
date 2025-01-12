from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

'''
connection_string = "mongodb+srv://user:password@cluster0.l6iy87kj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

# Access Database
db = client['your_database']
collection = db['notifications']

# Print MongoDB Data
print("MongoDB Data >> ",collection.find())
'''

notifications = [
    "📩 New message from John",
    "📢 New update available: Version 1.2 released!",
    "📝 New blog post: '5 Tips for Better Web Design'",
    "📩 You have a new message from Alex.",
    "🔔 Event reminder: Team meeting at 3 PM.",
    "🚀 Feature launched: Dark mode now available!",
    "📅 Your subscription will expire in 3 days.",
    "🏆 Congratulations! You've unlocked a new badge.",
    "💡 Tip of the day: Use keyboard shortcuts to save time.",
    "📷 New photo album uploaded by John.",
    "🎉 Exclusive offer: 20% off on premium plans."
]

@app.route("/", methods=["GET"])
def mainPage():
    return  render_template("index.html")

@app.route("/notification", methods=["GET"])
def notification():
    return  render_template("notification.html", notifications=notifications)

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=9002, debug=True)