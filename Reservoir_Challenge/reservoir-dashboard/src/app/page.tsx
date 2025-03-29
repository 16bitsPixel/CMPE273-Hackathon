import Image from "next/image";
import styles from "./page.module.css";
import { Box, Typography } from "@mui/material";
import NavBar from "./components/NavBar";
import BarChartComponent from "./components/BarGraph"

export default function Home() {
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
        <Typography variant="h3" sx={{marginTop: "5%"}}>Reservoir Statistics</Typography>
        <BarChartComponent />
      </Box>
    </Box>
  );
}
