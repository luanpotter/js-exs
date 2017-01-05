(function () {

  const process = function (op1, o, op2) {
    /** --- SEU CÓDIGO AQUI --- **/
    return 42; // ...
    /** ----------------------------------- **/
  };

  let operand1 = document.getElementById('operand1').value;
  let operator = document.getElementById('operator').value;
  let operand2 = document.getElementById('operand2').value;

  document.getElementById('button').addEventListener('click', () => {
    let result = process(operand1, operator, operand2);
    document.getElementById('result').innerHTML = result;
  });

})();