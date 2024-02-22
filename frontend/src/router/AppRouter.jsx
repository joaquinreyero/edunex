import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Home from '../pages/Home';
import Tutorings from '../pages/Tutorings';

const AppRouter = () => {
  return (
    <Routes>
        <Route path='/' element={ <Home /> }/>
        <Route path='/tutorings' element= { <Tutorings />}/>
        <Route path='/*' element= { <Navigate to="/" />}/>
    </Routes>
  )
}

export default AppRouter