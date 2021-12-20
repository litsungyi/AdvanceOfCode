const fs = require('fs');

let horizontal_position = 0;
let depth = 0;
const datas = fs.readFileSync('input.txt', 'utf-8').split(/\n/).map(line => {
    let results = line.split(' ');
    return { direction: results[0], value: parseInt(results[1]) };
});
datas.map( data => {
    switch(data['direction']) {
        case 'forward':
            horizontal_position += data['value'];
            break;

        case 'up':
            depth -= data['value'];
            break;

        case 'down':
            depth += data['value'];
            break;
    }
});
console.log(horizontal_position * depth);
