import json
from enum import Enum
import os
from dotenv import load_dotenv
from openai import OpenAI

class FitnessGoal(Enum):
    GAIN_MUSCLE = 1
    LOSE_WEIGHT = 2
    IMPROVE_CARDIOVASCULAR_ENDURANCE = 3

    @classmethod
    def get_by_string(cls, string_value):
        for member in cls:
            if member.name.replace("_", " ").lower() == string_value.lower():
                return member
        raise ValueError(f"No FitnessGoal exists for '{string_value}'")

    def to_string(self):
        return self.name.replace("_", " ").lower()


class FitnessLevel(Enum):
    BEGINNER = 1
    EXPERIENCED = 2
    ADVANCED = 3

    @classmethod
    def get_by_string(cls, string_value):
        for member in cls:
            if member.name.lower() == string_value.lower():
                return member
        raise ValueError(f"No FitnessLevel exists for '{string_value}'")


return_json_sample: dict = {
    "workouts": [
        {
            "description": "1-sentence description of workout 1",
            "exercises": [
                {
                    "name": "Exercise 1 Name",
                    "sets": "3-4",
                    "reps": "8-12",
                    "technique": "Include proper form and technique tips"
                },
                {
                    "name": "Exercise 2 Name",
                    "sets": "3",
                    "reps": "12",
                    "technique": "Include proper form and technique tips"
                }
            ]
        },
        {
            "description": "1-sentence description of workout 2",
            "exercises": [
                {
                    "name": "Exercise 1 Name",
                    "sets": "3-4",
                    "reps": "8-12",
                    "technique": "Include proper form and technique tips"
                },
                {
                    "name": "Exercise 2 Name",
                    "sets": "3",
                    "reps": "12",
                    "technique": "Include proper form and technique tips"
                }
            ]
        }
    ]
}


def send_prompt_to_chatgpt(prompt: str) -> str:
    # Load environment variables from .env file
    load_dotenv()

    # Now you can use variables from the .env file
    openai_api_key = os.getenv("API_KEY")
    client = OpenAI(api_key=openai_api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    response_text = chat_completion.choices[0].message.content.strip()
    return response_text


def generate_workout_recommendations(n_workouts: int, n_exercises_per_workout: int,
                                     weight_lbs: int, fitness_level: FitnessLevel, fitness_goal: FitnessGoal) -> dict:

    chatgpt_api_prompt: str = (f"Imagine you are a personal trainer for a person with {fitness_level.name.lower()}"
                               f"-level fitness experience. They weigh {weight_lbs} lbs, and their overall fitness "
                               f"goal is to {fitness_goal.to_string()}. Recommend them {n_workouts} different "
                               f"workouts, each with {n_exercises_per_workout} exercises. For each workout, provide "
                               f"the information as specified in the sample JSON below. Ensure your response is only "
                               f"JSON, as it will be parsed directly by code, and any conversational text will "
                               f"disrupt our service."
                               f"\nHere is a sample JSON response:"
                               f"{json.dumps(return_json_sample, indent=4)}")
    
    chatgpt_response: str = send_prompt_to_chatgpt(chatgpt_api_prompt)
    return chatgpt_response

print(generate_workout_recommendations(3, 5, 150, FitnessLevel.BEGINNER, FitnessGoal.IMPROVE_CARDIOVASCULAR_ENDURANCE))




