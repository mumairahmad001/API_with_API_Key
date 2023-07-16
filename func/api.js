const functions = require('firebase-functions');
const app = require('./datashare_api.py').app;
exports.func = functions.https.onRequest(app);
