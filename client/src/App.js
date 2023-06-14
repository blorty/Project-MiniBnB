import React, { useState } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'; // import Redirect
import NavBar from './components/NavBar';
import Home from './components/Home';
import JobsOnly from './components/JobsOnly';
import Dashboard from './components/Dashboard';
import SignUp from './components/SignUp';
import LoginForm from './components/LogIn';

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false); 

    const handleLogout = () => {
        setIsLoggedIn(false); 
    };

    return (
        <div>
        <Router>
            <NavBar isLoggedIn={isLoggedIn} handleLogout={handleLogout} />
            <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/jobs" component={JobsOnly} />
            <Route exact path="/signup" component={SignUp} />
            <Route 
                exact path="/login"
                render={(props) => <LoginForm {...props} setIsLoggedIn={setIsLoggedIn} />}
            />
            <Route
                exact path="/dashboard"
                render={(props) =>
                isLoggedIn ? (
                    <Dashboard {...props} />
                ) : (
                    <Redirect to="/login" />
                )
                }
            />
            </Switch>
        </Router>
        </div>
    );
}

export default App;
