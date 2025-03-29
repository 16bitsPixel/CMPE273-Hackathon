"use client";

import { Box, Card, Typography } from "@mui/material";
import NavBar from "./components/NavBar";
import PredictionCard from "./components/PredictionCard";
import { useState, useEffect } from "react";

export default function Home() {
  const [audioData, setAudioData] = useState(null);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      setAudioData(newData);
    };

    return () => ws.close();
  }, []);

  return (
    <Box sx = {{
      height: '100vh',
      display: 'flex',
      flexDirection: 'column',
    }}>
      <NavBar />

      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',      // Center vertically
          flexDirection: 'column',   // Stack the children vertically
          flexGrow: 1,               // Allow this box to take remaining space
        }}
      >
        <Typography variant="h3" sx={{marginTop: "5%"}}>Live Audio Classification Data</Typography>
        {audioData ? (
          <PredictionCard predictedclass={audioData.predictedclass} confidence={audioData.confidence} />
        ) : (
          <Typography variant = "h4">Waiting for data...</Typography>
        )}
      </Box>
    </Box>
  );
}
