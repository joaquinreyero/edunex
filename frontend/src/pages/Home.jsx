import React from 'react'

import MainLayout from '../layout/MainLayout'
import SearchBox from '../components/search_by_steps/SearchBox'

const Home = () => {
  return (
    <MainLayout>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <SearchBox />
      </div>
    </MainLayout>
  )
}

export default Home