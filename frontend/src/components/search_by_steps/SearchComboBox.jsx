import React, { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Box } from '@mui/material';

export default function SearchComboBox({ activeStep }) {
  let options = [];

  if (activeStep === 0) {
    options = [{ name: 'University A', id: 1 }, { name: 'University B', id: 2 }];
  } else if (activeStep === 1) {
    options = [{ name: 'Degree A', id: 1 }, { name: 'Degree B', id: 2 }];
  } else if (activeStep === 2) {
    options = [{ name: 'Subject A', id: 1 }, { name: 'Subject B', id: 2 }];
  }

  const [value, setValue] = useState(null);

  useEffect(() => {
    setValue(null);
  }, [activeStep]);

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <Box sx={{ marginBottom: '10px' }}>
        <Autocomplete
          disablePortal
          id="combo-box"
          options={options}
          getOptionLabel={(option) => option.name}
          value={value}
          onChange={(event, newValue) => {
            setValue(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
          sx={{ width: 300 , marginBottom:'5px'}}
        />
      </Box>
    </Box>
  );
}
