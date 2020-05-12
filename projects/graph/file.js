


// Add up and print the sum of the all of the minimum elements of each inner array:
const a = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
// The expected output is given by:
// 4 + -1 + 9 + -56 + 201 + 18 = 175

let total = 0
a.forEach(cv => {
  let min = Math.min(...cv)
  total += min
})
console.log(total)