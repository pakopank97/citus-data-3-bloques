import React from "react";
import ReactDOM from "react-dom/client";

function App() {
  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>✅ Frontend conectado a Citus</h1>
      <p>Si ves este mensaje, el entorno ya funciona perfectamente 🚀</p>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
