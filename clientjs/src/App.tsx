import React from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import {Navbar, Intro, SearchResult, Search, AllBooks} from './components/index';
import './App.css';

const App = () => {
  // when switch is rendered, it searches through children route. Once a url match is found, 
  // it will use that route to load its contents 
  return (
    <div>
      <Navbar/>
      <Router>
        <Switch>
          <Route path="/home">
            <Search />
            <Intro />
          </Route>
          <Route path={"/page"}>
            <SearchResult/>
          </Route>
          <Route path={"/books"}>
            <AllBooks/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}
export default App;
// command to start gql linked server
// npx postgraphile -c 'postgresql://postgres:San611909@localhost/flaskPractice' --watch --enhance-graphiql --dynamic-json