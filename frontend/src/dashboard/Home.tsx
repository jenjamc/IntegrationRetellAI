import { useState } from "react";
import { createWebCall } from "../api/apiClient";
import { useAuth } from "../hooks/useAuth";
import { RetellWebClient } from "retell-client-js-sdk";

export default function Home() {
  const { user } = useAuth();
  const [url, setUrl] = useState<string>("");
  const retellWebClient = new RetellWebClient();

  async function startCall() {
    await retellWebClient.startCall({
      accessToken: 'agent_78233f717b41c36cb4f5266491',
    });
  }

  return (
    <div>
      <h2>Welcome, {user?.first_name}</h2>

      <button onClick={startCall}>Start Web Call</button>

      {url && (
        <iframe
          src={url}
          style={{ width: "600px", height: "700px", border: "1px solid #ccc" }}
        />
      )}
    </div>
  );
}
