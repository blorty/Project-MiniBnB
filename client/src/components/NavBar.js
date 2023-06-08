import React from 'react';
import { NavLink } from 'react-router-dom';

function NavBar() {
  const navLinks = [
    { path: '/', label: 'Home' },
    { path: '/jobs', label: 'Jobs' },
    { path: '/company-reviews', label: 'Company Reviews' },
    { path: '/salaries', label: 'Salaries' },
  ];

  return (
    <nav className="bg-creamcicle py-4">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-center">
        <div className="flex justify-center space-x-4">
          {navLinks.map((link) => (
            <NavLink
              key={link.path}
              exact
              to={link.path}
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
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
