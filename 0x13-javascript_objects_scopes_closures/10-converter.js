#!/usr/bin/node

exports.converter = function (base) {
  function my_Converter (n) {
    return n.toString(base);
  }

  return my_Converter;
};
