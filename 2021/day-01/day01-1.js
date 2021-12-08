const fs = require('fs');

const lines = fs.readFileSync('input.txt', 'utf-8').split(/\n/).map(line => parseInt(line));
console.log(lines.filter( (line, index) => index != 0 && line > lines[index -1] ).length);
