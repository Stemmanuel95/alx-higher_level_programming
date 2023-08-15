#!/usr/bin/node

const [argumentOne] = process.argv.slice(2);

if (!argumentOne) {
  console.log('No argument');
} else {
  console.log(argumentOne);
}
