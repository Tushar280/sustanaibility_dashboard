import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from "./App";
import Dashboard from "./pages/Dashboard";
import OverallInsights from "./pages/OverallInsights";
import MetricInsights from "./pages/MetricInsights";
import "./index.css";

const router = createBrowserRouter([
  { path: "/", element: <App />, children: [
    { index: true, element: <Dashboard /> },
    { path: "/insights/overall", element: <OverallInsights /> },
    { path: "/insights/:metric", element: <MetricInsights /> }
  ] }
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode><RouterProvider router={router} /></React.StrictMode>
);
