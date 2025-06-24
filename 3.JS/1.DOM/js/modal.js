const open = document.getElementById('open');
const close = document.getElementById('close');

// const modal = document.querySelector('.modal-wrapper');
const modal = document.getElementsByClassName('modal-wrapper')[0];

// console.log(modal)

// 세 가지 모두 같은 것
// open.onclick = function openModal(){}
// open.onclick = function(){}
open.onclick = () => {
    modal.style.display = 'flex';

}

close.onclick = () => {
    modal.style.display = 'none';
}