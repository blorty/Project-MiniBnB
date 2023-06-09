import React from 'react';
import { useState, useEffect } from 'react';

import cindy from '../creator_images/Cindy2.jpg';
import vadim from '../creator_images/Vadim.jpeg';
import josh from '../creator_images/Josh.jpeg';

function Home() {
  const [reveal, setReveal] = useState(false);

  useEffect(() => {
    setReveal(true);
  }, []);

  return (
    <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center">
      {/* Rest of the content */}
      <div className="creators-section mt-8">
        <h2 className="text-2xl font-bold mb-4">App Creators</h2>
        <div className="flex justify-center items-center space-x-8">
          <div className="pl-4">
            <img
              src={cindy}
              alt="Creator 1"
              className={`rounded-lg object-contain max-h-screen w-auto transition-transform duration-300 ease-in-out transform hover:scale-110 ${
                reveal ? 'opacity-100' : 'opacity-0'
              } hover:ring-2 ring-orange-500`}
            />
          </div>
          <div>
            <img
              src={vadim}
              alt="Creator 2"
              className={`rounded-lg object-contain max-h-screen w-auto transition-transform duration-300 ease-in-out transform hover:scale-110 ${
                reveal ? 'opacity-100' : 'opacity-0'
              } hover:ring-2 ring-orange-500`}
            />
          </div>
          <div className="pr-4">
            <img
              src={josh}
              alt="Creator 3"
              className={`rounded-lg object-contain max-h-screen w-auto transition-transform duration-300 ease-in-out transform hover:scale-110 ${
                reveal ? 'opacity-100' : 'opacity-0'
              } hover:ring-2 ring-orange-500`}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
