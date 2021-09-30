## 🎆문제
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

#### Example

For `a = [1, 2, 3]` and `b = [1, 2, 3]`, the output should be
`areSimilar(a, b) = true`.

The arrays are equal, no need to swap any elements.

For `a = [1, 2, 3]` and `b = [2, 1, 3]`, the output should be
`areSimilar(a, b) = true`.

We can obtain b from a by swapping 2 and 1 in b.

For `a = [1, 2, 2]` and `b = [2, 1, 1]`, the output should be
`areSimilar(a, b) = false`.

Any swap of any two elements either in a or in b won't make a and b equal.

## 🎇풀이
```js
function areSimilar(a, b) {
    let count = 0;
    let compareA = [];
    let compareB = [];
    let result;

  for(i=0; i<a.length; i++) {
      if(a[i] !== b[i]) {
          count++;
          compareA.push(a[i])
          compareB.push(b[i]);
      }
  }
  const stra = compareA.sort((a,b)=>{return a-b}).join('');
  const strb = compareB.sort((a,b)=>{return a-b}).join('');
  if(count === 0) {
      return true;
  }
    if(count === 2) {
        if(stra === strb) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

```

## ✨다른 풀이
```js
function areSimilar(a, b) {
    const ad = a.filter((v,i)=>v!=b[i])
    const bd = b.filter((v,i)=>v!=a[i])
    return ad.length == 0 || (ad.length == 2 && ad.join('') == bd.reverse().join(''))
}

```



