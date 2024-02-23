import React, { useState } from 'react';

const Navbar = () => {

    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
      setMenuOpen(!menuOpen);
    };

  return (
    <div className='border-b border-indigo-500/50 text-slate-200 shadow-md bg-white dark:bg-gray-900'>
        <div class="flex flex-row p-2 mx-auto max-w-screen-2xl">
            <div class="w-1/3 sm:w-2/3">
                <div className='flex flex-row p-2'>
                    <div className='w-1/4'>
                        <button className='md:border-r border-indigo-500/50 font-semibold md:text-4xl text-xl px-5'>
                            edunex
                        </button>
                    </div>
                    <button className='w-3/4 text-left hidden md:inline text-xl font-light'>
                        <p className='transform transition-transform hover:scale-110 inline-block'>
                            Tutorias
                        </p>
                    </button>
                </div>
                
            </div>
            <div class="w-2/3 sm:1/3 flex justify-end">
                <button className='md:hidden ml-auto' onClick={toggleMenu}>
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
                </svg>
                </button>
                <button className='inline-block p-2 hidden md:inline transform transition-transform hover:scale-110'> 
                    Registrate como un tutor
                </button>
            </div>
        </div>
        {menuOpen && (
    <div className="md:hidden mt-2 divide-y">
        <button className='block text-left pl-2 py-2 w-full hover:bg-gray-200' onClick={toggleMenu}>Tutorías</button>
        <button className='block text-left pl-2 py-2 w-full hover:bg-gray-200' onClick={toggleMenu}>Registrarse como un tutor</button>
    </div>
)}

    </div>
    

  );
};

export default Navbar;
