from flask import Flask, render_template

app = Flask(__name__)

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