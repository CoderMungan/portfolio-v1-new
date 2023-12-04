import { Routes, Route } from 'react-router-dom';

import './App.css'
import NavigationComponents from './Components/NavigationComponents';
import HeaderComponent from './Components/HeaderComponent';
import PageNotFound404 from './Pages/PageNotFound404';
import ArticleSections from './Pages/ArticleSections';
import SingleArticle from './Pages/SingleArticle';
import ContactForm from './Pages/ContactForm';
import ContactSucces from './Pages/ContactSucces';



function App() {


  return (
    <>
    <NavigationComponents></NavigationComponents>
      <Routes>
        <Route path='/' element={<HeaderComponent></HeaderComponent>}></Route>
        <Route path='/article' element={<ArticleSections></ArticleSections>}></Route>
        <Route path='/article/:slug' element={<SingleArticle></SingleArticle>}></Route>
        <Route path='/contact-me' element={<ContactForm></ContactForm>}></Route>
        <Route path='/form-succes' element={<ContactSucces></ContactSucces>}></Route>
        <Route path='*' element={<PageNotFound404></PageNotFound404>}></Route>
      </Routes>
    </>
  )
}

export default App
