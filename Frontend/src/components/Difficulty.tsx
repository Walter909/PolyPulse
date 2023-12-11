import React from "react";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";

const Diff = styled.div`
  text-align: center;
  box-sizing: border-box;
  font-size: 25px;
  height: 75px;
  width: 150px;
  color: #fff;
  background: ${(props) => props.color};
  border: 1px solid #000000;
  border-radius: 50px;
`;

const Difficulty = () => {
  const navigate = useNavigate();

  return (
    <>
      <div className="flex justify-center flex-col gap-5">
        <h1 className="flex justify-center">DIFFICULTY</h1>
        <Diff color="#1a383a">
          <button onClick={() => navigate("/plan")}>Expert</button>
        </Diff>
        <Diff color="#244e50">
          <button onClick={() => navigate("/plan")}>Intermediate</button>
        </Diff>
        <Diff color="#98cfd3">
          <button onClick={() => navigate("/plan")}>Beginner</button>
        </Diff>
      </div>
    </>
  );
};

export default Difficulty;
