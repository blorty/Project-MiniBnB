import React from "react";
import Jobs from "./Jobs";
import { useHistory } from 'react-router-dom';

const Dashboard = ({ user, isLoggedIn, handleLogout }) => {
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

  const jobsData = [
    // Add your job data here
  ];

  return (
    <div>
      <div className="mt-8 text-center text-xl">Welcome to Your Dashboard, {user}!</div>
      <div className="mt-8 text-center">Here are your jobs:</div>
      <Jobs jobs={jobsData} />

      {isLoggedIn && (
        <button
          className="inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
          onClick={handleLogoutClick}
        >
          Logout
        </button>
      )}
    </div>
  );
};

export default Dashboard;
