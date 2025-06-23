function number_inc() {
            // console.log('+1')

            // let number = document.getElementById('result').textContent ;  
            // div 요소 안에 잇는 글을 가져오는 방식
            // innerText :  글자만 가져옴(디자인 속성을 적용받음)
            // innerHTML : 글자와 그 태그까지 함께 가져온다
            // textContent : 순수 글자만 가져옴

            // console.log(number) ;

            // let result= number + 1;
            // document.getElementById('result').textContent = result;

            // let result = number.textContent + 1;
            // number.textContent = result;


            // let result = Number(number.textContent) + 1; 
            // number.textContent = result;

            let number = document.getElementById("result");
            let number_string = number.textContent;
            console.log(number_string)
            
            let number_string_to_number = Number(number_string);
            let result = number_string_to_number + 1
            console.log(result)

            number.textContent = result;

        }
        function number_dec() {
            // console.log('-1')
            // let result = document.getElementById('result');
            // result.textContent = Number(result.textContent) - 1;

            document.getElmentById('result').textContent =- 1;
        }