import React from 'react'

const TutoringCard = () => {
  return (
    <div class="flex rounded-xl flex-row border rounded-xl p-2 shadow-xl text-white">
      <img
        class="h-20 w-20 rounded-full object-cover pl-2 pt-1 hidden md:inline"
        src="https://tecdn.b-cdn.net/wp-content/uploads/2020/06/vertical.jpg"
      />
      <div class="flex flex-col justify-start px-8">
        <h6
          class="mb-2 text-xl font-medium">
          Clases Matematicas
        </h6>

        <p className='pb-5 pl-2'> Joaquin Reyero</p>

        <div class="flex flex-row">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0 0 12 9.75c-2.551 0-5.056.2-7.5.582V21M3 21h18M12 6.75h.008v.008H12V6.75Z" />
          </svg>
          <p className='px-2 py-1 '> Universidad Catolica de cordoba</p>
        </div>

        <div class="flex flex-row">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
          <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
        </svg>
          <p className='px-2 pb-4'> 3517262786</p>
        </div>

        <p class="mb-4">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
      </div>
    </div>
  )
}

export default TutoringCard