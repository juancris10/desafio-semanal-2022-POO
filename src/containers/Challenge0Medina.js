let numeros=[]

for (let i = 1; i < 100; i++){
    
   numeros.push(i)
    
}
for ( let numero of numeros){
    if (numero % 3 == 0 ) {
        console.log('fizz')
    }else if (numero % 5 == 0) {
        console.log('buzz')
    }else {
        console.log('fizz buzz');}
}
    
