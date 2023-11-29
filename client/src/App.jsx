import { Routes, Route } from 'react-router-dom';
import './App.css'

function App() {


  return (
    <>
      <Routes>
        <Route path='/' element={<><h1 className='text-blue-900 text-3xl'>Hello World!</h1></>}></Route>
        <Route path='/halil' element={<><h5 className='text-blue-700'>Hello Halil World!</h5></>}></Route>
      </Routes>
    </>
  )
}

export default App
