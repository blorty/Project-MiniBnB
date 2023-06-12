import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./components/Home";
import Jobs from "./components/Jobs";
import CompanyReviews from "./components/CompanyReviews";
import Salaries from "./components/Salaries";
import Login from "./components/Login";
import SignUp from "./components/SignUp";

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
            <Footer />

        </Router>
        </Router>
        </div>
    );
}

export default App;
