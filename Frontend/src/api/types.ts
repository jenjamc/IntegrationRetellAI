// -------------------- AUTH --------------------

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

// -------------------- TENANT --------------------

export interface Call {
  call_id: string;
  tenant_id: number;
  status: string;
  started_at: string;
  ended_at: string | null;
  billed_seconds: number;
  cost_dollars: number;
}

export interface Balance {
  current_balance: number;
}

export interface TenantBot {
  agent_id: string;
  agent_name: string;
}

export interface TenantFull extends TenantBot {
  calls: Call[];
  balance: Balance;
}

// -------------------- START / END CALL --------------------

export interface StartCallResponse {
  call_id: string;
  access_token: string;
}

export interface EndCallResponse {
  success: boolean;
}
