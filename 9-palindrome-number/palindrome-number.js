/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str=x.toString()
    let y=''
    for(let i=str.length-1;i>-1;i--)
    {
        y+=str[i]
    }
    return str==y
};