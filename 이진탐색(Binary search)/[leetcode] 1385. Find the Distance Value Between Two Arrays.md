### 1385. Find the Distance Value Between Two Arrays

<br>
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

<br>
The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

```
Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1


Constraints:

1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100

```

```js
var findTheDistanceValue = function (arr1, arr2, d) {
	let count = 0;
	// 조건에 해당하는 arr1 요소의 갯수를 세기 위해, arr1의 한 요소 el이 arr2의 모든 요소와 2 이상의 거리에 위치했다면, count를 1 증가시킵니다.
	arr1.forEach((el) => {
		count += binarySearch(el, arr2, d);
	});
	return count;
};

const binarySearch = (el, arr2, distance) => {
	//binearySearch를 사용하기 위해서는 기본적으로 요소들이 순서대로 정렬되어 있어야 합니다.
	const sortedArr2 = arr2.sort((a, b) => a - b);

	// 정렬된 arr2의 요소들 중 arr1의 한 요소 el과 거리가 2보다 큰 요소는 몇번째부터 등장하는지 알아내야 합니다.
	// 이 때 이진탐색을 사용하면 일일히 탐색하지 않고도 효율적으로 찾아낼 수 있습니다.

	// arr1의 요소 하나는 arr2의 모든 요소와의 거리가 2보다 커야 하므로, binarySearch()에서는
	// 모든 요소가 2보다 클 때 1을, 아닐 때 0을 리턴합니다.
	// 이는 arr2와의 모든 요소와의 거리가 2 이상인 arr1의 요소의 갯수를 세기 위함입니다.
	// 거리를 판별할 요소를 탐색할 때 이진탐색법을 사용합니다.

	let left = 0;
	let right = sortedArr2.length - 1;

	while (left <= right) {
		const mid = Math.floor((left + right) / 2);

		// arr2의 한 요소라도 arr1의 한 요소 el과 거리가 2보다 작으면 탈락이므로, 0을 리턴합니다.
		if (Math.abs(sortedArr2[mid] - el) <= distance) {
			return 0;
		} else if (sortedArr2[mid] <= el) {
			// 차이가 2보다 크다면, 다음 요소를 탐색해야 합니다. 이 중간값이 arr1의 요소 el보다 크면 왼쪽으로, 작으면 오른쪽으로 이어 탐색합니다.
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}

	// 탐색이 모두 끝났다면 모든 요소가 el과의 거리가 2보다 큰 것이므로 1을 리턴합니다.
	return 1;
};
```
