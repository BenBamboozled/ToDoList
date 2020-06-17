
const list = document.getElementById("main");
const dateElement = document.getElementById("date-header");
const taskInput = document.getElementById("add-task");
const dateInput = document.getElementById("add-date");

// Classes names
const CHECK = "fa-check-square";
const UNCHECK = "fa-square";
const LINE_THROUGH = "lineThrough";

var d = new Date();

var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

dateElement.innerHTML = months[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();

$(document).ready(function() {

	$("#add").click( function(event) {
		event.preventDefault();
		console.log('click');

		if($('#add-date').val()=="" || $('#add-task').val() == ""){
			alert("Must add a task and date to add to the list");
		}
		else{

		$.ajax({
			type: 'POST',
			url: '/task/create/',
			data: {
				task:$('#add-task').val(), 
				date:$('#add-date').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
			},
			success: function(){
				window.location.reload();
			}

		});
	}

	 });

	 $("#clear-list").click( function(event) {
		event.preventDefault();
		
		if(confirm("Are you sure you want to clear the list? This will delete all tasks.")){
			$.ajax({
				type: 'GET',
				url: '/list/clear/',
				success: function(){
					window.location.reload();
				}
	
			});

		}

	 });

	

	 $( "i[job='complete']" ).click( function(event) {		
		event.preventDefault();

		$(this).toggleClass(CHECK);
		$(this).toggleClass(UNCHECK);

		$(this).parent().children("#task").toggleClass(LINE_THROUGH);
		$(this).parent().children("#date").toggleClass(LINE_THROUGH);

		$.ajax({
			type: 'GET',
			url: '/complete/' + $(this).parent().children("#box").attr("value"),
			success: function(){
			}

		});

	 });


	 $("i[job='delete']").click( function(event) {
		event.preventDefault();
		task = $(this).parent().children("#task").html()
		if(confirm("Are you sure you want to delete \"" + task + "\" from the list?")){
			$.ajax({
				type: 'POST',
				url: '/task/delete/',
				data: {
					value:$(this).parent().children("#box").attr("value"), 
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
				},
				success: function(){
					window.location.reload();
				}
	
			});
		}

	 });

	 
	 $("[job='task-detail']").click( function(event) {
		event.preventDefault();
		id = $(this).parent().children("#box").attr("value")
		
				
		window.location.replace('/task/'+id);
				
	
		});


	 $("#clear-input").click( function(event) {
		event.preventDefault();
		$('#add-task').val("");
		$('#add-date').val("")

	 });

	// JQuery code to be added in here.

});

