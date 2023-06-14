import React, { useState } from 'react';
import Jobs from './Jobs';
import FavoriteJobs from './FavoriteJobs';
import 'tailwindcss/tailwind.css';
import FavoriteButton from './FavoritesBtn';

const Dashboard = ({ user, isLoggedIn, handleLogout }) => {
  const jobsData = [
    // Add your job data here
  ];

  const [showFavorites, setShowFavorites] = useState(false);

  const handleToggleFavorites = () => {
    setShowFavorites(!showFavorites);
  };

  return (
    <div className="flex flex-col items-center mt-10">
      <h1 className="uppercase text-3xl font-bold mb-8 text-center text-blue-700">
        Welcome to Your Dashboard, {user}
      </h1>
      {isLoggedIn && (
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
          onClick={handleToggleFavorites}
        >
          {showFavorites ? 'Show All Jobs' : 'Show Favorite Jobs'}
        </button>
      )}
      <div className="text-xl mb-4 font-bold text-center text-blue-500">
        {showFavorites ? 'Here are your favorite jobs:' : 'Here are all jobs:'}
      </div>
      <div className="w-full max-w-l">
        {showFavorites ? (
          <FavoriteJobs jobs={jobsData} onDelete={() => {}} />
        ) : (
          <FavoriteButton />, 
          <Jobs jobs={jobsData} />
        )}
        
      </div>
    </div>
  );
};

export default Dashboard;
