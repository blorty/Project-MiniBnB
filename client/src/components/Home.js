import React from 'react';
import { useState, useEffect } from 'react';

function Home() {

  const [reveal, setReveal] = useState(false);

  useEffect(() => {
    setReveal(true);
  }, []);

  return (
    <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center">
      <div className="text-center mt-8">
        <h1 className="text-4xl font-bold mb-4">
          <span className={`block ${reveal ? 'opacity-100' : 'opacity-0'}`}>
            Welcome to
          </span>
          <span className={`block text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-orange-600 ${reveal ? 'animation-reveal' : ''}`}>
            WorkWander
          </span>
        </h1>
        <p className="text-lg mb-6">
          Find your dream job and explore company reviews and salaries.
        </p>
        <div className="flex items-center space-x-4 mb-4">
          <input
            type="text"
            placeholder="Search for jobs"
            className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
          <input
            type="text"
            placeholder="Location"
            className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
          <button className="px-6 py-2 rounded bg-orange-500 text-white hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
            Search
          </button>
        </div>
        <div>
          <button className="px-6 py-2 rounded bg-orange-500 text-white hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500 mr-4">
            Get Started
          </button>
          <button className="px-6 py-2 rounded bg-orange-500 text-white hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
            Learn More
          </button>
        </div>
      </div>
    </div>
  );
}

export default Home;
