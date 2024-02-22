import React from 'react'

import Stepper from './Stepper'
import StepperProvider from '../../context/StepperProvider'

const SearchBox = () => {
  return (
    <StepperProvider>
        <Stepper />
    </StepperProvider>
  )
}

export default SearchBox