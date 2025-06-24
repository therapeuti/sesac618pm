const open = document.getElementById('open');
const close = document.getElementById('close');

// const modal = document.querySelector('.modal-wrapper');
const modal = document.getElementsByClassName('modal-wrapper')[0];

// console.log(modal)

// 세 가지 모두 같은 것
// open.onclick = function openModal(){}
// open.onclick = function(){}
open.onclick = () => {
    showModal()
}



function showModal() {
    const modalWrapper = document.createElement('div');
    modalWrapper.className = 'modal-wrapper';
 
    modalWrapper.innerHTML =`
    <div class="modal">
            <div class="modal-title">모달 타이틀</div>
            <p>모달 본문 내용 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aut deleniti quasi rem! Id enim repellendus maxime ex tempore. Odio aspernatur obcaecati hic praesentium modi minus libero labore nam ab quos!</p>
            <div class="close-wrapper">
                <button id="close">닫기 버튼</button>
            </div>
    </div>`;

    // body에 위에 만든 모달창 껍데기를 붙이기
    document.body.appendChild(modalWrapper);

    // 닫기 버튼 이벤트추가
    // const close = document.getElementById('close');
    // close.onclick = () => {
    //     modalWrapper.remove();
    // }
    // js는 짧고 간결하게 짜려는 다양한 문법과 기법들이 있음
    document.getElementById('close').onclick = () => {
        modalWrapper.remove();
    }
}