import React from 'react';
import { Link } from "react-router-dom";

import styles from './header.module.css'

export default function Header (props) {
  return (
    <div className="hero bg-gray col-12 p-0">
      <div className="hero-body columns">
        <h1 className={styles.title + " col-12 serif"}>Boletines de España</h1>
        <div className="col-lg-12 col-5 serif"> 
          <h2 className={styles.subtitle + " m-0"}>
            Una plataforma no oficial para seguir la
            actividad legislativa a nivel estatal y autonómico
          </h2>
        </div>
        <div className={styles.links + " d-flex col-lg-12 col-7"}> 
          <nav>
            <ul className="d-flex m-0">
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/estatal">
                  <span className="hide-xl">Boletín del Estado</span>
                  <span className="show-xl">Estatal</span>
                </Link>
              </li>
              <li>
                <Link to="/autonomico">
                  <span className="hide-xl">Boletines Autonómicos</span>
                  <span className="show-xl">Autonómico</span>
                </Link>
              </li>
              <li>
                <Link to="/acerca-de">
                  Acerca de
                </Link>
              </li>
              <li>
                <a href="https://boe.es" target="blank">
                  <span className="hide-xl">Portal oficial del BOE</span>
                  <span className="show-xl">Portal oficial</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <div class="divider"></div>
    </div>
  );
}
