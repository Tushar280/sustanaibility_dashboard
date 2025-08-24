import { useParams } from "react-router-dom";
export default function MetricInsights() {
  const { metric } = useParams();
  return <div style={{ padding: 16 }}>
    <h2>{metric} Insights</h2>
    <p>Implement trend, anomalies (red), hotspots bar, heatmap, goals, export.</p>
  </div>;
}
