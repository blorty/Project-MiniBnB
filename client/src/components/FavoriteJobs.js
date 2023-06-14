import React from 'react';

const FavoriteJobs = ({ jobs, onDelete }) => {
  return (
    <div>
      {jobs.length === 0 ? (
        <p>No favorite jobs found.</p>
      ) : (
        jobs.map((job) => (
          <div key={job.id} className="bg-white rounded shadow p-4 m-4 space-y-4">
            <h2 className="text-xl font-bold">{job.title}</h2>
            <p className="text-gray-600 mb-2">{job.description}</p>
            <p className="text-gray-600 mb-2">{job.location}</p>
            <p className="text-gray-600 mb-2">{`$${job.salary}`}</p>
            <button
              className="bg-red-500 text-white font-semibold py-2 px-4 rounded"
              onClick={() => onDelete(job.id)}
            >
              Delete
            </button>
          </div>
        ))
      )}
    </div>
  );
};

export default FavoriteJobs;
