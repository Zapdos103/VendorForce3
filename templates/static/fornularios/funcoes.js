/* Funções dos formulários */

console.log('teste')

const modalBtn = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

url = window.location.href

modalBtn.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const nome = modalBtn.getAttribute('data-form')
    const qtd_questoes = modalBtn.getAttribute('data-questoes')
    const tempo = modalBtn.getAttribute('data-tempo')
    const qtd_acertos = modalBtn.getAttribute('data-acertos')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Tem certeza que deseja começar '<b>${nome}</b>'?</div>
        <div class="text-muted">
            <ul>
                <li>Número de questões: ${qtd_questoes} </li>
                <li>Tempo: ${tempo} minuto(s)</li>

            </ul>
        </div>
    `
    startBtn.addEventListener('click', startBtn=>{
        window.location.href = url + pk
    })
    }))
