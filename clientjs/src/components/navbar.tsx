import React from 'react';
import { Link } from "react-router-dom";
import Search from './searchBook' ;
import logo from '../icon.png'
import '../App.css'

// link is used instead of a href (which causes full page refesh)
// link is better since it will keep my navbar and only refresh the content of the page
const Navbar = () =>{
  return (
    <div className="header">
      <Link to='/home'>
          <div><img src={logo} alt='logo' width="9%"/></div>
      </Link>
      <ul>
        <li>
          <Link to='/home'>Home</Link> 
        </li>
        <li>
          <Link to='/books'>Books</Link>
        </li>
      </ul>
      <Search/>
    </div>

  );
}
export default Navbar;