import api from "./apiClient";
import type {
  RegisterPayload,
  LoginPayload,
  AuthResponse,
  User,
  TenantFull,
  StartCallResponse,
} from "./types";

// ----------------- ERROR HANDLER -----------------
async function handleRequest<T>(fn: () => Promise<T>): Promise<T> {
  try {
    return await fn();
  } catch (err: any) {
    console.error(err);

    // Axios error handling
    if (err.response?.data?.message) {
      throw new Error(err.response.data.message);
    } else if (err.message) {
      throw new Error(err.message);
    } else {
      throw new Error("Unknown error");
    }
  }
}

// ---------------- AUTH ----------------

export async function register(payload: RegisterPayload): Promise<AuthResponse> {
  return handleRequest(() => api.post("/register", payload).then((res) => res.data));
}

export async function login(payload: LoginPayload): Promise<AuthResponse> {
  return handleRequest(() => api.post("/login", payload).then((res) => res.data));
}

export async function getUserInfo(): Promise<User> {
  return handleRequest(() => api.get("/me").then((res) => res.data));
}

// ---------------- TENANT ----------------

export async function getTenantBot(): Promise<TenantFull> {
  return handleRequest(() => api.get("/tenant/bot").then((res) => res.data));
}

// ---------------- CALL CONTROL ----------------

export async function startCall(): Promise<StartCallResponse> {
  return handleRequest(() => api.post("/tenant/calls").then((res) => res.data));
}
