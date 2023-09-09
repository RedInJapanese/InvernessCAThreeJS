# InvernessCAThreeJS

This project uses threejs and the google maps api to take coordinates from a csv file and plot them.

## Installation

To install the repository, run the following command.
```bash
git clone https://github.com/RedInJapanese/InvernessCAThreeJS.git
npm i
npm start -- --port=8080
```

Note: The API key does not belong to me. This key is from the google maps api docs page and is restricted to `localhost:8080`. 
**DO NOT TRY HOSTING THIS APPLICATION WITH THE CURRENT KEY**

## Update the Google Maps API key

The application is currently using the
<walkthrough-editor-open-file filePath=".env">.env</walkthrough-editor-open-file>
file to embed the API key in the HTML document. This is a temporary key and is
not valid for production usage.

The key can be replaced by following these instructions to
[get an api key](https://developers.google.com/maps/documentation/javascript/get-api-key).

After changing the key, the Webpack server must be restarted with the following
command:

```bash
npm start -- --port=8080
```
