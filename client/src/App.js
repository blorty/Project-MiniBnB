import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import './scrollbar.css'

import "./style.css";

function App() {
    return (
        <div >
        <Router>
            <NavBar />
            <Switch>
            {/* Add more routes here */}
            </Switch>
        </Router>
        </div>
    );
}

export default App;
