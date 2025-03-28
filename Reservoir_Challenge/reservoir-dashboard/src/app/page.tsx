import Image from "next/image";
import styles from "./page.module.css";
import { Box } from "@mui/material";
import NavBar from "./components/NavBar";

export default function Home() {
  return (
    <Box>
      <NavBar />
    </Box>
  );
}
