#!/usr/bin/node

const args = process.argv;
const arry = 'C is fun';

if (args.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log(arry);
  }
}
