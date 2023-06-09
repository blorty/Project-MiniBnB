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
            HOME 
          </span>
          <span className={`block text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-orange-600 ${reveal ? 'animation-reveal' : ''}`}>
            PAGE
          </span>
        </h1>
      </div>
    </div>
  );
}

export default Home;


//add creators to the page