"use client"

import { styled } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import InputBase from '@mui/material/InputBase';

export default function Header() {
  return (
    <Box>
      <AppBar position="sticky" sx={{ backgroundColor: '046B99', color: 'white' }} >
        <Toolbar sx={{ justifyContent: 'space-between' }}>
          {/* Left side logo */}
          <Typography
            variant="h6"
            noWrap
            component="div"
            sx={{ display: { xs: 'none', md: 'block' } }}
          >
            Car Sounds Dashboard
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}