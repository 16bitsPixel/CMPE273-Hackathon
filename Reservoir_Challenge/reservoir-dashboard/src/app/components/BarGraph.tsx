'use client';

import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Paper, Typography } from '@mui/material';

interface ReservoirData {
  reservoir_code: string;
  min_value: number;
  max_value: number;
  avg_value: number;
  latest_depth: number;
}

const BarChartComponent: React.FC = () => {
  const [reservoirData, setReservoirData] = useState<ReservoirData[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      setReservoirData(newData);
    };

    return () => ws.close();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  const formattedData = reservoirData.map((item) => ({
    name: item.reservoir_code,
    min: item.min_value,
    max: item.max_value,
    avg: item.avg_value,
    latest: item.latest_depth,
  }));

  return (
    <Paper elevation={3} style={{ padding: '20px', textAlign: 'center' }}>
      <Typography variant="h5" gutterBottom>
        Reservoir Depth Statistics
      </Typography>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={formattedData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="min" fill="#8884d8" />
          <Bar dataKey="max" fill="#82ca9d" />
          <Bar dataKey="avg" fill="#ffc658" />
          <Bar dataKey="latest" fill="#ff7300" />
        </BarChart>
      </ResponsiveContainer>
    </Paper>
  );
};

export default BarChartComponent;
