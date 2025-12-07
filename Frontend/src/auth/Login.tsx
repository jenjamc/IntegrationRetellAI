import { useState } from "react";
import { login } from "../api/api";
import { useNavigate } from "react-router-dom";
import type { FormEvent } from "react";
import type { LoginPayload } from "../api/types";

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState<LoginPayload>({
    email: "",
    password: "",
  });

  async function submit(e: FormEvent) {
    e.preventDefault();

    const data = await login(form);
    if (data.token) {
      localStorage.setItem("token", data.token);
      navigate("/");
    }
  }

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={submit}>
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

        <button>Login</button>
      </form>
    </div>
  );
}
