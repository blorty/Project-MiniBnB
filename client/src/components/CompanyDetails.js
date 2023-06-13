import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const CompanyDetails = () => {

    const [company, setCompany] = useState(null);
    const { id } = useParams();

    useEffect(() => {
        fetch(`/companies/${id}`)
            .then((response) => response.json())
            .then((data) => setCompany(data))
            .catch((error) => console.log(error));
    }, [id]);

    if (!company) {
        return <p>Loading...</p>;
    }

    return (
        <div>
            <h1 className="text-3xl font-bold mb-4">Company Details</h1>
            <div className="bg-gray-100 rounded-lg shadow-lg p-6 mb-8">
                <h1 className="text-xl font-bold mb-2">{company.name}</h1>
                <h1 className="text-gray-600 mb-2">{company.industry}</h1>
                <h1 className="text-gray-600 mb-2">
                    <a href={company.website} className="text-blue-500 hover:underline">{company.website}</a>
                </h1>
            </div>
            <h1 className="text-3xl font-bold mb-4">Jobs</h1>
            <ul>
                {company.jobs.map((job) => (
                    <li key={job.id} className="bg-gray-100 rounded-lg shadow-lg p-6 mb-8">
                        <h1 className="text-xl font-bold mb-2">{job.title}</h1>
                        <h1 className="text-gray-600 mb-2">{job.description}</h1>
                        <h1 className="text-gray-600 mb-2">{job.location}</h1>
                        <h1 className="text-gray-600 mb-2">{job.salary}</h1>
                    </li>
                ))}
            </ul>
            {/* Render other details as needed */}
        </div>
    );
};

export default CompanyDetails;
