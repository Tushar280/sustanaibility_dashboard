import { Drawer, List, Tag } from "antd";
import { useEffect, useState } from "react";
import api from "../api/client";

export default function AlertsPanel({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [alerts, setAlerts] = useState<any[]>([]);
  useEffect(() => {
    if (!open) return;
    (async () => {
      const res = await api.get("/alerts/list");
      setAlerts(res.data);
    })();
  }, [open]);

  return (
    <Drawer title="Alerts & Notifications" open={open} onClose={onClose} width={420}>
      <List
        dataSource={alerts}
        renderItem={(a) => (
          <List.Item>
            <List.Item.Meta
              title={<span>{a.message} <Tag color={a.severity === "critical" ? "red" : a.severity === "high" ? "volcano" : "blue"}>{a.severity}</Tag></span>}
              description={new Date(a.created_at).toLocaleString()}
            />
          </List.Item>
        )}
      />
    </Drawer>
  );
}
