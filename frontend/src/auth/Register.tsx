import { useState } from "react";
import { register } from "../api/apiClient";
import type { RegisterPayload } from "../api/apiClient";
import { useNavigate } from "react-router-dom";
import type { FormEvent } from "react";

export default function Register() {
  const navigate = useNavigate();
  const [form, setForm] = useState<RegisterPayload>({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  async function submit(e: FormEvent) {
    e.preventDefault();

    const data = await register(form);
    if (data.token) {
      localStorage.setItem("token", data.token);
      navigate("/");
    }
  }

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={submit}>
        <input
          placeholder="First name"
          value={form.first_name}
          onChange={(e) => setForm({ ...form, first_name: e.target.value })}
        />

        <input
          placeholder="Last name"
          value={form.last_name}
          onChange={(e) => setForm({ ...form, last_name: e.target.value })}
        />

        <input
          placeholder="Email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />

        <input
          placeholder="Password"
          type="password"
          value={form.password}
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />

        <button>Register</button>
      </form>
    </div>
  );
}
