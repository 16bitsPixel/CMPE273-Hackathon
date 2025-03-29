"use client";

import { Box, Typography } from "@mui/material";
import NavBar from "./components/NavBar";
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
    <Box>
      <NavBar />
      <Typography>Live Audio Classification Data</Typography>
      {audioData ? (
        <div>
          <p>Predicted Class: {audioData.predictedclass}</p>
          <p>Confidence: {audioData.confidence}</p>
        </div>
      ) : (
        <p>Waiting for data...</p>
      )}
    </Box>
  );
}
