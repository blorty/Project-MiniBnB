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
            <h1>Company Details</h1>
            <h2 className="text-xl font-bold">{company.name}</h2>
            <p className="text-gray-600 mb-2">{company.industry}</p>
            <a href={company.website}>{company.website}</a>
            <h1>Jobs</h1>
            <ul>
                {company.jobs.map((job) => (
                    <li key={job.id}className="bg-white rounded shadow p-4 m-4">
                    <h2 className="text-xl font-bold">{job.title}</h2>
                    <p className="text-gray-600 mb-2">{job.description}</p>
                    <p className="text-gray-600 mb-2">{job.location}</p>
                    <p className="text-gray-600 mb-2">{job.salary}</p>
                    </li>
                ))}
            </ul>
            {/* Render other details as needed */}
        </div>
    );
};

export default CompanyDetails;
