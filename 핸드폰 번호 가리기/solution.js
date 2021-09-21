function solution(phone_number) {
  const keepNum = phone_number.slice(-4);
  const hideNum = new Array(phone_number.length-4).fill('*').join('');
  return hideNum + keepNum;
}
