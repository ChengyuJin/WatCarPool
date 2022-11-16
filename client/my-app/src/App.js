import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import { AddModifyTrip } from './pages/AddModifyTrip';
import { Home } from './pages/Home'
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { Welcome } from './pages/Welcome';
function App() {
    return (
        <BrowserRouter>
        
        <Routes>
          <Route path="/" element={<Welcome />} />
          <Route path="/mainpage" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/addmodify" element={<AddModifyTrip />} />
          
        </Routes>
        </BrowserRouter>
    );
  }
  
export default App;
