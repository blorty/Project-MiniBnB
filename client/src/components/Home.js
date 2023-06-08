import React from 'react';
import NavBar from './NavBar';

function Home() {
  return (
    <div className="bg-orange-200 h-screen flex flex-col justify-center items-center">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-4">Welcome to WorkWander</h1>
        <p className="text-lg mb-6">
          Find your dream job and explore company reviews and salaries.
        </p>
        <div className="flex mb-4">
          <input
            type="text"
            placeholder="Search for jobs"
            className="mr-2 px-4 py-2 rounded border border-gray-300"
          />
          <input
            type="text"
            placeholder="Location"
            className="mr-2 px-4 py-2 rounded border border-gray-300"
          />
          <button className="px-6 py-2 rounded bg-blue-500 text-white">
            Search
          </button>
        </div>
        <div>
          <button className="px-6 py-2 rounded bg-green-500 text-white mr-4">
            Get Started
          </button>
          <button className="px-6 py-2 rounded bg-gray-500 text-white">
            Learn More
          </button>
        </div>
      </div>
    </div>
  );
}

export default Home;
