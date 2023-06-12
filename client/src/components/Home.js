import React, { useState } from 'react';

import cindy from '../creator_images/Cindy2.jpg';
import vadim from '../creator_images/Vadim.jpeg';
import josh from '../creator_images/Josh.jpeg';

const creatorsData = [
  {
    id: 1,
    name: 'Cindy',
    image: cindy,
    favorites: {
      hobbies: ['Loves power lifting', 'Enjoys nights out with good company', 'Hobby 3'],
      languages: ['Python', 'JavaScript', 'HTML'],
      passions: ['Coding', 'Traveling the world <3', 'Scrolling through Hinge'],
    },
  },
  {
    id: 2,
    name: 'Vadim',
    image: vadim,
    favorites: {
      hobbies: ['Loves going to car shows', 'Gaming (Counter Strike)', 'Dedicated camera man on nights out'],
      languages: ['JavaScript', 'Python', 'CSS'],
      passions: ['Bodybuilding', 'Coding', 'Hiking'],
    },
  },
  {
    id: 3,
    name: 'Josh',
    image: josh,
    favorites: {
      hobbies: ['Loves live music show and festivals', 'Working out', 'Hobby 3'],
      languages: ['Python', 'React', 'Ruby'],
      passions: ['Coding incredibly fast', 'Passion 8', 'Passion 9'],
    },
  },
];

function Home() {
  const [selectedCreator, setSelectedCreator] = useState(null);

  const handleCreatorClick = (creator) => {
    setSelectedCreator(creator);
  };

  return (
    <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center bg-gradient-to-b from-yellow-200 to-orange-300">
      {/* Rest of the content */}
      <div className="creators-section mt-8">
        <h2 className=" uppercase justify-center items-center text-white text-2xl font-bold px-4 py-2 transition-colors duration-300 hover:text-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">Founders</h2>
        <div className="flex justify-center items-center space-x-8">
          {creatorsData.map((creator) => (
            <div key={creator.id}>
              <img
                src={creator.image}
                alt={creator.name}
                className="pl-4 pr-4 overflow-hidden rounded-xl object-contain max-h-screen w-auto transition-transform duration-300 ease-in-out transform hover:scale-110 cursor-pointer"
                onClick={() => handleCreatorClick(creator)}
              />
            </div>
          ))}
        </div>
        {selectedCreator && (
          <div className="mt-8">
            <h3 className="text-xl font-bold text-orange-500">{selectedCreator.name}</h3>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-orange-500">Favorite Hobbies:</h4>
              <ul className="list-disc pl-6 text-orange-500">
                {selectedCreator.favorites.hobbies.map((hobby) => (
                  <li key={hobby} className="text-base">{hobby}</li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-orange-500">Favorite Languages to Write In:</h4>
              <ul className="list-disc pl-6 text-orange-500">
                {selectedCreator.favorites.languages.map((language) => (
                  <li key={language} className="text-base">{language}</li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-orange-500">Passions:</h4>
              <ul className="list-none hover:list-disc inline-flex items-center transition-transform duration-300 ease-in-out transform hover:scale-110 px-4 py-2 border border-transparent text-md font-medium rounded-md text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
                {selectedCreator.favorites.passions.map((passion) => (
                  <li key={passion} className="text-base">{passion}</li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Home;
