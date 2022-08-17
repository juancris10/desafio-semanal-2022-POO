

var lst= "juan"
var lst1= "uuuu"


var anagrama= true;
var cont;
var index;

if (lst.length != lst1.length) {
    anagrama= false
}else{
    cont=0
    while (anagrama && (cont < lst.length)) {
        index = lst1.indexOf(lst[cont])

        if (index == -1) {
            anagrama=false
        }
        else{
            lst1.split(index);
        }
        cont++
    }
}
if (anagrama){
    console.log(anagrama)
}else{
    console.log(false)
}