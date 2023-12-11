import Home from "./components/Home.tsx";
import Plan from "./components/Plan.tsx";
import Difficulty from "./components/Difficulty.tsx";
import voluPath from "./img/volume.png";
import accessPath from "./img/access.png";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import styled from "styled-components";

const Disclaimer = styled.div`
  /* Home */
  text-align: center;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 10px;
  color: #adadad;
`;

function App() {
  return (
    <>
      <div className="flex flex-col h-screen w-screen">
        <div className="flex flex-row-reverse gap-5" alt="header-container">
          <img
            onClick={() => {}}
            src={voluPath}
            alt="Volume Logo"
            height="25"
            width="25"
          />
          <img
            onClick={() => {
              console.log("h1");
            }}
            src={accessPath}
            alt="Access Logo"
            height="25"
            width="25"
          />
        </div>
        <div className="flex justify-center" alt="body-container">
          <Router>
            <Routes>
              <Route path="/" element={<Home />} initial={true} />
              <Route path="/plan" element={<Plan />} />
              <Route path="/difficulty" element={<Difficulty />} />
            </Routes>
          </Router>
        </div>

        <div className="flex justify-center gap-4" alt="footer-container">
          <Disclaimer>
            Safety Dislaimer: We are not responsible for any injuries that occur
            during your workout
          </Disclaimer>
        </div>
      </div>
    </>
  );
}

export default App;
