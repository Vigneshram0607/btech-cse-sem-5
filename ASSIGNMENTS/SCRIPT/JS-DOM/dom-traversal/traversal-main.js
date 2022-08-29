var itemList = document.querySelector('#items');

// console.log(itemList.childNodes);
// // console.log(itemList.appendChild(inner));

// console.log(itemList.parentNode);

// console.log(itemList.parentElement);

// itemList.children[0].style.backgroundColor= 'yellow';
// itemList.firstElementChild.textContent= 'first-item';
// itemList.lastElementChild.textContent = 'last-item'

//nextSibling()
// console.log(itemList.nextSibling);
// console.log(itemList.nextElementSibling);

//previousSibling()
// console.log(itemList.previousElementSibling);

//Create Element:
var newDiv = document.createElement('div');
//add class
newDiv.className = 'newdiv-classname';

//add id
newDiv.id = 'newdov-id'; 

//add attr
newDiv.setAttribute('title','newdiv-attr');

//create text node:
var newDivText = document.createTextNode('Hello World This is New Div');
newDiv.appendChild(newDivText);

var container = document.querySelector('header .container');
var h1 = document.querySelector('header h1');

console.log(newDiv);
newDiv.style.fontSize = '30px'
container.insertBefore(newDiv, h1);

var btn = document.getElementById('btn-btn').addEventListener('click', buttonClick);
// .addEventListener('click', buttonClick);
console.log(btn);
function buttonClick(){
    document.getElementById('header-title').textContent = 'This is Changed After click'
    console.log("button cicked");
}

//div-box: 
var box = document.getElementById('test-box');
// box.addEventListener('click',runEvent);
// box.addEventListener('dblclick',runEvent);

// box.addEventListener('mouseenter',textFunct);

box.addEventListener('mousemove',textFunct);

box.addEventListener('mouseleave',runEvent);

// box.addEventListener('mouseover',runEvent);
// box.addEventListener('mouseup',runEvent);

//function for div-box eventListeners
function runEvent(e){
    console.log('EVENT TYPE: '+e.type);
    box.style.color = 'black';

}

function textFunct(e){
    document.body.style.backgroundColor = 'rgb('+e.offsetX+','+e.offsetY+',40)';
}

//INPUT TEXT VALUE:
var inputInput = document.querySelector("input[type='text']");
var form = document.querySelector('form');
var selectInput = document.querySelector('select');


inputInput.addEventListener('keydown', textFunc);
inputInput.addEventListener('focus', focusEvent);

selectInput.addEventListener('change',selectFunc);
selectInput.addEventListener('input',selectFunc);

form.addEventListener('submit', formFunc);

function formFunc(e){
    e.preventDefault(); //to prevent from refreshing after clicking submit
    console.log("EVENT TYPE : "+e.type);


}

function selectFunc(e){
    console.log("SELECT : "+e.target.value);
}

function focusEvent(e){
    console.log('EVENT TYPE: '+e.type);
    
}

function textFunc(e){
    console.log('EVENT TYPE: '+e.type);
    console.log(e.target.value);
    box.innerHTML = 'OUTPUT: <h3>'+e.target.value+'</h3>';

}