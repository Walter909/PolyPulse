import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import logoPath from "../img/logo.png";
import "../styles/Form.css";

const Home = () => {
  const navigate = useNavigate();

  const [school, setSchool] = useState("");
  const [age, setAge] = useState("");
  const [weight, setWeight] = useState("");
  const [location, setLocation] = useState("");
  const [difficulty, setDifficulty] = useState("");

  return (
    <div className="flex flex-col flex-wrap">
      <div className="flex justify-center">
        <img src={logoPath} alt="PolyPulse Logo" height="75" width="75" />
      </div>

      <form onSubmit={() => navigate("/difficulty")}>
        <div className="form-group">
          <label htmlFor="school">School:</label>
          <input
            type="text"
            id="school"
            value={school}
            onChange={(e) => setSchool(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="age">Age:</label>
          <input
            type="number"
            id="age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="weight">Weight:</label>
          <input
            type="number"
            id="weight"
            value={weight}
            onChange={(e) => setWeight(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Location:</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                name="location"
                value="home"
                checked={location === "home"}
                onChange={() => setLocation("home")}
              />
              Home
            </label>
            <label>
              <input
                type="radio"
                name="location"
                value="gym"
                checked={location === "gym"}
                onChange={() => setLocation("gym")}
              />
              Gym
            </label>
            <label>
              <input
                type="radio"
                name="location"
                value="dorm"
                checked={location === "dorm"}
                onChange={() => setLocation("dorm")}
              />
              Dorm
            </label>
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="difficulty">Difficulty:</label>
          <select
            id="difficulty"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
          >
            <option value="">Select difficulty</option>
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
        </div>
        <div className="flex justify-center">
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
};

export default Home;
