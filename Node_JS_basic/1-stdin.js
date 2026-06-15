const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// console.log yerinə standart çıxışa yazırıq ki, testin gözlədiyi format pozulmasın
process.stdout.write("Welcome to Holberton School, what is your name?\n");

rl.on('line', (input) => {
    // Giriş mətninin sonundakı boşluqları və gizli \r xarakterlərini təmizləmək üçün .trim() istifadə edirik,
    // sonra isə testin tələb etdiyi kimi sonuna \r əlavə edirik.
    process.stdout.write(`Your name is: ${input.trim()}\r`);
});

rl.on('close', () => {
    process.stdout.write("This important software is now closing\n");
});
