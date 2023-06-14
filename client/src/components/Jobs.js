import React, { useEffect, useState } from 'react';
import CreateJob from './CreateJob';
import 'tailwindcss/tailwind.css';

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [numToShow, setNumToShow] = useState(5); // New state variable

  useEffect(() => {
    fetch('/jobs')
      .then((response) => response.json())
      .then((data) => setJobs(data))
      .catch((error) => console.log(error));
  }, []);

  const handleDelete = (jobId) => {
    fetch(`/jobs/${jobId}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.ok) {
          setJobs((prevJobs) => prevJobs.filter((job) => job.id !== jobId));
        } else {
          console.log('Failed to delete the job.');
        }
      })
      .catch((error) => {
        console.log('Error deleting the job:', error);
      });
  };

  const handleCreateJob = (newJob) => {
    fetch('/create_job', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newJob),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Job created successfully:', data);

        setJobs((prevJobs) => [data, ...prevJobs]); // Add the new job at the beginning of the jobs array
      })
      .catch((error) => {
        console.log('Error creating the job:', error);
      });
  };

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleShowMore = () => {
    setNumToShow(numToShow + 5); // Increase number of jobs shown by 5
  };

  const filteredJobs = jobs.filter((job) =>
    (job.title || '').toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center">
      <div className="mt-8 text-center">
        <div className="mb-4">
          <input
            type="text"
            placeholder="Search for jobs"
            className="px-4 py-2 mb-4 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
            value={searchTerm}
            onChange={handleSearch}
          />
          <CreateJob onJobCreated={handleCreateJob} />
        </div>
        {filteredJobs.slice(0, numToShow).map((job) => (
          <div key={job.id} className="bg-white rounded shadow p-4 m-4 space-y-4">
            <h2 className="text-xl font-bold">{job.title}</h2>
            <p className="text-gray-600 mb-2">{job.description}</p>
            <p className="text-gray-600 mb-2">{job.location}</p>
            <p className="text-gray-600 mb-2">{`$${job.salary}`}</p>
            <button
              className="bg-red-500 text-white font-semibold py-2 px-4 rounded"
              onClick={() => handleDelete(job.id)}
            >
              Delete
            </button>
          </div>
        ))}
        {numToShow < filteredJobs.length && ( // Only show 'Show More' button if there are more jobs to show
          <button
            onClick={handleShowMore}
            className="mt-4 mb-8 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Show More
          </button>
        )}
      </div>
    </div>
  );
}

export default Jobs;
