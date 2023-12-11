
from flask import Flask,render_template
from flask_cors import CORS
from gptrecs import generate_workout_recommendations,FitnessGoal,FitnessLevel
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load home page and model
@app.route("/")
def index():
    return render_template("index.html")

# Receive workout difficulty
@app.route("/workouts")
def workouts(): 
    return generate_workout_recommendations(3, 5, 150, FitnessLevel.BEGINNER, FitnessGoal.IMPROVE_CARDIOVASCULAR_ENDURANCE)

# Debug mode 
if __name__ == '__main__':
    app.run(port=5000)