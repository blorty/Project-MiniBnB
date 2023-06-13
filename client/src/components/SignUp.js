import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';

const SignupForm = () => {
    const initialValues = {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
    };

    const validationSchema = Yup.object().shape({
        username: Yup.string()
        .min(3, 'Username must be at least 3 characters')
        .max(20, 'Username must be at most 20 characters')
        .required('Username is required'),
        email: Yup.string().email('Invalid email').required('Email is required'),
        password: Yup.string()
        .min(6, 'Password must be at least 6 characters')
        .required('Password is required'),
        confirmPassword: Yup.string()
        .oneOf([Yup.ref('password'), null], 'Passwords must match')
        .required('Confirm Password is required'),
    });

    const handleSubmit = (values, { setSubmitting }) => {
        fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
        })
        .then((response) => {
            if (response.ok) {
            // Registration successful
            // Redirect the user or perform other actions
            console.log('Registration successful');
            } else {
            // Registration failed
            // Handle error case
            console.log('Registration failed');
            }
        })
        .catch((error) => {
            console.log('Error registering:', error);
        })
        .finally(() => {
            setSubmitting(false);
        });
    };

    const formik = useFormik({
        initialValues,
        validationSchema,
        onSubmit: handleSubmit,
    });

    return (
        <div className="max-w-md mx-auto bg-white rounded shadow p-8">
        <h1 className="text-2xl font-bold mb-8">Sign Up</h1>
        <form onSubmit={formik.handleSubmit}>
            <div className="mb-4">
            <label htmlFor="username" className="block mb-2 font-semibold">
                Username
            </label>
            <input
                type="text"
                id="username"
                name="username"
                onChange={formik.handleChange}
                value={formik.values.username}
                className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            {formik.errors.username && (
                <div className="text-red-500">{formik.errors.username}</div>
            )}
            </div>
            <div className="mb-4">
            <label htmlFor="email" className="block mb-2 font-semibold">
                Email
            </label>
            <input
                type="email"
                id="email"
                name="email"
                onChange={formik.handleChange}
                value={formik.values.email}
                className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            {formik.errors.email && (
                <div className="text-red-500">{formik.errors.email}</div>
            )}
            </div>
            <div className="mb-4">
            <label htmlFor="password" className="block mb-2 font-semibold">
                Password
            </label>
            <input
                type="password"
                id="password"
                name="password"
                onChange={formik.handleChange}
                value={formik.values.password}
                className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            {formik.errors.password && (
                <div className="text-red-500">{formik.errors.password}</div>
            )}
            </div>
            <div className="mb-4">
            <label htmlFor="confirmPassword" className="block mb-2 font-semibold">
                Confirm Password
            </label>
            <input
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                onChange={formik.handleChange}
                value={formik.values.confirmPassword}
                className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            {formik.errors.confirmPassword && (
                <div className="text-red-500">{formik.errors.confirmPassword}</div>
            )}
            </div>
            <button
            type="submit"
            className="w-full bg-indigo-500 text-white font-semibold py-2 px-4 rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
            disabled={formik.isSubmitting}
            >
            Sign Up
            </button>
        </form>
        </div>
    );
};

export default SignupForm;