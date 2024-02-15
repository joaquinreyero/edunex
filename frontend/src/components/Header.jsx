import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { useTheme } from '@mui/material/styles';

export default function Header() {
  const theme = useTheme();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="sticky" sx={ {backgroundColor:'white'}}>
        <Toolbar
          sx={{
            [theme.breakpoints.up('md')]: {
              paddingX: '100px',
            },
          }}
        >
          <Typography variant="h4" component="div" sx={{ flexGrow: 1 }}>
            <img src="/edunex.svg" alt="Logo" style={{ height: '100px', marginRight: '10px' }} />
          </Typography>
          <Button color="inherit">Soy un tutor</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
