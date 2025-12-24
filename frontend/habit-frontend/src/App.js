import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const API = "https://habit-tracker-production-3cfe.up.railway.app";

  const [habits, setHabits] = useState([]);
  const [name, setName] = useState("");

  const loadHabits = async () => {
    const res = await fetch(`${API}/habits`);
    const data = await res.json();
    setHabits(data);
  };

  useEffect(() => {
    loadHabits();
  }, []);

  const addHabit = async () => {
    if (!name.trim()) return;

    await fetch(`${API}/habits`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: Date.now(),
        name: name,
        completed: false,
      }),
    });

    setName("");
    loadHabits();
  };

  const toggleHabit = async (id) => {
    await fetch(`${API}/habits/${id}`, { method: "PUT" });
    loadHabits();
  };

  const deleteHabit = async (id) => {
    await fetch(`${API}/habits/${id}`, { method: "DELETE" });
    loadHabits();
  };

  return (
    <div className="app">
      <h2>🌸 My Habit Garden 🌸</h2>

      <div className="input-row">
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Plant a new habit 🌱"
        />
        <button onClick={addHabit}>Add</button>
      </div>

      <ul>
        {habits.map((h) => (
          <li key={h.id}>
            <span
              className={`habit ${h.completed ? "done" : ""}`}
              onClick={() => toggleHabit(h.id)}
            >
              {h.completed ? "🌼" : "🌷"} {h.name}
            </span>
            <button onClick={() => deleteHabit(h.id)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
