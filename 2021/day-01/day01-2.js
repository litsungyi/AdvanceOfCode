const fs = require('fs');

const lines = fs.readFileSync('input.txt', 'utf-8').split(/\n/).map(line => parseInt(line));
const MAX_INDEX = lines.length - 3;
let count = lines.filter( (line, index) => index <= MAX_INDEX && lines[index + 3] > line ).length;

console.log(count);
