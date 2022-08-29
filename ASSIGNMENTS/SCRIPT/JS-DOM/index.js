const body = document.body

// APPENDING ELEMENTS
// body.append("HELLO WORLD - body.append")
// body.appendChild("HELLO WORLD - body.appendChild") //This will not work , coz we dont have Child Node

// CREATING ELEMENTS

const div = document.createElement('div')
div.innerText = "This is InnerText - div" //contains only the text contents which is displayed in browser 
// div.textContent = "This is Text content - div" //Display the Text contents even its display is Hidden or None
div.innerHTML = "<strong>This is Inner Html</strong>" //to render HTML
// body.append(div) //SUCCESS
body.appendChild(div) //SUCCESS
