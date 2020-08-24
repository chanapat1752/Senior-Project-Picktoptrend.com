import React from 'react';
import { NavLink } from "react-router-dom";
import AutoCompleteSearch from '../search/autocompleteSearch'

export default function Navbar () {
    return(
            <nav class="navbar navbar-expand-lg fixed-top navbar-dark " style={{height:'65px',backgroundColor:'#011f4b'}}>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <NavLink to={'/university'}  ><a class="navbar-brand" href="#">
                    <img src="https://pngimg.com/uploads/twitter/twitter_PNG3.png" width="30" height="30" class="d-inline-block align-top" alt=""/>
                    Picktoptrends
                </a></NavLink>
                <AutoCompleteSearch/>
            </nav>
    );
}