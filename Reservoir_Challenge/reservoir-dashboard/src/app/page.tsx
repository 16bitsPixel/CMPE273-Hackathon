import Image from "next/image";
import styles from "./page.module.css";
import { Box } from "@mui/material";
import NavBar from "./components/NavBar";
import BarChartComponent from "./components/BarGraph"

export default function Home() {
  return (
    <Box>  
      <NavBar />
      <h1>Reservoir Statistics</h1>
      <BarChartComponent />
    </Box>
  );
}
