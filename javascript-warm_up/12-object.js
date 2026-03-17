#!/usr/bin/node
const numbers = [1, 5, 12, 4, 8]; // 12 reste dans le tableau initial

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] === 12) {
    numbers[i] = 89;
  }
}

console.log(numbers);
