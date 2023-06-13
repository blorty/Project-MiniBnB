// Dashboard.js
import React from "react";
import Jobs from "./Jobs";

const Dashboard = ({ user }) => {
  const jobsData = [
    // Add your job data here
  ];

  return (
    <div>
      <h1>Welcome to Your Dashboard, {user}!</h1>
      <h1>Here are your jobs:</h1>
      <Jobs jobs={jobsData} />
      {/* Render other details as needed */}
    </div>
  );
};

export default Dashboard;
