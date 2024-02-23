import React from 'react'

import MainLayout from '../layout/MainLayout'
import SearchBox from '../components/search_by_steps/SearchBox'
import Hero from '../components/hero/Hero'

const Home = () => {
  return (
    <MainLayout>
      <>
        <Hero/>
        <div className='py-5'></div>
        <SearchBox />
      </>
    </MainLayout>
  )
}

export default Home