import { useEffect, useState, useRef } from "react";
import { getUserInfo, getTenantBot, startCall } from "../api/api";
import type { User, TenantFull, Call } from "../api/types";
import { RetellWebClient } from "retell-client-js-sdk";

const COST_PER_MIN = 0.4;

export default function HomePage() {
  const [user, setUser] = useState<User | null>(null);
  const [tenant, setTenant] = useState<TenantFull | null>(null);
  const [loading, setLoading] = useState(true);
  const [callId, setCallId] = useState<string | null>(null);
  const [liveDuration, setLiveDuration] = useState<number>(0); // in ms

  const retellClient = useRef<RetellWebClient | null>(null);
  const intervalRef = useRef<number | null>(null); // browser-friendly type

  useEffect(() => {
    retellClient.current = new RetellWebClient();
  }, []);

  async function loadAll() {
    try {
      const [u, t] = await Promise.all([getUserInfo(), getTenantBot()]);
      setUser(u);
      setTenant(t);
    } catch (err) {
      // alert handled globally in Axios
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadAll();
  }, []);

  // Track ongoing call duration
  useEffect(() => {
    if (callId) {
      intervalRef.current = window.setInterval(() => {
        setLiveDuration((prev) => prev + 1000); // increment every second
      }, 1000);
    } else if (intervalRef.current) {
      clearInterval(intervalRef.current);
      setLiveDuration(0);
      intervalRef.current = null;
    }

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
    };
  }, [callId]);

  const getLiveCost = () => {
    const minutes = liveDuration / 60000; // ms → minutes
    const cost = minutes * COST_PER_MIN;
    return (cost < COST_PER_MIN && liveDuration > 0 ? COST_PER_MIN : cost).toFixed(2);
  };

  async function handleStartCall() {
    try {
      const { call_id, access_token } = await startCall();
      setCallId(call_id);
      await retellClient.current?.startCall({ accessToken:access_token });
      setLiveDuration(0);
      loadAll();
      setTimeout(() => {
        loadAll();
      }, 2000);
    } catch (err) {
      // alert handled globally
    }
  }

  async function handleEndCall() {
    if (!callId) return;
    try {
      retellClient.current?.stopCall();
      setCallId(null);
      setLiveDuration(0);
      setTimeout(() => {
        loadAll();
      }, 2000);
    } catch (err) {
      // alert handled globally
    }
  }

  if (loading) return <div style={{ padding: 30 }}>Loading...</div>;

  const totalCalls = tenant?.calls.length ?? 0;

  return (
    <div style={{ padding: 30 }}>
      <h1>Dashboard</h1>

      <h2>User Info</h2>
      <p>
        {user?.first_name} {user?.last_name} ({user?.email})
      </p>

      <h2>Bot Info</h2>
      <p>
        <strong>Agent ID:</strong> {tenant?.agent_id}
      </p>
      <p>
        <strong>Agent Name:</strong> {tenant?.agent_name}
      </p>

      <h2>Balance</h2>
      <p>
        <strong>
           {tenant ? Number(tenant.balance.current_balance).toFixed(2) : "0.00"}
        </strong>
      </p>

      <h2>Total Calls</h2>
      <p>{totalCalls}</p>

      <div style={{ marginTop: 25 }}>
        {callId ? (
          <>
            <button
              onClick={handleEndCall}
              style={{ background: "red", color: "white", padding: "10px 20px" }}
            >
              End Call
            </button>
            <p style={{ marginTop: 10 }}>
              <strong>Live Duration:</strong> {(liveDuration / 1000).toFixed(0)} sec
              <br />
              <strong>Live Cost:</strong> ${getLiveCost()}
            </p>
          </>
        ) : (
          <button
            onClick={handleStartCall}
            style={{ padding: "10px 20px" }}
            disabled={!tenant || Number(tenant.balance.current_balance) <= 0}
          >
            Start Call
          </button>
        )}
      </div>

      <h2 style={{ marginTop: 40 }}>Call History</h2>
      {tenant?.calls.length === 0 ? (
        <p>No calls</p>
      ) : (
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={th}>Call ID</th>
              <th style={th}>Status</th>
              <th style={th}>Start</th>
              <th style={th}>End</th>
              <th style={th}>Billed (sec)</th>
              <th style={th}>Cost ($)</th>
            </tr>
          </thead>
          <tbody>
            {tenant?.calls.map((c: Call) => (
              <tr key={c.call_id}>
                <td style={td}>{c.call_id}</td>
                <td style={td}>{c.status}</td>
                <td style={td}>{new Date(c.started_at).toLocaleString()}</td>
                <td style={td}>
                  {c.ended_at ? new Date(c.ended_at).toLocaleString() : "—"}
                </td>
                <td style={td}>{c.billed_seconds}</td>
                <td style={td}>
                   ${c.cost_dollars ? Number(c.cost_dollars).toFixed(2) : "0.00"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

const th: React.CSSProperties = {
  borderBottom: "1px solid #ccc",
  padding: "8px",
  textAlign: "left",
};

const td: React.CSSProperties = {
  borderBottom: "1px solid #eee",
  padding: "8px",
};
