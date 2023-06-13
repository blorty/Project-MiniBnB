// LoginForm.js
import React, { useState } from "react";
import { useHistory } from "react-router-dom";

const LoginForm = () => {
  const history = useHistory();
  const [values, setValues] = useState({
    email: "",
    password: ""
  });
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues({ ...values, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setErrors(validateForm(values));
    setIsSubmitting(true);

    if (Object.keys(errors).length === 0) {
      console.log("Submitting login request with values:", values);
      fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((response) => {
          console.log("Received response:", response);
          if (response.ok) {
            console.log("Login successful");
            // Authentication successful
            // Redirect the user to another route
            history.push("/dashboard");
          } else {
            console.log("Login failed");
            // Authentication failed
            // Handle error case
          }
        })
        .catch((error) => {
          console.log("Error logging in:", error);
        })
        .finally(() => {
          setIsSubmitting(false);
        });
    } else {
      console.log("Form validation errors:", errors);
    }
  };

  const validateForm = (values) => {
    let errors = {};
    if (!values.email) {
      errors.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(values.email)) {
      errors.email = "Invalid email address";
    }
    if (!values.password) {
      errors.password = "Password is required";
    }
    return errors;
  };

  return (
    <div className="max-w-md mx-auto bg-white rounded shadow p-8">
      <h1 className="text-2xl font-bold mb-8">Login</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="email" className="block mb-2 font-semibold">
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={values.email}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
          />
          {errors.email && <div className="text-red-500">{errors.email}</div>}
        </div>
        <div className="mb-4">
          <label htmlFor="password" className="block mb-2 font-semibold">
            Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            value={values.password}
            onChange={handleChange}
            className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
          />
          {errors.password && <div className="text-red-500">{errors.password}</div>}
        </div>
        <button
          type="submit"
          className="w-full bg-indigo-500 text-white font-semibold py-2 px-4 rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
          disabled={isSubmitting}
        >
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginForm;
