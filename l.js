let c=require("readline-sync");
let loop_time=c.questionInt("enter loop time: ");
 
var maxi=0;
let lis1=[ ]
for (let i=1;i<=loop_time;i++) {
   let num=c.questionInt("enter number: ")
   lis1.push(num)
}
console.log(lis1)
// var i=0
// var max=lis1[0]
// for(i of lis1){
//     if(lis1[i]>max){
//         max=lis1[i]
//     }
var max=lis1[0]
for (i in lis1){
    if(lis1[i]>max){
        max=lis1[i]
    }
}
console.log(max,"max")

    