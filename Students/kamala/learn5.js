const studentScores =[
    10,85,92,78,88,95,80
];
const total=studentScores.reduce(function(total,current){
    console.log("value:",total,current)
    return total+ current
},0);
console.log("Total Marks Sum :",total)