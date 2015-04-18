$(function() {
    //model
    
    var A_article=Backbone.Model.extend(
    {
      initialize:function(){},
      url:'/latest'
    });
    var a_article=new A_article();
    var articles=new Array();
    var _fetch=null;
    a_article.fetch({
      success:function(model,response){
         var data=response.data;
        $(data).each(function(i){
           $('#links').append("<li><a href='#post/"+i+"'>"+this.title+"</a></li>");
           articles[i]=this;
        })
          $('#brand').html(articles[0]['title']);
          $('#title').html(articles[0]['title']);
          $('#time').html(articles[0]['pubdate']);
          $('#content').html(articles[0]['descr']+articles[0]['content']);
          $('#from').html('<p>转自：'+articles[0]['article']+'<span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></p>');
      },
      error:function(){
        console.log("err")
      }
    })
    //router
    var $divBrand=$("#brand");
    var $divShow=$("#content");
    var $divTitle=$("#title");
    var $divTime=$("#time");
    var $divFrom=$("#from");
    //action方式触发
    var testrouter=Backbone.Router.extend({
      routes:{
        '':'main',
        'post/:key':'article_read',
      },
      main:function(){
        $divTitle.html(articles[0]['title']);
        $divTime.html(articles[0]['pubdate']);
        $divShow.html(articles[0]['descr']+articles[0]['content']);
        $divFrom.html('<p>转自：'+articles[0]['article']+'<span><a href="'+articles[0]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></p>');
      },
      article_read:function(key){
        $divBrand.html(articles[key]['title']);
        $divTitle.html(articles[key]['title']);
        $divTime.html(articles[key]['pudate']);
        $divShow.html(articles[key]['descr']+articles[key]['content']);
        $divFrom.html('<p>转自：'+articles[key]['article']+'<span><a href="'+articles[key]['link']+'" style="float:right;color:#A36D6D" target="_blank"><i class="glyphicon glyphicon-eye-open"></i>查看原文</a></span></p>');
        $('html,body').animate({scrollTop: 0}, 100);

      },
     
    });
    var router=new testrouter();
    Backbone.history.start();

  });