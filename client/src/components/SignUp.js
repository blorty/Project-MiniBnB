import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

const SignupForm = () => {
    const [customers, setCustomers] = useState([{}]);
    const [refreshPage, setRefreshPage] = useState(false);

    useEffect(() => {
        console.log("FETCH! ");
        fetch("/customers")
        .then((res) => res.json())
        .then((data) => {
            setCustomers(data);
            console.log(data);
        });
    }, [refreshPage]);

    const formSchema = yup.object().shape({
        email: yup.string().email("Invalid email").required("Must enter email"),
        name: yup.string().required("Must enter a name").max(15),
        age: yup
        .number()
        .positive()
        .integer()
        .required("Must enter age")
        .typeError("Please enter an Integer")
        .max(125),
    });

    const formik = useFormik({
        initialValues: {
        name: "",
        email: "",
        age: "",
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
        fetch("customers", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(values, null, 2),
        }).then((res) => {
            if (res.status === 200) {
            setRefreshPage(!refreshPage);
            }
        });
        },
    });

    return (
        <div>
        <form onSubmit={formik.handleSubmit} className="m-8">
            <label htmlFor="email" className="block mb-2">
            Email Address
            </label>
            <input
            id="email"
            name="email"
            onChange={formik.handleChange}
            value={formik.values.email}
            className="w-full px-4 py-2 mb-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            <p className="text-red-500">{formik.errors.email}</p>
            <label htmlFor="name" className="block mb-2">
            Name
            </label>
            <input
            id="name"
            name="name"
            onChange={formik.handleChange}
            value={formik.values.name}
            className="w-full px-4 py-2 mb-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            <p className="text-red-500">{formik.errors.name}</p>
            <label htmlFor="age" className="block mb-2">
            Age
            </label>
            <input
            id="age"
            name="age"
            onChange={formik.handleChange}
            value={formik.values.age}
            className="w-full px-4 py-2 mb-2 border rounded focus:outline-none focus:border-indigo-500"
            />
            <p className="text-red-500">{formik.errors.age}</p>
            <button
            type="submit"
            className="px-4 py-2 mt-4 text-white bg-indigo-500 rounded hover:bg-indigo-600 focus:outline-none focus:bg-indigo-600"
            >
            Submit
            </button>
        </form>
        <table className="p-4">
            <tbody>
            <tr>
                <th className="px-4 py-2">Name</th>
                <th className="px-4 py-2">Email</th>
                <th className="px-4 py-2">Age</th>
            </tr>
            {customers === undefined ? (
                <p>Loading</p>
            ) : (
                customers.map((customer, i) => (
                <tr key={i}>
                    <td className="px-4 py-2">{customer.name}</td>
                    <td className="px-4 py-2">{customer.email}</td>
                    <td className="px-4 py-2">{customer.age}</td>
                </tr>
                ))
            )}
            </tbody>
        </table>
        </div>
    );
};

export default SignupForm;
