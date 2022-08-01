#!/usr/bin/node

const args = process.argv;

if (args.length === 3) {
  console.log('My number: ' + parseInt(args[2]));
} else if (args.length < 3) {
  console.log('Not a number ');
}
