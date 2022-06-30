$(document).ready(function(){
    $("#category").change(function(){
        
        console.log($("#category").val());
        switch ($("#category").val()) { 
            case 'All': 
                $("tr").show();
                break;
            case 'Science': 
                $("tr:has(td)").hide();$(".Science").show();
                break;
            case 'General Knowledge': 
                $("tr:has(td)").hide();$(".General.Knowledge").show();
                break;		
            case 'English': 
                $("tr:has(td)").hide();$(".English").show();
                break;
            case 'History': 
                $("tr:has(td)").hide();$(".History").show();
                break;
            default:
                $("tr").show();
        }
    })
    
});