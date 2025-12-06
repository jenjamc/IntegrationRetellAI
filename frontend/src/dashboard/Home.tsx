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
      accessToken: 'eyJhbGciOiJIUzI1NiJ9.eyJ2aWRlbyI6eyJyb29tSm9pbiI6dHJ1ZSwicm9vbSI6IndlYl9jYWxsXzA3MDFlYWFhMmY1Y2UyYzMwOTM1YWZhNDc5NCJ9LCJpc3MiOiJBUEl3UkNGdVBCYXdtMmgiLCJleHAiOjE3NjUwNDAyODEsIm5iZiI6MCwic3ViIjoiY2xpZW50In0.GIRNuOuuiOoEd0HLuh0wSzkKEk6B8DA1UyrU2BIY4rA',
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
