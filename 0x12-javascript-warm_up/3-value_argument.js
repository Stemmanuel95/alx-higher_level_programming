#!/usr/bin/node

const [argumentOne, argumentTwo] = process.argv.slice(2);

if (!argumentOne) {
  console.log('No argument');
} else {
  console.log('Argument One:', argumentOne);
  console.log('Argument Two:', argumentTwo);
}
