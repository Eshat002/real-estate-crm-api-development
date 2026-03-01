// app/logout/page.tsx
"use client"; // must be client component

import LogoutButton from "@/components/LogoutButton";

export default function LogoutPage() {
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>You are about to log out</h2>
      <p>Click the button below to log out safely:</p>
      <LogoutButton />
    </div>
  );
}
