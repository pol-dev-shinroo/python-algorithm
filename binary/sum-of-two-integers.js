const solution = (a, b) => {
  while (b != 0) {
    const carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
};

console.log(solution(1, 2));
