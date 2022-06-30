$(document).ready(function(){

  $(" tbody #rows").each(function() {
    if ($(this).find("td")[1].innerHTML == $(this).find("td")[2].innerHTML){
      $(this).toggleClass("table-success");
    }
    
    if ($(this).find("td")[1].innerHTML != $(this).find("td")[2].innerHTML){
      $(this).toggleClass("table-danger");
    }  
    
   
   });
  
  
  });