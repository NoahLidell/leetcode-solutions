
function * fiboSeq() {
  let n1 = 2;
  let n2 = 1;
  let num;
  while (true) {
    num = n1 + n2;
    yield num;
    n2 = n1;
    n1 = num;
  }
}

var climbStairs = function(n) {
    fib = fiboSeq();
    if (n < 3) {
        return n;
    } else {
        for (i = 2; i < n; i++) {
            stairs = fib.next().value;
        }
    }
    return stairs;
};

