import React from 'react'
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'

import Footer from './footer.js';
import Header from './header.js';

function Current(props){return <p>hoy</p>}
function BOE(props){return <p>boletín del estado</p>}
function BAU(props){return <p>boletin autonómico</p>}
function About(props){return <p>about</p>}

export default function Skeleton({children, date}) {
  return (
    <div className="container grid-xl">
      <div className="columns">
        <Header date={date}/>
        {children}
        <Footer />
      </div>
    </div>
  )
}
