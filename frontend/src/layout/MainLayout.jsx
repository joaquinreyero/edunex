import React from 'react';
import Navbar from '../components/navbar/Navbar';
import Footer from '../components/footer/Footer'
export const MainLayout = ({ children }) => {
  return (
    <div class='bg-gradient-to-r from-blue-950 to-blue-900 backdrop-blur-md  font-sans'>
      <Navbar />
      <div className='mx-auto max-w-screen-2xl'>
        {children}
      </div>
      <Footer />
    </div>
  );
};

export default MainLayout;
