

function fnFibo(numero){
    if(numero==0){
        return 0
    }else if (numero ==1){
        return 1
    }else{
        return (fnFibo(numero -2) + fnFibo(numero-1))}
}

var num=50

for (i=0; i < num; i++){
    console.log(fnFibo(i))

}

