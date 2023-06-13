import React, { useState, useEffect } from "react";
import {  Link } from "react-router-dom";

const Companies = () => {
  const [companies, setCompanies] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetch("/companies")
      .then((response) => response.json())
      .then((data) => setCompanies(data))
      .catch((error) => console.log(error));
  }, []);

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  }

  const filteredCompanies = companies.filter((company) =>
    company.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="container mx-auto py-8">
      <h1 className="text-2xl font-bold mb-4">Company List</h1>

      <input
        type="text"
        className="border border-gray-300 rounded-md px-4 py-2 mb-4"
        placeholder="Search..."
        value={searchTerm}
        onChange={handleSearch}
      />

      {filteredCompanies.length > 0 ? (
        <ul className="space-y-4">
          {filteredCompanies.map((company) => (
            <li
              key={company.id}
              className="border border-gray-300 rounded-md p-4"
            >
              <h2 className="text-lg font-bold mb-2">{company.name}</h2>
              <p>{company.description}</p>
              <Link
                to={`/companies/${company.id}`}
                className="bg-blue-500 hover:bg-blue-600 text-white rounded-md px-4 py-2 mt-4 inline-block"
              >
                View Details
              </Link>
            </li>
          ))}
        </ul>
      ) : (
        <p>No companies found.</p>
      )}
    </div>
  );
};

export default Companies;
