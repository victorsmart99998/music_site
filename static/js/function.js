const monthNames = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June',
  'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
];
$("#comment-form").submit(function(e){
    e.preventDefault();
    console.log("button clicked.....");

    let dt = new Date();
    let time = dt.getDay() + "" + monthNames[dt.getUTCMonth()] + "," + dt.getFullYear()

    $.ajax({
          data: $(this).serialize(),
          method: $(this).attr("method"),
          url: $(this).attr("action"),
          dataType: 'json',

          success: function(res){
            console.log("comment save to DB....");

           if(res.bool == true){
           $(".review-res").html("Review added successfully..")

           let _html = '<div class="row mb-3 border p-2 rounded shadow-sm gx-2">'

               _html += '<div class="col-md-12 d-flex">'
               _html += '<div class="m-2">'
               _html += '<div class="bg-success d-flex justify-content-center align-items-center text-white mt-3 commenter-icon">'
               _html += '<h3 class="mt-2">T </h3>'
               _html += '</div>'
               _html += '</div>'
               _html += '<div class="mt-4 m-2">'
               _html += '<p class="text-dark text-bold ">'
               _html += '<b>'+ res.context.user +'</b>'
               _html += '<br>'
               _html += '<span class="mt-3 text-success">'+ res.context.review +'</span>'
               _html += '<br>'
               _html += '<small><i class="fa fa-clock mr-2"></i>'+ time +'</small>'
               _html += '</p>'
               _html += '</div>'
               _html += '</div>'
               _html += '</div>'
               $(".comment-list").prepend(_html)
           }
           }
        })
    })



