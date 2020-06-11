const list = document.getElementById('list');


// Classes names
const CHECK = "fa-check-square";
const UNCHECK = "fa-square";
const LINE_THROUGH = "lineThrough";

function completeToDo(element){
	element.classList.toggle(CHECK);
	element.classList.toggle(UNCHECK);

	element.parentNode.querySelector(".task").classList.toggle(LINE_THROUGH);

	LIST[element.id].done ?  false : true;
}

list.addEventListener("click", function(event){
	let element = event.target;
	const elementJob = event.target.attributes.job.value;

	if(elementJob== "complete"){
		completeToDo(element);
	}

});