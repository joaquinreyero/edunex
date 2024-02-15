import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Button from '@mui/material/Button';
import { Box } from '@mui/material';

export default function ComboBox() {
    const [selectedUniversity, setSelectedUniversity] = React.useState(null);
    const [selectedDegree, setSelectedDegree] = React.useState(null);
    const [filteredDegrees, setFilteredDegrees] = React.useState([]);
    const [filteredSubjects, setFilteredSubjects] = React.useState([]);
  
    const universities = [{ name: 'University A', id: 1 }, { name: 'University B', id: 2 }];
    const degrees = [{ name: 'Degree 1', universityId: 1 }, { name: 'Degree 2', universityId: 1 }, { name: 'Degree 3', universityId: 2 }];
    const subjects = [{ name: 'Subject 1', degreeId: 1 }, { name: 'Subject 2', degreeId: 1 }, { name: 'Subject 3', degreeId: 2 }];
  
    const handleUniversityChange = (event, newValue) => {
      setSelectedUniversity(newValue);
      setFilteredDegrees(newValue ? degrees.filter(degree => degree.universityId === newValue.id) : []);
      setSelectedDegree(null); 
      setFilteredSubjects([]); 
    };
  
    const handleDegreeChange = (event, newValue) => {
      setSelectedDegree(newValue);
      setFilteredSubjects(newValue ? subjects.filter(subject => subject.degreeId === newValue.universityId) : []);
    };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Box sx={{ marginBottom: '10px' }}>
            <Autocomplete
            disablePortal
            id="combo-box-university"
            options={universities}
            getOptionLabel={(option) => option.name}
            value={selectedUniversity}
            onChange={handleUniversityChange}
            renderInput={(params) => <TextField {...params} label="Universidad" />}
            sx={{ width: 300 , marginBottom:'5px'}}
            />
        </Box>
        <Box sx={{ marginBottom: '10px' }}>
            <Autocomplete
            disablePortal
            id="combo-box-degree"
            options={filteredDegrees}
            getOptionLabel={(option) => option.name}
            value={selectedDegree}
            onChange={handleDegreeChange}
            renderInput={(params) => <TextField {...params} label="Carrera" />}
            sx={{ width: 300 , marginBottom:'5px'}}
            />
        </Box>
        <Box sx={{ marginBottom: '10px' }}>
            <Autocomplete
            disablePortal
            id="combo-box-subjet"
            options={filteredSubjects}
            getOptionLabel={(option) => option.name}
            renderInput={(params) => <TextField {...params} label="Materia" />}
            sx={{ width: 300 , marginBottom:'5px'}}
            />
        </Box>
        <Button variant="contained">Buscar</Button>
    </Box>
    
  );
}

