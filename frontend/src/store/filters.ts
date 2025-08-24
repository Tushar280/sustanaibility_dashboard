import { create } from "zustand";
import dayjs from "dayjs";

type Filters = {
  start: string; end: string;
  unit_id?: number; department_id?: number; machine_id?: number; shift_id?: number;
}
type Store = { filters: Filters; setFilters: (f: Partial<Filters>) => void; }

const defaultToday = () => {
  const now = dayjs();
  const start = now.startOf("day").toISOString();
  const end = now.endOf("day").toISOString();
  return { start, end };
}

export const useFilters = create<Store>((set, get) => ({
  filters: JSON.parse(localStorage.getItem("filters") || "null") || { ...defaultToday() },
  setFilters: (f) => {
    const updated = { ...get().filters, ...f };
    set({ filters: updated });
    localStorage.setItem("filters", JSON.stringify(updated));
  }
}));
