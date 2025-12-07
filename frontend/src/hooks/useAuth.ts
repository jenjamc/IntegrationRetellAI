import { useEffect, useState } from "react";
import { getUserInfo } from "../api/api";
import type { User } from "../api/types";

export function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const token = localStorage.getItem("token");
      if (!token) {
        setLoading(false);
        return;
      }

      const data = await getUserInfo();
      if (data?.id) setUser(data);
      setLoading(false);
    }

    load();
  }, []);

  return { user, loading, setUser };
}
