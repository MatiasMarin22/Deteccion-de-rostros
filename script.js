function cargarFotosDesdeLocalStorage() {
    let fotosDiv = document.getElementById('fotos');
    fotosDiv.innerHTML = '';

    for (let i = 0; i < localStorage.length; i++) {
        let key = localStorage.key(i);
        if (key.startsWith('foto_')) {
            let imgSrc = localStorage.getItem(key);
            let col = document.createElement('div');
            col.className = 'col-md-3 mb-3';
            let img = document.createElement('img');
            img.src = imgSrc;
            img.alt = key;
            img.className = 'img-fluid img-thumbnail';
            col.appendChild(img);
            fotosDiv.appendChild(col);
        }
    }
}

document.getElementById('cargarFotos').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/fotos')
        .then(response => response.json())
        .then(fotos => {
            let fotosDiv = document.getElementById('fotos');
            fotosDiv.innerHTML = '';
            fotos.forEach(foto => {
                let imgSrc = `http://127.0.0.1:5000/fotos/${foto}`;
                let col = document.createElement('div');
                col.className = 'col-md-3 mb-3';
                let img = document.createElement('img');
                img.src = imgSrc;
                img.alt = foto;
                img.className = 'img-fluid img-thumbnail';
                col.appendChild(img);
                fotosDiv.appendChild(col);

                localStorage.setItem(`foto_${foto}`, imgSrc);
            });
        })
        .catch(error => console.error('Error al cargar fotos:', error));
});

window.onload = function() {
    cargarFotosDesdeLocalStorage();
};
