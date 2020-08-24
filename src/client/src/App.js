import React, { Fragment } from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import { createBrowserHistory as history } from 'history';
import Header from './components/header/NavBar';
import Home from './home';
import SearchResult from './components/search/result'



function App() {
  return (
    <Fragment>
      <Router history={history}>
        <div class="container-fliud bg-light">
          <Header />
          <Switch>
            <Route exact path="/university" component={Home} />
            <Route exact path="/university/tweetCount" component={Home} />
            {/* <Route exact path="/university/retweetPerMinute" component={Home} /> */}
            <Route exact path="/university/retweetCount" component={Home} />
            <Route exact path="/university/search" component={Home} />
            {/* <Route exact path="/university/count7Days" component={Home} /> */}
            <Route path="/university/:id" component={SearchResult} />
          </Switch>
        </div>
      </Router>
    </Fragment>
  );
}

export default App;
