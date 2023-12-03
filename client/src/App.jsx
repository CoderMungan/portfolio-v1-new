import { Routes, Route } from 'react-router-dom';

import './App.css'
import NavigationComponents from './Components/NavigationComponents';
import HeaderComponent from './Components/HeaderComponent';
import PageNotFound404 from './Pages/PageNotFound404';
import ArticleSections from './Pages/ArticleSections';
import SingleArticle from './Pages/SingleArticle';



function App() {


  return (
    <>
    <NavigationComponents></NavigationComponents>
      <Routes>
        <Route path='/' element={<HeaderComponent></HeaderComponent>}></Route>
        <Route path='/article' element={<ArticleSections></ArticleSections>}></Route>
        <Route path='/article/:slug' element={<SingleArticle></SingleArticle>}></Route>
        <Route path='*' element={<PageNotFound404></PageNotFound404>}></Route>
      </Routes>
    </>
  )
}

export default App
