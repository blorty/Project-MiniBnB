import React from 'react';
import { NavLink, Link, useHistory} from 'react-router-dom';

import logo from '../WorkWanderer3.png';

function NavBar({ isLoggedIn, handleLogout}) {
  const navLinks = [
    // { path: '/', label: 'Home' },
    { path: '/jobs', label: 'Jobs' },
    { path: '/dashboard', label: 'Dashboard', isPrivate: true },
  ];

  const history = useHistory();

  const handleLogoutClick = async () => {
    if (window.confirm('Are you sure you want to logout?')) {
      try {
        const response = await fetch('/logout', {
          method: 'POST',
        });

        if (response.ok) {
          handleLogout(); // Call the handleLogout function passed from the parent component
          history.push('/');
        } else {
          console.error('Logout failed');
        }
      } catch (error) {
        console.error(error);
      }
    }
  };

  return (
    <nav className="sticky py-4">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
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
          <div className="flex justify-end items-center space-x-4">
            {!isLoggedIn ? (
              <>
                <NavLink
                  to="/signup"
                  className="inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
                  activeClassName="active"
                >
                  Sign Up
                </NavLink>
                <NavLink
                  to="/login"
                  className="inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
                  activeClassName="active"
                >
                  Log In
                </NavLink>
              </>
            ) : (
              <button
                onClick={handleLogoutClick}
                className="inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
              >
                Logout
              </button>
            )}
          </div>
        </div>
        <div className="flex justify-center items-center space-x-4">
          {navLinks.map((link) => (
            <NavLink
              key={link.path}
              exact
              to={link.path}
              className="inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
              activeClassName="active"
            >
              {link.label}
            </NavLink>
          ))}
        </div>
      </div>
    </nav>
  );
}
  

export default NavBar;
