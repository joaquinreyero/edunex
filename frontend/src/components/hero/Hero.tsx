import React from 'react'

const Hero = () => {
    return (
      <div className="flex flex-col md:flex-row">
        <div className="order-2 md:order-2 w-full md:w-1/2">
          <img src="src/public/hero.svg" alt='Tutor and student' />
        </div>
        <div className="order-1 md:order-1 w-full md:w-1/2 text-lg md:text-4xl text-slate-200">
          <div className='text-center font-light md:py-32 py-10 px-10'>
          <p>
            Encuentra <a></a>
            <a className="underline decoration-indigo-500">tutores expertos </a>que se ajusten a tus necesidades académicas
            <a className="underline decoration-sky-500"></a>
            y lleven tu aprendizaje al 
            <a className="underline decoration-pink-500"> siguiente nivel</a>. 
            Prepárate para el éxito académico hoy mismo.
        </p>

          </div>
        </div>
      </div>
    )
  }
  
  export default Hero
  
  
  