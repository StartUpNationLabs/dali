import fs from 'fs';
import path from 'path';
import { exec } from 'child_process';

const examplesDir = './examples';

fs.readdir(examplesDir, (err, files) => {
    if (err) {
        console.error("Erreur lors de la lecture du répertoire:", err);
        return;
    }

    const arduinomlFiles = files.filter(file => path.extname(file) === '.arduinoml');

    arduinomlFiles.forEach(file => {
        const filePath = path.join(examplesDir, file);
        const command = `node .\\bin\\cli.js generate "${filePath}"`;

        exec(command, (error, stdout, stderr) => {
            if (error) {
                console.error(`Erreur lors de l'exécution de la commande pour ${file}:`, error);
                return;
            }
            console.log(`Génération réussie pour ${file}`);
            if (stdout) console.log(stdout);
            if (stderr) console.error(stderr);
        });
    });
});