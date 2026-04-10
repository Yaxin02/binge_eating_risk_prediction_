import { useState } from "react";
import { useNavigate } from "react-router-dom";

function AdminLoginPage() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = () => {
    if (username === "yassin" && password === "123") {
      localStorage.setItem("admin_auth", "true");
      navigate("/dashboard");
    } else {
      setError("Invalid username or password");
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background:
          "linear-gradient(135deg, #eef2ff 0%, #fdf2f8 50%, #ecfeff 100%)",
        padding: "20px",
        fontFamily:
          "Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "420px",
          background: "rgba(255,255,255,0.95)",
          borderRadius: "24px",
          padding: "30px",
          boxShadow: "0 20px 60px rgba(15, 23, 42, 0.12)",
          textAlign: "center",
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: "10px",
            padding: "8px 14px",
            borderRadius: "999px",
            background: "#ede9fe",
            color: "#5b21b6",
            fontWeight: 700,
            fontSize: "14px",
            marginBottom: "16px",
          }}
        >
          🛡️ Admin Access
        </div>

        <h1 style={{ marginTop: 0, color: "#0f172a" }}>Admin Login</h1>
        <p style={{ color: "#64748b", marginBottom: "24px" }}>
          Enter your admin credentials to access the dashboard.
        </p>

        {error && (
          <div
            style={{
              marginBottom: "14px",
              padding: "12px",
              borderRadius: "12px",
              background: "#fef2f2",
              color: "#b91c1c",
              textAlign: "center",
            }}
          >
            {error}
          </div>
        )}

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={inputStyle}
        />

        <button onClick={handleLogin} style={buttonStyle}>
          Login
        </button>

        <button onClick={() => navigate("/")} style={backButtonStyle}>
          Back to Home
        </button>
      </div>
    </div>
  );
}

const inputStyle: React.CSSProperties = {
  width: "100%",
  padding: "14px",
  marginBottom: "14px",
  borderRadius: "12px",
  border: "1px solid #d1d5db",
  fontSize: "15px",
  boxSizing: "border-box",
};

const buttonStyle: React.CSSProperties = {
  width: "100%",
  padding: "14px",
  border: "none",
  borderRadius: "14px",
  color: "white",
  fontSize: "16px",
  fontWeight: "bold",
  background: "linear-gradient(135deg, #2563eb 0%, #7c3aed 100%)",
  cursor: "pointer",
};

const backButtonStyle: React.CSSProperties = {
  width: "100%",
  padding: "14px",
  marginTop: "12px",
  borderRadius: "14px",
  border: "1px solid #d1d5db",
  color: "#0f172a",
  fontSize: "16px",
  fontWeight: "bold",
  background: "white",
  cursor: "pointer",
};

export default AdminLoginPage;