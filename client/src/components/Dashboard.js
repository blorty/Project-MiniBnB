// Dashboard.js
import React from "react";
import Jobs from "./Jobs";


const Dashboard = ({ user }) => {
  const jobsData = [
    // Add your job data here
  ];

  return (
    <div>
      <div className="mt-8 text-center text-xl">Welcome to Your Dashboard, {user}!</div>
      <div className="mt-8 text-center">Here are your jobs:</div>
      <Jobs jobs={jobsData} />
      {/* Render other details as needed */}
    </div>
  );
};



export default Dashboard;
