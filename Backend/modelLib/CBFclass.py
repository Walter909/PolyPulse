import torch
import torch.nn as nn

class CBF(nn.Module):
    def __init__(self, num_users, num_workouts, num_difficulty_levels):
        super(CBF, self).__init__()

        # Create embedding layers for workouts, difficulty levels, and users
        self.user_embeddings = nn.Embedding(num_users, 128)
        self.workout_embeddings = nn.Embedding(num_workouts, 128)
        self.difficulty_level_embeddings = nn.Embedding(num_difficulty_levels, 128)

        # Create linear layers for user rating prediction
        self.linear_workout = nn.Linear(128, 64)  # Adjust the dimensions as needed
        self.linear_difficulty = nn.Linear(128, 64)  # Adjust the dimensions as needed
        self.linear_user = nn.Linear(128, 64)  # Adjust the dimensions as needed

        # Final prediction layer
        self.predict_layer = nn.Linear(192, 1)  # Adjust the dimensions as needed

    def forward(self, user_id, workout_id, difficulty_level_id):
        user_embedding = self.user_embeddings(user_id)
        workout_embedding = self.workout_embeddings(workout_id)
        difficulty_level_embedding = self.difficulty_level_embeddings(difficulty_level_id)

        # Pass the embeddings through linear layers
        user_out = self.linear_user(user_embedding)
        workout_out = self.linear_workout(workout_embedding)
        difficulty_out = self.linear_difficulty(difficulty_level_embedding)

        # Concatenate the embeddings
        embeddings = torch.cat([user_out, workout_out, difficulty_out], dim=1)

        # Predict user rating
        user_rating_prediction = self.predict_layer(embeddings)

        return user_rating_prediction