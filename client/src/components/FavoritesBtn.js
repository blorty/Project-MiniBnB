import React from 'react';
import { useHistory } from 'react-router-dom';

const FavoriteButton = () => {
  const history = useHistory();

  const handleClick = () => {
    history.push('/favorites');
  };

  return (
    <button
      className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded"
      onClick={handleClick}
    >
      Favorites
    </button>
  );
};

export default FavoriteButton;
