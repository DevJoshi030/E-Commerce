import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Admin from "./Admin";
import Home from "./Home";

const Main = () => {
  return (
    <div>
      <Router>
        <Switch>
          <Route path="/admin-api" component={Admin} />
          <Route exact path="/" component={Home} />
        </Switch>
      </Router>
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<Main />, appDiv);

export default Main;
