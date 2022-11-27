function solution(arr1, arr2) {
  let result = [];
  let row = [];
  const rowLength = arr1.length;
  const columnLength = arr1[0].length;

  for(j = 0; j < rowLength; j++) {
      row = [];
      for(i = 0; i < columnLength; i++) {
          row.push(arr1[j][i]+arr2[j][i]);
      }
      result.push(row);
  }
  return result;
}
