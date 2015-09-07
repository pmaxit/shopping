$(document).ready(function(){
    $(".list-group-item").click(function(event){

        // if it is already active, we won't do anything
        if($(this).hasClass('active'))
            return

        // hide any subgroup if openened
        $('.list-subgroups').slideUp()

        // change the class from active
        $(this).siblings('.list-group-item').removeClass('active')

        $(this).next('.list-subgroups').slideToggle('slow')

        $(this).addClass('active')
    })
})