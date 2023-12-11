import torch
from CBFclass import CBF
import pandas as pd

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the CSV file
df = pd.read_csv('/Users/walte/Desktop/PolyPulse/Backend/modelLib/megaGymDataset.csv')

# Filter out rows that contain a null value in any column
df = df.dropna(how='any')

# Create a workout map
workout_map = {}
val = 0
for workout in df['Title'].unique():
    if workout not in workout_map:
        workout_map[workout] = val
        val += 1


# Create a difficulty level map
difficulty_map = {}
val = 0
for difficulty in df['Level'].unique():
    if difficulty not in difficulty_map:
        difficulty_map[difficulty] = val
        val += 1

# Convert a workout, difficulty level (categorical) and user rating to tensors
def convert_to_tensors(workout, difficulty_level,user_rating):
    workout_tensor = torch.tensor([workout_map[workout]], dtype=torch.long)
    difficulty_level_tensor = torch.tensor([difficulty_map[difficulty_level]], dtype=torch.long)
    user_rating_tensor = torch.tensor([user_rating], dtype=torch.long)
    return workout_tensor, difficulty_level_tensor, user_rating_tensor

# Create the model
model = CBF(num_users=len(df['Rating']),num_workouts=len(workout_map), num_difficulty_levels=len(difficulty_map))

# Define the loss function and optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.MSELoss()

# Train the model
for epoch in range(100):
    for _, workout, _, _, _, _, difficulty_level, user_rating,_ in df.itertuples(index=False):
        workout_tensor, difficulty_level_tensor,user_rating_tensor = convert_to_tensors(workout, difficulty_level, user_rating)

        # Compute the user rating prediction
        user_rating_prediction = model(user_rating_tensor,workout_tensor, difficulty_level_tensor)

        # Compute the loss
        loss = criterion(user_rating_prediction, user_rating_tensor.float())

        # Backpropagate the loss and update the model parameters
        optimizer.zero_grad()
        loss.backward()

# Pick a set of workouts
workout1,difficulty1,user_rating1 = convert_to_tensors("Over bench jump", "Intermediate", 10)
workout2,difficulty2,user_rating2 = convert_to_tensors("Double Kettlebell Push Press", "Intermediate", 10)
workout3,difficulty3,user_rating3 = convert_to_tensors("Reverse Grip Triceps Pushdown", "Intermediate", 10)

# User rating predictions for current user
user_preference_prediction1 = model.forward(user_rating1,workout1,difficulty1)
user_preference_prediction2 = model.forward(user_rating2,workout2,difficulty2)
user_preference_prediction3 = model.forward(user_rating3,workout3,difficulty3)

# The users actual likeliness of enjoying a given set of workouts
print(user_preference_prediction1.item())
print(user_preference_prediction2.item())
print(user_preference_prediction3.item())