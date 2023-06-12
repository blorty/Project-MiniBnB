import React, { useState } from 'react';

function CreateJob({ onJobCreated }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };

  const handleCreateJob = () => {
    // Validate the input data before creating the job
    if (!title || !description) {
      alert('Please enter a title and description for the job');
      return;
    }

    // Create the job object
    const newJob = {
      title,
      description,
    };

    // Call the callback function to create the job
    onJobCreated(newJob);

    // Clear the input fields
    setTitle('');
    setDescription('');
  };

  return (
    <div className="max-w-md mx-auto bg-creamsicle p-6 rounded-lg shadow-lg">
      <h2 className="text-xl font-bold mb-4">Create Job Listing</h2>
      <div className="mb-4">
        <label htmlFor="title" className="text-sm font-medium">Title:</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={handleTitleChange}
          className="w-full px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
        />
      </div>
      <div className="mb-4">
        <label htmlFor="description" className="text-sm font-medium">Description:</label>
        <textarea
          id="description"
          value={description}
          onChange={handleDescriptionChange}
          className="w-full px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
        />
      </div>
      <button
        onClick={handleCreateJob}
        className="bg-orange-500 text-white font-semibold py-2 px-4 rounded hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
      >
        Create Job
      </button>
    </div>
  );
}

export default CreateJob;
