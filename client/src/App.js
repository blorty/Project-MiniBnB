import React from "react";
import { BrowserRouter as Router, Switch} from "react-router-dom";
import NavBar from "./components/NavBar";

import './scrollbar.css'

import "./style.css";

function App() {

    return (
        <div >
        <Router>
        <Router>
            <NavBar />
            <Switch>

            </Switch>
        </Router>
        </Router>
        </div>
    );
}

export default App;
