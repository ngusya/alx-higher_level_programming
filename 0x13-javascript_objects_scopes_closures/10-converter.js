#!/usr/bin/node

exports.converter = function (base) {
  return (b) => {
    return parseInt(b).toString(base);
  };
};
