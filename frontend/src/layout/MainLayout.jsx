import React from 'react';
import Header from '../components/Header';
import { Box } from '@mui/material';
import { Padding } from '@mui/icons-material';

export const MainLayout = ({ children }) => {
  return (
    <div>
      <Header />
      <Box sx={{
        padding: '5px 1rem 1rem 1rem'
      }}/>
      {children}
    </div>
  );
};

export default MainLayout;
