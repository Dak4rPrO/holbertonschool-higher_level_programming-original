#!/usr/bin/node

function starwars () {
    const episode = process.argv[2];
    const axios = require('axios');
    const url = `https://swapi-api.hbtn.io/api/films/${episode}`

    axios.get(url)
      .then((response) => {
        console.log(`${response.data.title}`);
      })
  
      .catch((error) => {
        console.log(`${error}`);
      });
  }
  starwars();
