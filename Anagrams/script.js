document.addEventListener('DOMContentLoaded', function(){
    var checkButton= document.getElementById('checkButton');
    checkButton.addEventListener('click', function(){
        checkanagram();
    });
});
function checkanagram(){
    var string1= document.getElementById("string1")
    var string2= document.getElementById("string2")
    if (string1.length != string2.length){
        document.getElementById("result").innerText="Not Anagrams"
    }
    else{
        string1= string1.toLowerCase();
        string2= string2.toLowerCase();
        sorted1= string1.sort();
        sorted2= string2.sort();
        if(sorted1 == sorted2){
            document.getElementById("result").innerText="Strings are Anagrams"
        }else{
            document.getElementById("result").innerText="Strings are not Anagrams"
        }
    }
}
    