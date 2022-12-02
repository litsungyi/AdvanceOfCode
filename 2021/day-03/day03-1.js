const fs = require('fs');

let counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
let gamma = 0;
let epsilon = 0;
let total = 0;
const datas = fs.readFileSync('input.txt', 'utf-8').split(/\n/).map(line => {
    ++total;
    for (let index = 0; index < line.length; ++index) {
        counts[index] += parseInt(line[index]);
      }
});

let half = total / 2;
counts.map( count => {
    gamma <<= 1;
    epsilon <<= 1;
    if (count > half) {
        ++gamma;
    } else {
        ++epsilon;
    }
});
console.log(gamma * epsilon);
