import React from 'react'

import MainLayout from '../layout/MainLayout'
import SearchUniversity from '../components/SearchUniversity'

const Home = () => {
  return (
    <MainLayout>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <SearchUniversity />
      </div>
    </MainLayout>
  )
}

export default Home