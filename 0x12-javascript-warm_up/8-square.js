#!/usr/bin/node

const i = process.argv[2];
const arry = 'X';

if (i && parseInt(i)) {
  for (let j = 0; j < i; j++) {
    console.log(arry.repeat(i));
  }
} else {
  console.log('Missing size');
}
