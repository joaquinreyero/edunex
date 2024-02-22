import React, { useState, useEffect, useContext } from 'react';
import useFetch from '../../hooks/useFetch';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Box } from '@mui/material';
import { StepperContext } from '../../context';

const SearchComboBox = ({ activeStep }) => {
    const { stepper, setUniversity, setDegree, setSubject } = useContext(StepperContext);
    const [endpoint, setEndpoint] = useState('');
    const [data, , errors] = useFetch(endpoint); 
    const [value, setValue] = useState(null);

    useEffect(() => {
        setValue(null);
    }, [activeStep]);

    useEffect(() => {
        switch (activeStep) {
            case 0:
                setEndpoint('https://backend-rn4m6jjw6a-ue.a.run.app/api/universities');
                break;
            case 1:
                stepper.university && setEndpoint(`https://backend-rn4m6jjw6a-ue.a.run.app/api/degrees?university_id=${stepper.university.id}`);
                break;
            case 2:
                stepper.degree && setEndpoint(`https://backend-rn4m6jjw6a-ue.a.run.app/api/subjects?subject_id=${stepper.degree.id}`);
                break;
            default:
                break;
        }
    }, [activeStep, stepper]);

    const options = data ? data.map(item => ({ name: item.name, id: item.id })) : []; 

    const renderAutocomplete = () => (
        <Autocomplete
            disablePortal
            id="combo-box"
            options={options}
            getOptionLabel={(option) => option.name}
            value={value}
            onChange={(event, newValue) => {
                setValue(newValue);
                switch (activeStep) {
                    case 0:
                        setUniversity(newValue);
                        break;
                    case 1:
                        setDegree(newValue);
                        break;
                    case 2:
                        setSubject(newValue);
                        break;
                    default:
                        break;
                }
            }}
            renderInput={(params) => <TextField {...params} />}
            sx={{ width: 300, marginBottom: '5px' }}
            loadingText="Cargando..." 
        />
    );

    const renderContent = () => {
        if (errors) {
            return <p>Error: {errors}</p>;
        } else {
            return (
                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <Box sx={{ marginBottom: '10px' }}>
                        {renderAutocomplete()}
                    </Box>
                </Box>
            );
        }
    };

    console.log("Stepper context:", stepper);

    return (
        <>
            {renderContent()}
        </>
    );
};

export default SearchComboBox;
