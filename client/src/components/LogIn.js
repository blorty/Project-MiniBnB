import React from "react";
import { Formik, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

const LoginForm = () => {
    const initialValues = {
        email: "",
        password: "",
    };

    const validationSchema = Yup.object().shape({
        email: Yup.string().email("Invalid email").required("Email is required"),
        password: Yup.string().required("Password is required"),
    });

    const handleSubmit = (values, { setSubmitting }) => {
        setTimeout(() => {
        alert(JSON.stringify(values, null, 2));
        setSubmitting(false);
        }, 500);
    };

    return (
        <div className="max-w-md mx-auto bg-white rounded shadow p-8">
        <h1 className="text-2xl font-bold mb-8">Login</h1>
        <Formik
            initialValues={initialValues}
            validationSchema={validationSchema}
            onSubmit={handleSubmit}
        >
            {({ isSubmitting }) => (
            <form>
                <div className="mb-4">
                <label htmlFor="email" className="block mb-2 font-semibold">
                    Email
                </label>
                <Field
                    type="email"
                    id="email"
                    name="email"
                    className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
                />
                <ErrorMessage name="email" component="div" className="text-red-500" />
                </div>
                <div className="mb-4">
                <label htmlFor="password" className="block mb-2 font-semibold">
                    Password
                </label>
                <Field
                    type="password"
                    id="password"
                    name="password"
                    className="w-full px-4 py-2 border rounded focus:outline-none focus:border-indigo-500"
                />
                <ErrorMessage name="password" component="div" className="text-red-500" />
                </div>
                <button
                type="submit"
                className="w-full bg-indigo-500 text-white font-semibold py-2 px-4 rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                disabled={isSubmitting}
                >
                Login
                </button>
            </form>
            )}
        </Formik>
        </div>
    );
};

export default LoginForm;
