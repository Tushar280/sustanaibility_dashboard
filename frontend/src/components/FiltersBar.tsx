import { DatePicker, Select, Button } from "antd";
import dayjs from "dayjs";
import { useFilters } from "../store/filters";

export default function FiltersBar() {
  const { filters, setFilters } = useFilters();
  return (
    <div style={{ display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" }}>
      <DatePicker.RangePicker
        value={[dayjs(filters.start), dayjs(filters.end)]}
        onChange={(vals) => { if (!vals) return; setFilters({ start: vals[0]!.toISOString(), end: vals[1]!.toISOString() }); }}
        showTime
      />
      <Select placeholder="Unit" style={{ width: 160 }} allowClear onChange={(v) => setFilters({ unit_id: v || undefined })} />
      <Select placeholder="Department" style={{ width: 160 }} allowClear onChange={(v) => setFilters({ department_id: v || undefined })} />
      <Select placeholder="Machine" style={{ width: 160 }} allowClear onChange={(v) => setFilters({ machine_id: v || undefined })} />
      <Select placeholder="Shift" style={{ width: 160 }} allowClear onChange={(v) => setFilters({ shift_id: v || undefined })} />
      <Button onClick={() => window.location.reload()}>Refresh</Button>
    </div>
  );
}
