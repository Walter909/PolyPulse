import React, { useEffect, useState } from "react";

import axios from "axios";

const Plan = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchDataAndSetState = async () => {
      try {
        console.log("here");
        const http = await axios.get("http://127.0.0.1:5000/workouts"); // Call the fetchData function
        setWorkouts(http.data); // Set the workouts from fetched data
      } catch (error) {
        // Handle errors if needed
        console.log("Took to long" + error);
      }
    };

    fetchDataAndSetState(); // Invoke the fetchDataAndSetState function
  }, []); // The empty dependency array ensures this effect runs only once

  console.log(workouts);
  return (
    <>
      <h1>Cardiovascular Endurance Workouts</h1>

      <div>
        <h2>Cardiovascular Endurance Workout 1</h2>
        <ul>
          <li>
            <strong>Exercise 1: Jumping Jacks</strong>
            <ul>
              <li>Sets: 3 | Reps: 20</li>
              <li>
                Technique: Start with feet together and arms at the sides, then
                jump while spreading the legs and raising the arms above the
                head. Land softly and repeat.
              </li>
            </ul>
          </li>

          <li>
            <strong>Exercise 2: Burpees</strong>
            <ul>
              <li>Sets: 3 | Reps: 10</li>
              <li>
                Technique: Start in a standing position, then drop into a squat
                position with hands on the ground. Kick the feet back into a
                plank position, then immediately return them to the squat
                position. Jump up as high as possible from the squat position
                and repeat.
              </li>
            </ul>
          </li>

          <li>
            <strong>Exercise 3: High Knees</strong>
            <ul>
              <li>Sets: 3 | Reps: 30 seconds</li>
              <li>
                Technique: Stand with feet hip-width apart and jog in place,
                lifting the knees as high as possible while pumping the arms.
              </li>
            </ul>
          </li>

          <li>
            <strong>Exercise 4: Jumping Rope</strong>
            <ul>
              <li>Sets: 3 | Reps: 1 minute</li>
              <li>
                Technique: Hold the handles of a jump rope with your hands and
                swing it over your head while jumping over it with both feet.
              </li>
            </ul>
          </li>

          <li>
            <strong>Exercise 5: Cycling</strong>
            <ul>
              <li>Sets: 3 | Reps: 20 minutes</li>
              <li>
                Technique: Hop on a stationary bike or go for a bike ride
                outdoors to improve cardiovascular endurance.
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </>
  );
};

export default Plan;
