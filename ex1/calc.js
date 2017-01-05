(function () {

  const process = function (op1, o, op2) {
    /** --- SEU CÓDIGO AQUI --- **/
    return 42; // ...
    /** ----------------------------------- **/
  };

  let operand1 = document.getElementById('operand1');
  let operator = document.getElementById('operator');
  let operand2 = document.getElementById('operand2');

  document.getElementById('button').addEventListener('click', () => {
    let result = process(operand1.value, operator.value, operand2.value);
    document.getElementById('result').innerHTML = result;
  });

})();
