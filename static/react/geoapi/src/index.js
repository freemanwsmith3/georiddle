import React from 'react';
import { createRoot } from "react-dom/client";
import './index.css';
import App from './App';
//import reportWebVitals from './reportWebVitals';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
import Header from './components/Header'
import Footer from './components/Footer';

const root = createRoot(document.getElementById("root"));

root.render(
  <Router>
    <React.StrictMode>
      <Header />
      <Routes>
        <Route exact path="/"  element={<App />}></Route>
      </Routes>
      <Footer />
    </React.StrictMode>
  </Router>
)



