import { Button } from "antd";
import { useState } from "react";
import FiltersBar from "../components/FiltersBar";
import KpiTiles from "../components/KpiTiles";
import AlertsPanel from "../components/AlertsPanel";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const [alertsOpen, setAlertsOpen] = useState(false);
  const navigate = useNavigate();
  return (
    <div style={{ padding: 16 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h2>Sustainability Dashboard</h2>
        <Button type="primary" onClick={() => setAlertsOpen(true)}>Bell</Button>
      </div>
      <FiltersBar />
      <div style={{ marginTop: 16 }}>
        <KpiTiles onOpen={(metric) => {
          if (metric === "overall") navigate("/insights/overall");
          else navigate(`/insights/${metric}`);
        }} />
      </div>
      <AlertsPanel open={alertsOpen} onClose={() => setAlertsOpen(false)} />
    </div>
  );
}
