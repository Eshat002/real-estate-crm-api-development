"use client";

import { useState } from "react";

export default function RegisterPage() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    re_password: "",
  });

  const [error, setError] = useState<any>(null);
  const [success, setSuccess] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess("");

    try {
      const res = await fetch("http://127.0.0.1:8000/api/auth/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data);
      } else {
        setSuccess("Account created successfully!");
        setFormData({
          username: "",
          email: "",
          password: "",
          re_password: "",
        });
      }
    } catch (err) {
      setError({ detail: "Something went wrong" });
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto" }}>
      <h1>Register</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <br />
        <br />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <br />
        <br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <br />
        <br />

        <input
          type="password"
          name="re_password"
          placeholder="Confirm Password"
          value={formData.re_password}
          onChange={handleChange}
          required
        />
        <br />
        <br />

        <button type="submit">Register</button>
      </form>

      {success && <p style={{ color: "green" }}>{success}</p>}

      {error && (
        <div style={{ color: "red" }}>
          {Object.keys(error).map((key) => (
            <p key={key}>
              {key}: {error[key]}
            </p>
          ))}
        </div>
      )}
    </div>
  );
}
