#!/usr/bin/node
exports.esrever = function (list) {
    const new_list = [];
    for (let i = 0; i < list.length; i++) {
      new_list.unshift(list[i])
      }
    return new_list;
  };