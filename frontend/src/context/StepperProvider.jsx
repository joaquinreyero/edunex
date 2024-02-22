import React, { useState } from 'react';
import { StepperContext } from './StepperContext';

const StepperProvider = ({ children }) => {
    const [stepper, setStepper] = useState({
        university: null,
        degree: null,
        subject: null
    });

    const setUniversity = (university) => {
        setStepper((prevStepper) => ({
            ...prevStepper,
            university
        }));
    };

    const setDegree = (degree) => {
        setStepper((prevStepper) => ({
            ...prevStepper,
            degree
        }));
    };

    const setSubject = (subject) => {
        setStepper((prevStepper) => ({
            ...prevStepper,
            subject
        }));
    };

    return (
        <StepperContext.Provider
            value={{
                stepper,
                setUniversity,
                setDegree,
                setSubject
            }}
        >
            {children}
        </StepperContext.Provider>
    );
};

export default StepperProvider;
