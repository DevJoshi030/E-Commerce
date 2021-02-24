import React from "react";
import { render } from "react-dom";

const Main = () => {
  return (
    <div>
      <h1>Hello</h1>
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<Main />, appDiv);

export default Main;
