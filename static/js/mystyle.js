 $(document).ready(function(){
    var length=51;
    for ( var i=1;i<length;i++)
    {
       $('#show-hide'+i).click(function(){
           brief=$(this).prev().prev();
           content=brief.next();
          if($(this).text()=="展开")
           {
            $(this).text("收起");
             brief.hide();
           if(brief.hide()){
             content.show('3000');
           }  
        }
        else{
          $(this).text("展开");
           content.hide();
           if(content.hide()){
             brief.show();
            var height=$(this).parent().next().offset().top;
            $('body,html').animate({scrollTop:height-60},1000);
           }  
        }
              
       });
    }

  	$('.scroll-top').click(function(){
       $('body,html').animate({scrollTop:0},1000);}) 	
   
  if($(window).width()>768){
    $.getScript("http://v3.jiathis.com/code_mini/jiathis_r.js?uid=1405995817902311&type=left&amp;move=0");
  }
  /* scroll-top button */
   $(window).scroll(function(){
    if(parseFloat($(window).scrollTop())>=100 && $(window).width()>768){
          $('.scroll-top').fadeIn();
        }
    else{
          $('.scroll-top').fadeOut();
    }
  });

      /* smooth scrolling sections */
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top - 65
        }, 1000);
        return false;
      }
    }
});    
  })