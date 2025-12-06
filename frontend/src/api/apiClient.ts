const API_BASE = "http://localhost:4000/users";

export interface RegisterPayload {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface AuthResponse {
  token: string;
}

export interface User {
  id: string;
  first_name: string;
  last_name: string;
  email: string;
}

export async function register(payload: RegisterPayload): Promise<AuthResponse> {
  const res = await fetch(`${API_BASE}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}

export async function login(payload: LoginPayload): Promise<AuthResponse> {
  const res = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}

export async function getUserInfo(): Promise<User> {
  const token = localStorage.getItem("token");
  const res = await fetch(`${API_BASE}/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}

export interface WebCallResponse {
  web_call_url: string;
  call_id: string;
}

export async function createWebCall(agentId: string): Promise<WebCallResponse> {
  const res = await fetch("https://api.retellai.com/v2/web-call/create", {
    method: "POST",
    headers: {
      Authorization: `Bearer YOUR_RETELL_API_KEY`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      agent_id: agentId,
      metadata: { source: "web" }
    }),
  });

  return res.json();
}
