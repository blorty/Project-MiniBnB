import React from 'react';
import Jobs from './Jobs';

const Dashboard = ({ user, isLoggedIn, handleLogout }) => {
  const jobsData = [
    // Add your job data here
  ];

  return (
    <div className="flex flex-col items-center mt-10">
      <h1 className="uppercase text-3xl font-bold mb-8 text-center text-blue-700">Welcome to Your Dashboard, {user}</h1>
      <div className="text-xl mb-4 font-bold text-center text-blue-500">Here are your jobs:</div>
      <div className="w-full max-w-l">
        <Jobs jobs={jobsData} />
      </div>
    </div>
  );
};

export default Dashboard;
