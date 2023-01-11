import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';
import {BrowserRouter } from 'react-router-dom';
// import reportWebVitals from './reportWebVitals';



//a terminating link that sends a GraphQL operation to a remote endpoint over HTTP
// cors origin policy is caused from trhe brower that blocks requests from external url if they are diff origin. 
// const httpLink = new HttpLink({
//   uri: 'http://localhost:3000/graphql',
//   fetchOptions: {
//     mode: 'no-cors',
//   },
// });

// if you call the same query again, it will access from the cache so it is faster 
export const client = new ApolloClient({
  cache: new InMemoryCache(),
  uri: 'http://localhost:3000/graphql',
});

const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(
  // apolloprivider wraps react app and allows you to access queries from anywhere in app
// force refresh loads all the components when changing paths
// brower router allows the browser URL to be changed, and keeps the UI in sync with the URL
<BrowserRouter forceRefresh={true}> 
  <ApolloProvider client={client}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </ApolloProvider>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
