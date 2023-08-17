#!/usr/bin/node

let counterVar = 0;

exports.logMe = function count (item) {
  console.log(`${counterVar}: ${item}`);
  counterVar += 1;
};
