#!/usr/bin/node
const value = 12;
const numbers = [1, 5, value, 4, 8];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] === value) numbers[i] = 89;
}
console.log(numbers);
