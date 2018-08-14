
(function($) {
    
    $.fn.fold_menu = function(b) {
        
        var c,
        item,
        httpAdress;
        b = jQuery.extend({
            Speed: 220,
            autostart: 1,
            autohide: 1
        },
        b);
        c = $(this);
        item = c.children("ul").parent("li").children("a");
        httpAdress = window.location;
        for (var i = item.length - 1; i >= 0; i--) {
            if($(item[i]).attr("class") != "active"){
                $(item[i]).addClass("inactive");
            }
        };
        function _item() {
            var a = $(this);
            if (b.autohide) {
                a.parent().parent().find(".active").parent("li").children("ul").slideUp(b.Speed / 1.2, 
                function() {
                    $(this).parent("li").children("a").removeAttr("class");
                    $(this).parent("li").children("a").attr("class", "inactive")
                })
            }
            if (a.attr("class") == "inactive") {
                a.parent("li").children("ul").slideDown(b.Speed, 
                function() {
                    a.removeAttr("class");
                    a.addClass("active")
                })
            }
            if (a.attr("class") == "active") {
                a.removeAttr("class");
                a.addClass("inactive");
                a.parent("li").children("ul").slideUp(b.Speed)
            }
        }

        item.unbind('click').click(_item);
        
    }
})(jQuery);