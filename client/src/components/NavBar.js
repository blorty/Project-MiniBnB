import React from 'react';
import { NavLink, Link, BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './Home';
import Jobs from './Jobs';
import LoginForm from './LogIn';
import SignUpForm from './SignUp';
import CreateJob from './CreateJob'; // Import the CreateJob component

import logo from '../WorkWanderer3.png';

const navComponents = [
  { component: Home, path: '/', label: 'Home' },
  { component: Jobs, path: '/jobs', label: 'Find Jobs' },
  { component: LoginForm, path: '/login', label: 'Log In' },
  { component: SignUpForm, path: '/signup', label: 'Sign Up' },
  { component: CreateJob, path: '/createjob', label: 'Create Job' }
  // Add more components and their paths here
];

function NavBar() {
  return (
    <Router>
      <nav className="sticky py-4">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          {/* Top Section */}
          <div className="flex flex-col justify-center items-center mb-4">
            <Link to="/" className="flex items-center">
              <img
                src={logo}
                alt="Logo"
                className="h-12 w-12 mr-2 transition-transform duration-300 ease-in-out transform hover:scale-110"
              />
              <span className="text-orange-500 text-2xl font-bold transform hover:scale-110 px-4 py-2 transition-colors duration-300 hover:text-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
                WorkWander
              </span>
            </Link>
          </div>

          {/* Bottom Section */}
          <div className="flex justify-center items-center space-x-4">
            {navComponents.map((navComponent) => (
              <NavLink
                key={navComponent.path}
                exact
                to={navComponent.path}
                className="inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
                activeClassName="active"
              >
                {navComponent.label}
              </NavLink>
            ))}
          </div>
        </div>
      </nav>

      <Switch>
        {navComponents.map((navComponent) => (
          <Route key={navComponent.path} exact path={navComponent.path} component={navComponent.component} />
        ))}
      </Switch>
    </Router>
  );
}

export default NavBar;
