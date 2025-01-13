import React from "react";
import { PieChart, Pie, Cell, Tooltip, Legend, BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer } from "recharts";

function ResultsVisualization({ results }) {
  // Calculates sentiment distribution
  const sentimentCounts = {
    positive: results.filter((r) => r.sentiment === "positive").length,
    neutral: results.filter((r) => r.sentiment === "neutral").length,
    negative: results.filter((r) => r.sentiment === "negative").length,
  };

  const data = [
    { name: "Positive", value: sentimentCounts.positive },
    { name: "Neutral", value: sentimentCounts.neutral },
    { name: "Negative", value: sentimentCounts.negative },
  ];

  
  const timeData = results.map((r, index) => ({
    time: new Date(r.timestamp).toLocaleString(), 
    positive: r.sentiment === "positive" ? 1 : 0,
    neutral: r.sentiment === "neutral" ? 1 : 0,
    negative: r.sentiment === "negative" ? 1 : 0,
  }));

  const COLORS = ["#00C49F", "#FFBB28", "#FF8042"];

  return (
    <div className="results-container">
      <h2>Sentiment Analysis Results</h2>

      <div className="pie-chart-container">
        <h3>Sentiment Distribution</h3>
        <PieChart width={350} height={350}>
          <Pie
            data={data}
            cx={175}
            cy={175}
            outerRadius={150}
            fill="#8884d8"
            dataKey="value"
            label
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend verticalAlign="top" height={36} />
        </PieChart>
      </div>

      <div className="bar-chart-container">
        <h3>Sentiment Change Over Time</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={timeData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="positive" fill="#00C49F" name="Positive Sentiment" />
            <Bar dataKey="neutral" fill="#FFBB28" name="Neutral Sentiment" />
            <Bar dataKey="negative" fill="#FF8042" name="Negative Sentiment" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default ResultsVisualization;
