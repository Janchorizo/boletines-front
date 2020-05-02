import React from 'react'
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'
import css from 'vendor_css'
import fonts from 'fonts';

import {Skeleton} from 'components/skeleton'

function Current(props){return <p>hoy</p>}
function BOE(props){return <p>boletín del estado</p>}
function BAU(props){return <p>boletin autonómico</p>}
function About(props){return <p>about</p>}

class App extends React.Component {
  render () {
    return (
      <Router>
        <Skeleton date={'hoy'}>
          <Switch>
            <Route path='/estatal'>
              <BOE />
            </Route>
            <Route path='/autonomico'>
              <BAU />
            </Route>
            <Route path='/acerca-de'>
              <About />
            </Route>
            <Route path='/'>
              <Current />
            </Route>
          </Switch>
        </Skeleton>
      </Router>
    )
  }
}

export default App
