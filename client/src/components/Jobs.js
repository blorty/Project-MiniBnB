import React, { useEffect, useState } from 'react';
import CreateJob from './CreateJob';
import 'tailwindcss/tailwind.css';

function Jobs() {
    const [jobs, setJobs] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [visibleJobs, setVisibleJobs] = useState(10);

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
            // Job deleted successfully
            // Update the jobs state by removing the deleted job
            setJobs((prevJobs) => prevJobs.filter((job) => job.id !== jobId));
            } else {
            // Handle error case
            console.log('Failed to delete the job.');
            }
        })
        .catch((error) => {
            console.log('Error deleting the job:', error);
        });
    };

    const handleCreateJob = (newJob) => {
        fetch('/jobs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newJob),
        })
        .then((response) => response.json())
        .then((data) => {
            // Handle the response from the backend
            console.log('Job created successfully:', data);

            // Add the new job to the jobs state
            setJobs((prevJobs) => [...prevJobs, data]);
        })
        .catch((error) => {
            console.log('Error creating the job:', error);
        });
    };

    const handleSearch = (e) => {
        setSearchTerm(e.target.value);
    };

    const filteredJobs = jobs.filter((job) =>
        job.title.toLowerCase().includes(searchTerm.toLowerCase())
    );

    const visibleJobItems = filteredJobs.slice(0, visibleJobs);

    const handleShowMore = () => {
        setVisibleJobs((prevVisibleJobs) => prevVisibleJobs + 10);
    };

    return (
        <div className="bg-gradient-animation min-h-screen flex flex-col justify-start items-center">
        <div className="mt-8 text-center">
            <div className="mb-4">
            <input
                type="text"
                placeholder="Search for jobs"
                className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500"
                value={searchTerm}
                onChange={handleSearch}
            />
            <CreateJob onJobCreated={handleCreateJob} />
            </div>
            {visibleJobItems.map((job) => (
            <div key={job.id} className="bg-white rounded shadow p-4 m-4">
                <h2 className="text-xl font-bold">{job.title}</h2>
                <p className="text-gray-600 mb-2">{job.description}</p>
                <p className="text-gray-600 mb-2">{job.location}</p>
                <p className="text-gray-600 mb-2">{`$ ${job.salary}`}</p>
                <button
                className="bg-red-500 text-white font-semibold py-2 px-4 rounded"
                onClick={() => handleDelete(job.id)}
                >
                Delete
                </button>
            </div>
            ))}
            {visibleJobs < filteredJobs.length && (
            <button
                className="bg-blue-500 text-white font-semibold py-2 px-4 rounded"
                onClick={handleShowMore}
            >
                Show More
            </button>
            )}
        </div>
        </div>
    );
}

export default Jobs;
