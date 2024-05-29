
function renderiza_radar(url) {
    fetch(url, {
        method: 'GET',
    })
    .then(function(result) {
        return result.json();
    })
    .then(function(data) {
        const ctx = document.getElementById('grafico-radar').getContext('2d');
        const MyChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: data.funcionario.nome,
                    data: data.pontuacao,
                    fill: true,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgb(54, 162, 235)',
                    pointBackgroundColor: 'rgb(54, 162, 235)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(54, 162, 235)'
                }, {
                    label: 'Vaga',
                    data: [1, 2, 3, 4, 5, 6],
                    fill: true,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgb(255, 99, 132)',
                    pointBackgroundColor: 'rgb(255, 99, 132)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(255, 99, 132)'
                }]
            },
            options: {
                elements: {
                    line: {
                        borderWidth: 2,

                    }
                }
            }
        });
    })
    .catch(function(error) {
        console.error('Erro ao buscar dados:', error);
    });
}
