document.addEventListener("DOMContentLoaded", function () {
    // 여기는 브라우저가 DOM을 불러왔을 때 여기가 호출됨.
    let fruitSelector = document.getElementById("fruitSelector");

    fruitSelector.addEventListener("change", function() {
        // 실행될 내용 추가
        console.log("변경 감지")
    });

    fruitSelector.addEventListener("change", fruitDisplay)
})




function fruitDisplay() {
    console.log("과일 변경")
    let fruit = document.getElementById("fruitSelector").value;
    console.log(fruit);
    let result = document.getElementById("fruitResult")

    switch(fruit) { // if/else로 대체 가능하지만 가독성이 더 좋음.
        case "apple":
        case "APPLE": // 이런 경우가 있으므로 break 안 쓰면 계쏙 진행하도록 되어있음.
            result.innerText = "이것은 사과입니다."
            break; // 안 쓰면 계속 아래 코드 진행
        case "banana":
            result.innerText = "<b>이것은 바나나입니다.</b>"
            break; // 안 쓰면 계속 아래 코드 진행
        case "orange":
            result.innerHTML = "<b>이것은 오렌지입니다.</b>"
            break; // 안 쓰면 계속 아래 코드 진행
        case "pineapple":
            result.innerHTML = "이것은 파인애플입니다."
            break; // 안 쓰면 계속 아래 코드 진행
        default:
            result.textContent = "<b>몰러</b>"

    }

}