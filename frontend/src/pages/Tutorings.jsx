import React from 'react';
import MainLayout from '../layout/MainLayout';
import TutoringCard from '../components/tutorings/TutoringCard';

const Tutorings = () => {

  return (
    <MainLayout>
      <div className='py-5'></div>
      <div className='px-3'>
        <TutoringCard />
      </div>
      <div className='py-5'></div>
    </MainLayout>
  )
}

export default Tutorings