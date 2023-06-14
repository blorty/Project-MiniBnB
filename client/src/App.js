import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import Home from './components/Home';
import Jobs from './components/Jobs';
import Dashboard from './components/Dashboard';
import SignUp from './components/SignUp';
import LogIn from './components/LogIn';

function App() {
    return (
        <div>
        <Router>
            <NavBar />
            <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/jobs" component={Jobs} />
            <Route exact path="/dashboard" component={Dashboard} />
            <Route exact path="/signup" component={SignUp} />
            <Route exact path="/login" component={LogIn} />
            </Switch>
        </Router>
        </div>
    );
}

export default App;
