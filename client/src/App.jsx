import { Routes, Route } from 'react-router-dom';

import './App.css'
import NavigationComponents from './Components/NavigationComponents';
import HeaderComponent from './Components/HeaderComponent';
import PageNotFound404 from './Pages/PageNotFound404';
import BlogSections from './Pages/BlogSections';
import SingleBlog from './Pages/SingleBlog';



function App() {


  return (
    <>
    <NavigationComponents></NavigationComponents>
      <Routes>
        <Route path='/' element={<HeaderComponent></HeaderComponent>}></Route>
        <Route path='/blog' element={<BlogSections></BlogSections>}></Route>
        <Route path='/blog/:slug' element={<SingleBlog></SingleBlog>}></Route>
        <Route path='*' element={<PageNotFound404></PageNotFound404>}></Route>
      </Routes>
    </>
  )
}

export default App
