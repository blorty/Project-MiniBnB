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
      hobbies: ['Loves trying new restuarants', 'Reading', 'Video Editing'],
      languages: ['Python', 'JavaScript', 'HTML', 'CSS', 'React', 'Flask'],
      passions: ['Powerlifting', 'Coding', 'Traveling the world ❤️',],
    },
    github: 'https://github.com/cinhernandez',
  },
  {
    id: 2,
    name: 'Vadim',
    image: vadim,
    favorites: {
      hobbies: ['Loves going to car shows', 'Gaming (Counter Strike)', 'Dedicated camera man on nights out'],
      languages: ['Python', 'JavaScript', 'HTML', 'CSS', 'React', 'Flask'],
      passions: ['Bodybuilding', 'Coding', 'Hiking'],
    },
    github: 'https://github.com/blorty',
  },
  {
    id: 3,
    name: 'Josh',
    image: josh,
    favorites: {
      hobbies: ['Loves live music shows and festivals', 'Working out', 'Photography', 'Hiking'],
      languages: ['Python', 'JavaScript', 'HTML', 'CSS', 'React', 'Flask'],
      passions: ['Coding incredibly fast', 'Traveling the world', 'Photography'],
    },
    github: 'https://github.com/familymanjosh',
  },
];

function Home() {
  const [selectedCreator, setSelectedCreator] = useState(null);

  const handleCreatorClick = (creator) => {
    setSelectedCreator(creator);
  };

  return (
    <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center bg-gradient-to-b from-yellow-200 to-orange-300">
      <div className="creators-section mt-8">
        <h2 className="uppercase justify-center items-center text-white text-2xl font-bold px-4 py-2 transition-colors duration-300 hover:text-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">Founders</h2>
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
          <div className="mt-8 bg-white p-6 rounded-lg shadow-lg mx-auto max-w-screen-sm">
            <h3 className="text-xl font-bold text-indigo-500 text-center">{selectedCreator.name}</h3>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-indigo-500 text-center">Favorite Hobbies:</h4>
              <ul className="list-disc pl-6 text-indigo-500">
                {selectedCreator.favorites.hobbies.map((hobby) => (
                  <li key={hobby} className="text-base">{hobby}</li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-indigo-500 text-center">Favorite Languages to Write In:</h4>
              <ul className="list-disc pl-6 text-indigo-500">
                {selectedCreator.favorites.languages.map((language) => (
                  <li key={language} className="text-base">{language}</li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-indigo-500 text-center">Passions:</h4>
              <ul className="list-disc pl-6 text-indigo-500">
                {selectedCreator.favorites.passions.map((passion) => (
                  <li key={passion} className="text-base">{passion}</li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-semibold mt-4 text-indigo-500 text-center">GitHub:</h4>
              <p className="text-indigo-500 text-center">
                <a href={selectedCreator.github} target="_blank" rel="noopener noreferrer">
                  {selectedCreator.github}
                </a>
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Home;
