#!/usr/bin/node
// function returns the number of occurences in a list
exports.esrever = function (list) {
  let rev = [];
  for (let i = 0; i < list.length; i++) {
    rev.unshift(list[i]);
  };
  return rev;
};
