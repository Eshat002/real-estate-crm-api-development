"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function CustomersPage() {
  const router = useRouter();
  const [customers, setCustomers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCustomers = async () => {
      const token = localStorage.getItem("access");

      if (!token) {
        router.push("/login"); // redirect if not logged in
        return;
      }

      try {
        const res = await fetch("http://127.0.0.1:8000/api/v1/customers/", {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        if (res.status === 401) {
          // token invalid/expired
          router.push("/login");
          return;
        }

        if (!res.ok) throw new Error("Failed to fetch customers");

        const data = await res.json();
        setCustomers(data.results || data); // DRF pagination check
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchCustomers();
  }, [router]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div style={{ maxWidth: "800px", margin: "50px auto" }}>
      <h1>Customers</h1>
      <ul>
        {customers.map((customer: any) => (
          <li key={customer.id}>
            {customer.name} — {customer.email} — {customer.phone}
          </li>
        ))}
      </ul>
    </div>
  );
}
