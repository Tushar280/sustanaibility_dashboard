import { Card, Statistic } from "antd";
import { useEffect, useState } from "react";
import api from "../api/client";
import { useFilters } from "../store/filters";
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

type SeriesPoint = { ts: string; value: number; }

export default function KpiTiles({ onOpen }: { onOpen: (metric: string) => void }) {
  const { filters } = useFilters();
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    (async () => {
      const res = await api.get("/kpis/overview", { params: { ...filters } });
      setData(res.data.kpis);
    })();
  }, [filters]);

  if (!data) return null;

  const metrics = [
    { key: "energy_kwh", title: "Energy" },
    { key: "water_m3", title: "Water" },
    { key: "waste_kg", title: "Waste" },
    { key: "co2e_tons", title: "Emissions" },
  ];

  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 12 }}>
      <Card hoverable onClick={() => onOpen("overall")} style={{ gridColumn: "span 1" }}>
        <Statistic title="Overall Performance" value="Index" />
        <div style={{ height: 80 }}>
          <ResponsiveContainer>
            <AreaChart data={metrics.map(m => ({ name: m.title, v: data[m.key]?.value || 0 }))}>
              <XAxis dataKey="name" hide /><YAxis hide /><Tooltip />
              <Area dataKey="v" stroke="#8884d8" fill="#8884d8" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </Card>
      {metrics.map((m) => (
        <Card key={m.key} hoverable onClick={() => onOpen(m.key)}>
          <Statistic title={m.title} value={Math.round((data[m.key]?.value || 0) * 100) / 100} />
          <div style={{ height: 80 }}>
            <ResponsiveContainer>
              <AreaChart data={(data[m.key]?.series || []) as SeriesPoint[]}>
                <XAxis dataKey="ts" hide /><YAxis hide /><Tooltip />
                <Area dataKey="value" stroke="#82ca9d" fill="#82ca9d" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </Card>
      ))}
    </div>
  );
}
