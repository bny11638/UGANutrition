import * as React from "react";
import Welcome from "./Welcome";
import Login from "./Login";
import Dashboard from "./Dashboard";
import { Routes, Route} from "react-router-dom";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />}/>
      </Routes>
    </div>
  );
}

export default App;