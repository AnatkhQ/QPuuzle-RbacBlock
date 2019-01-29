
!function($) {
    "use strict";

    var SweetAlert = function() {};

    //examples 
    SweetAlert.prototype.init = function() {

    //Basic
    $('#sa-basic').click(function(){
        swal("Here's a message!");
    });

    //A title with a text under
    $('#sa-title').click(function(){
        swal("Here's a message!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat eleifend ex semper, lobortis purus sed.")
    });

    //Success Message
    $('#sa-success').click(function(){
        swal("Good job!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat eleifend ex semper, lobortis purus sed.", "success")
    });

    //Warning Message
    $('.sa-warning').click(function(){
        var pk = $(this).attr('id');
        console.log(pk);
        swal({
            title: "你确定要删除吗?",
            text: "你将无法恢复它!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "确认删除!",
            closeOnConfirm: false ,
            showLoaderOnConfirm: true
        }, function(){
            $.ajax(
                    {
                        type: "post",
                        url: "/rbac/role/del/",
                        data: {
                            pk:pk
                        },
                        success: function(data){
                            console.log(data);
                            if(data.msg){
                                swal("成功删除!", "所选记录以删除", "success");
                                window.location.reload();
                            }else{
                                swal("删除失败!", "所选记录未删除", "error")
                            }
                        }
                    }
            );

        });
    });

    //Parameter
    $('#sa-params').click(function(){
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this imaginary file!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes, delete it!",
            cancelButtonText: "No, cancel plx!",
            closeOnConfirm: false,
            closeOnCancel: false
        }, function(isConfirm){
            if (isConfirm) {
                swal("Deleted!", "Your imaginary file has been deleted.", "success");
            } else {
                swal("Cancelled", "Your imaginary file is safe :)", "error");
            }
        });
    });

    //Custom Image
    $('#sa-image').click(function(){
        swal({
            title: "Title",
            text: "Lorem ipsum dolor sit amet, consectetur",
            imageUrl: "assets/images/users/avatar-1.jpg"
        });
    });

    //Auto Close Timer
    $('#sa-close').click(function(){
         swal({
            title: "Auto close alert!",
            text: "I will close in 2 seconds.",
            timer: 2000,
            showConfirmButton: false
        });
    });


    },
    //init
    $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.SweetAlert.init()
}(window.jQuery);