import { createProxyMiddleware } from 'http-proxy-middleware';
const express = require('express');
const app = express();

app.use('/graphql', createProxyMiddleware({ target: 'http://localhost:5000/graphql', changeOrigin: true }));
app.listen(3000);

//  software that enables one or more kinds of communication or connectivity between two or more applications