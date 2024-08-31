function ajouterAuPanier(courseId) {
    const url = `/panier/ajouter/${courseId}/`;
    console.log(url); // Vérifiez si l'URL est correcte
    fetch(url, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (!response.ok) {
            // Affiche le message d'erreur dans la console
            return response.text().then(text => { throw new Error(text) });
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'exists') {
            Swal.fire({
                text: "Ce cours est déjà dans votre panier.",
                icon: 'warning',
                confirmButtonText: 'OK'
            });
        } else if (data.status === 'added') {
            Swal.fire({
                text: "Le cours a été ajouté à votre panier.",
                icon: 'success',
                confirmButtonText: 'OK'
            });
        }
    })
    .catch(error => console.error('Erreur:', error)); // Affiche les erreurs dans la console
}
